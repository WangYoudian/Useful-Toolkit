'''
1. ( a + b ) % c = ( ( a % c ) + ( b % c ) ) % c

2. ( a * b ) % c = ( ( a % c ) * ( b % c ) ) % c

3. ( a – b ) % c = ( ( a % c ) – ( b % c ) ) % c
--------------------- 
作者：扬俊酱 
来源：CSDN 
原文：https://blog.csdn.net/qq_19782019/article/details/85621386 
版权声明：本文为博主原创文章，转载请附上博文链接！
'''
import time

MOD = 1000
def fastPower(base, power):
	res = 1
	while power > 0:
		if power&1:
			res = res * base % MOD
		power >>= 1
		base = base * base % MOD
	return res

def main():
	base = 2
	power = 100000000
	print(fastPower(base, power))

if __name__ == '__main__':
	start = time.clock() # float type
	main()
	end = time.clock()
	print("The program takes %.6f seconds" %(end - start))
	print(end-start)