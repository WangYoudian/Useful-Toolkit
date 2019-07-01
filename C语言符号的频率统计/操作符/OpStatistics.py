import re
import os
from comment_remover import comment_remover

def traverse(folder):
    global d
    for root, dirs, files in os.walk(folder):
        if files:
            for file in files:
                filename = os.path.join(root,file)
                if os.path.splitext(filename)[1] in suffix:
                    stat(filename, d)
        if dirs:
            for directory in dirs:
                print(directory)
                traverse(directory)
def stat(file, d):
	with open(file, 'r', errors='ignore') as f:
		text = comment_remover(f.read())
		for key in d:
			op_pattern = re.compile(key)
			res = re.findall(op_pattern, text)
			d[key] += len(res)
		f.close()

suffix = ['.c', '.h']
operators = {}
pattern = re.compile(r'r\'(.*?)\'')

# init dictionary
with open('operators.txt', 'r') as f:
	# regex match
	for i, line in enumerate(f):
		res = re.search(pattern, line)
		if res:
			op = res.group(1)
			operators[op] = 0
	f.close()
# print(operators)
# 46
# print(len(operators))
# exclude '--' or '->'
if '-' in operators:
	operators.pop('-')
	operators[' - '] = 0
# exclude '+='
if '\\+' in operators:
	operators.pop('\\+')
	operators['\\+[^=]'] = 0
# exclude '/='
if '/' in operators:
	operators.pop('/')
	operators[' / '] = 0
# while '*' is denoted for pointer
if '>=' in operators:
	operators.pop('>=')
	operators[' >= '] = 0
if '<=' in operators:
	operators.pop('<=')
	operators[' <= '] = 0
if '>' in operators:
	operators.pop('>')
	operators[' > '] = 0
if '<' in operators:
	operators.pop('<')
	operators[' < '] = 0
# exclude from other assignment operators
if '=' in operators:
	operators.pop('=')
	operators[' = '] = 0

# for test
with open('bootp.c', 'r') as f:
	text = comment_remover(f.read())
	for key in operators:
		op_pattern = re.compile(key)
		res = re.findall(op_pattern, text)
		operators[key] += len(res)
	f.close()
# print(operators)
# {'\\+': 10, '-': 19, '\\*': 23, '/': 10, '%': 9, '\\|': 4, '&': 3, '~': 1, '\\^': 0, '<<': 1, '>>': 4, '\\|\\|': 1, '&&': 0, '!': 2, '<': 13, '>': 35, '<=': 1, '>=': 2, '==': 0, '!=': 2, '=': 29, '\\*=': 0, '/=': 0, '%=': 0, '\\+=': 0, '-=': 0, '<<=': 1, '>>=': 1, '&=': 0, '\\|=': 1, '\\^=': 0, '\\+\\+': 0, '--': 0, '->': 16, '\\?': 0, '\\(': 72, '\\)': 72, '\\[': 8, '\\]': 8, '\\{': 9, '\\}': 9, ',': 36, '\\.': 16, ';': 59, ':': 2, '\\.\\.\\.': 1}
# print(text)

folder = 'C:/Users/win10/Downloads/linux-master'
d = operators
d = {'\\*': 1994052, '%': 472310, '\\|': 515693, '&': 1437335, '~': 59138, '\\^': 8832, '<<': 232802, '>>': 69435, '\\|\\|': 91524, '&&': 128565, '!': 434957, '==': 261377, '!=': 119490, '\\*=': 2445, '/=': 2011, '%=': 478, '\\+=': 59944, '-=': 14745, '<<=': 2596, '>>=': 3624, '&=': 41252, '\\|=': 99879, '\\^=': 2798, '\\+\\+': 145393, '--': 31006, '->': 3253808, '\\?': 63134, '\\(': 7304055, '\\)': 7304061, '\\[': 731193, '\\]': 731059, '\\{': 1949359, '\\}': 1949294, ',': 8599584, '\\.': 1917629, ';': 7243435, ':': 638817, '\\.\\.\\.': 11883, ' - ': 109456, '\\+[^=]': 446940, ' / ': 35512, ' >= ': 42947, ' <= ': 22356, ' > ': 66438, ' < ': 182144, ' = ': 3004730}
# traverse(folder)
# [Finished in 382.3s]
print(d)

# frequency
with open('frequency.txt', 'w+') as f:
	for key in d:
		f.write(key + ':' + str(d[key]) + '\n')

# probability
denominator = 0
for key in d:
    denominator += d[key]
# 将字典中的信息写入文件record.txt
with open('record.txt', 'w+') as f:
    for key in d:
        d[key] = ('%.4f' %(d[key]/denominator))
        f.write(key + ':' + str(d[key]) + '\n')
    f.close()
