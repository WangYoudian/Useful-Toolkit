#分别用九行和十行代码求解
nums = range(1, 3001)
cnt2, cnt5 = 0, 0
for i in nums:
	while i % 2 == 0:
		i //= 2
		cnt2 += 1
	while i % 5 == 0:
		i //= 5
		cnt5 += 1
	#print(cnt2, cnt5)
print(cnt5)

from functools import reduce
def times(x, y):
	return x*y
t = reduce(times, range(1, 3001))
cnt = 0
while t % 10 == 0:
	cnt += 1
	t //= 10
print(cnt)

#不使用循环，如何找出一个末尾有多个零的数末尾连续零的个数。