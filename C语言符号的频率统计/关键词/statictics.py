import os

# 定义关键词字母表
alphabet = ['auto','break','case','char','const','continue','default','do',\
            'double','else','enum','extern','float','for','goto','if',\
            'int','long','register','return','short','signed','sizeof','static',\
            'struct','switch','typedef','union','unsigned','void','volatile','while']
suffix = ['.c', '.h']

# 字典存储
DICT = {}
for keyword in alphabet:
    DICT[keyword] = 0

# 遍历文件夹，通过后缀名来判断c源文件，并读取代码信息
# 进行词频统计
def traverse(folder):
    global d
    for root, dirs, files in os.walk(folder):
        if files:
            for file in files:
                filename = os.path.join(root,file)
                if os.path.splitext(filename)[1] in suffix:
                    stat(filename, DICT)
        if dirs:
            for directory in dirs:
                print(directory)
                traverse(directory)

def stat(file, d):
    words = []
    with open(file, 'r', errors='ignore') as f:
        for i, line in enumerate(f):
            words += line.replace('\n','').replace('\t','').split(' ')
    for word in words:
        if word in d:
            d[word] += 1

FILESYSTEM = 'C:/Users/win10/Downloads/linux-master'
# [Finished in 241.2s]
# traverse(FILESYSTEM)
# DICT = {'auto': 1252, 'break': 1138, 'case': 14699, 'char': 95635, \
#  'const': 147830, 'continue': 1459, 'default': 10788, \
#  'do': 24336, 'double': 1152, 'else': 91908, 'enum': 25745, \
#  'extern': 197, 'float': 293, 'for': 237718, 'goto': 936, \
#  'if': 138137, 'int': 420882, 'long': 119497, 'register': 34653, \
#  'return': 24468, 'short': 11025, 'signed': 773, 'sizeof': 1656, \
#  'static': 1693, 'struct': 388855, 'switch': 4974, 'typedef': 132, \
#  'union': 4705, 'unsigned': 116660, 'void': 203138, 'volatile': 2407, 'while': 19346}
DICT = {'auto': 1283, 'break': 1647, 'case': 245281, 'char': 118540, \
        'const': 201463, 'continue': 1603, 'default': 11271, 'do': 34724, \
        'double': 1620, 'else': 182761, 'enum': 67035, 'extern': 38270, \
        'float': 829, 'for': 330663, 'goto': 157655, 'if': 1225682, 'int': 757004, \
        'long': 126724, 'register': 39241, 'return': 753273, 'short': 12079, \
        'signed': 1074, 'sizeof': 1730, 'static': 615569, 'struct': 1090692, \
        'switch': 49507, 'typedef': 15423, 'union': 17312, 'unsigned': 280615, \
        'void': 329291, 'volatile': 4586, 'while': 46306}
print(DICT)

# 通过频率估计概率，得到一个范围在0~1之间的概率
denominator = 0
for key in alphabet:
    denominator += DICT[key]
# 将字典中的信息写入文件record.txt
with open('record.txt', 'w+') as f:
    for key in alphabet:
        DICT[key] = ('%.4f' %(DICT[key]/denominator))
        f.write(key + ':' + str(DICT[key]) + '\n')
    f.close()
