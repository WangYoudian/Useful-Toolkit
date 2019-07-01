import math
import random
import sys
'''
上调N的取值,则调和和就越接近欧拉误差gama的值
'''
N = 100
gama = 0.57721556
sum = 0
for i in range(1, N+1):
	sum += 1/i 
print('在1-%d范围内,调和和%f与近似值logN的误差约是:\n%f'
		%(N, sum, sum-math.log(N)))
print('这与gama=%f的近似值相差约:\n%f' %(gama, abs(gama-(sum-math.log(N)))))

print()

k = random.randint(0, 10)
sum = 0
if k != -1:
	final = N**(k+1)/abs(k+1)
	for i in range(1, N+1):
		sum += i**k
	print('i的任意k次方(k不等于-1)求和与近似值公式的误差为：\n%d' %abs(sum-final))
	print('其中,本次测试中,k=%d' %k)
	print('误差百分比占：%%%f' %(100*(sum-final)/sum))
else:
	print('k等于-1,程序退出！')
