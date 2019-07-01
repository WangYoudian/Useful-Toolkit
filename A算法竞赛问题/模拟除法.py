# 立华奏在学习初中数学的时候遇到了这样一道大水题：
# “设箱子内有 n 个球，其中给 m 个球打上标记，设一次摸球摸到每一个球的概率均等，求一次摸球摸到打标记的球的概率”
# “emmm...语言入门题”
# 但是她改了一下询问方式：设最终的答案为 p ,请输出 p 小数点后 K_1 到 K_2 位的所有数字（若不足则用 0 补齐）

def fastPower(base, power, MOD):
    res = 1
    while power > 0:
        if power&1:
            res = res*base%MOD
        power >>= 1
        base = base*base%MOD
    return res
 
T = int(input())
for _ in range(T):
    m, n, k1, k2 = map(int, input().split())
    kth_digit = (m%n * fastPower(10, k1-1, n))%n
    while k1 <= k2:
        kth_digit *= 10
        print(kth_digit//n, end='')
        kth_digit %= n
        k1 += 1
    print()