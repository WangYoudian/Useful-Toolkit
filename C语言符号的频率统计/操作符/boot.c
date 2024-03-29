 
 
#include <linux/kernel.h>
#include <linux/slab.h>
#include <linux/string.h>
#include <generated/utsrelease.h>
#include <linux/mm.h>

#include <asm/console.h>
#include <asm/hwrpb.h>
#include <asm/pgtable.h>
#include <asm/io.h>

#include <stdarg.h>

#include "ksize.h"

extern unsigned long switch_to_osf_pal(unsigned long nr,
	struct pcb_struct * pcb_va, struct pcb_struct * pcb_pa,
	unsigned long *vptb);

extern void move_stack(unsigned long new_stack);

struct hwrpb_struct *hwrpb = INIT_HWRPB;
static struct pcb_struct pcb_va[1];

 

static inline void *
find_pa(unsigned long *vptb, void *ptr)
{
	unsigned long address = (unsigned long) ptr;
	unsigned long result;

	result = vptb[address >> 13];
	result >>= 32;
	result <<= 13;
	result |= address & 0x1fff;
	return (void *) result;
}	

 

#define VPTB	((unsigned long *) 0x200000000)
#define L1	((unsigned long *) 0x200802000)

void
pal_init(void)
{
	unsigned long i, rev;
	struct percpu_struct * percpu;
	struct pcb_struct * pcb_pa;

	 
	pcb_va->ksp = 0;
	pcb_va->usp = 0;
	pcb_va->ptbr = L1[1] >> 32;
	pcb_va->asn = 0;
	pcb_va->pcc = 0;
	pcb_va->unique = 0;
	pcb_va->flags = 1;
	pcb_va->res1 = 0;
	pcb_va->res2 = 0;
	pcb_pa = find_pa(VPTB, pcb_va);

	 
	srm_printk("Switching to OSF PAL-code .. ");

	i = switch_to_osf_pal(2, pcb_va, pcb_pa, VPTB);
	if (i) {
		srm_printk("failed, code %ld\n", i);
		__halt();
	}

	percpu = (struct percpu_struct *)
		(INIT_HWRPB->processor_offset + (unsigned long) INIT_HWRPB);
	rev = percpu->pal_revision = percpu->palcode_avail[2];

	srm_printk("Ok (rev %lx)\n", rev);

	tbia();  
}

static inline void
load(unsigned long dst, unsigned long src, unsigned long count)
{
	memcpy((void *)dst, (void *)src, count);
}

 
static inline void
runkernel(void)
{
	__asm__ __volatile__(
		"bis %0,%0,$27\n\t"
		"jmp ($27)"
		:  
		: "r" (START_ADDR));
}

extern char _end;
#define KERNEL_ORIGIN \
	((((unsigned long)&_end) + 511) & ~511)

void
start_kernel(void)
{
	 
	static long nbytes;
	static char envval[256] __attribute__((aligned(8)));
	static unsigned long initrd_start;

	srm_printk("Linux/AXP bootp loader for Linux " UTS_RELEASE "\n");
	if (INIT_HWRPB->pagesize != 8192) {
		srm_printk("Expected 8kB pages, got %ldkB\n",
		           INIT_HWRPB->pagesize >> 10);
		return;
	}
	if (INIT_HWRPB->vptb != (unsigned long) VPTB) {
		srm_printk("Expected vptb at %p, got %p\n",
			   VPTB, (void *)INIT_HWRPB->vptb);
		return;
	}
	pal_init();

	 
	initrd_start = ((START_ADDR + 5*KERNEL_SIZE + PAGE_SIZE) |
			(PAGE_SIZE-1)) + 1;
#ifdef INITRD_IMAGE_SIZE
	srm_printk("Initrd positioned at %#lx\n", initrd_start);
#endif

	 
	move_stack(initrd_start - PAGE_SIZE);

	nbytes = callback_getenv(ENV_BOOTED_OSFLAGS, envval, sizeof(envval));
	if (nbytes < 0 || nbytes >= sizeof(envval)) {
		nbytes = 0;
	}
	envval[nbytes] = '\0';
	srm_printk("Loading the kernel...'%s'\n", envval);

	 

	 

#ifdef INITRD_IMAGE_SIZE
	load(initrd_start, KERNEL_ORIGIN+KERNEL_SIZE, INITRD_IMAGE_SIZE);
#endif
        load(START_ADDR+(4*KERNEL_SIZE), KERNEL_ORIGIN, KERNEL_SIZE);
        load(START_ADDR, START_ADDR+(4*KERNEL_SIZE), KERNEL_SIZE);

	memset((char*)ZERO_PGE, 0, PAGE_SIZE);
	strcpy((char*)ZERO_PGE, envval);
#ifdef INITRD_IMAGE_SIZE
	((long *)(ZERO_PGE+256))[0] = initrd_start;
	((long *)(ZERO_PGE+256))[1] = INITRD_IMAGE_SIZE;
#endif

	runkernel();
}

