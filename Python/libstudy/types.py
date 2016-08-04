# encoding: utf-8
"""
内置类型
@author Yuriseus
@create 2016-6-24 16:32
"""

import math

if 0 or 0.0 or () or {} or [] or '':
    print('True')
else:
    print('False')

# 对于自定义的类，实现__bool__函数

print(2**3)

c = complex(10, 2)    # (10+2j)
cc = c.conjugate()    # (10-2j) 共轭复数

n = 3.1415926
math.trunc(n)    # 3
round(n, 2)  # 3.14，保留2位小数

n = 10
t = bin(n)    # 0b1010
n.bit_length()    # 4

t = n.to_bytes(2, byteorder='big')    # b'\x00\n'
int.from_bytes(t, byteorder='big') # 10

a1 = [1, 2, 3]
a2 = [4, 5, 6]
t = a1 + a2    # 列表合并，[1, 2, 3, '222a', 4, 5, 6]
t = a1 * 3     # 重复3次，[1, 2, 3, 1, 2, 3, 1, 2, 3]

lists = [[]] * 3
lists[0].append(20)
print(lists)    # [[20], [20], [20]]

s = 'hello woRld'
s.capitalize()   # Hello world 首字母大写
s.lower()        # 转小写，对ASCII编码的字母有效
s.casefold()     # 转小写，Unicode 编码中凡是有对应的小写形式的，都会转换
print(t)

