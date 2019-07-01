from decimal import *
T = int(input())
for _ in range(T):
    m, n, K1, K2 = map(int, input().split())
    getcontext().prec = K2+1
    res = Decimal(m)/Decimal(n)
    if len(str(res)) < K2+1:
        res = ("%.{0}f".format(K2+1) %(res))
    ans = str(res)[K1+1:K2+2]
    print(ans)

'''
输入:
5
2 3 2 3
1 7 1 7
2 5 1 3
12345 54321 3 10
12345 54321 100000 100010

输出
复制

66
1428571
400
72601756
78428232175
'''