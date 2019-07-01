nums = []
for i in range(19, 99+1, 2):
    nums.append(i)
print('result of 19*99:', sum(nums)//(len(nums)))

# 解决诸如求解a*b定义问题
# a和b之间奇偶性和a相同的所有数平均值，只给定平均值和b
def countSameParitySum(b, mean):
    flag = 0
    container = []
    i = 1
    while flag <= 1:
        same_parity = []
        symbol = i%2
        if i > b:
            temI, temB = b, i
        else:
            temI, temB = i, b
        # parse the form 
        if temI%2 != symbol:
            temI += 1
        for j in range(temI, temB+1, 2):
            same_parity.append(j)
        if sum(same_parity)//(len(same_parity)) == mean:
            container += [i]
            flag += 1
        i += 1
    return container

print(countSameParitySum(59, 80))