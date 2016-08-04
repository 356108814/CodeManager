# encoding: utf-8
"""
built functions
@author Yuriseus
@create 2016-6-13 18:03
"""

print(ascii(u'我'))

b = bin(3)    # 转成二进制0b11

ba = bytearray('a', 'utf-8')    # ba[0]==97
print(len(ba))
for b in ba:
    print(b)    # 97

bo = bytes('我', 'utf-8')    # 转为字节对象b'\xe6\x88\x91'，对象不可修改

c = chr(65)    # A，int转Unicode字符串


class A(object):
    @classmethod
    def cm(cls, name):
        print(cls, name)    # <class '__main__.A'> hello

    @staticmethod
    def sm(name):
        print(name)    # hello

# 默认第一个参数都是类对象
A.cm('hello')
A().cm('hello')

A.sm('hello')
print(c)

code = 'for x in range(10):' \
       '    print(x)'

exec(compile(code, '', 'exec'))

divmod(7, 3)    # (2, 1)返回商和余数

print('================filter================')
a = [{'id': 1, 'name': 'A'}, {'id': 2, 'name': 'B'}, {'id': 3, 'name': 'C'}]
# a = [1, 2, 3]

def is_a(data):
    return data['name'] == 'A'
a = filter(is_a, a)    # {'id': 1, 'name': 'A'}

# ================frozenset================
s = frozenset(['a', 'b', '1'])    # 不可变的set
d = {s: 1}   # 可以作为键
print(d[s])

# ================hash================
hash(110)      # 110
hash('110')    # 1898876750133563518

help(list)    # 打印出对象所属类型帮助信息

a = {}
print(id(a))    # 整数，对象的唯一标识
a['name'] = 'a'
print(id(a))    # 12015752

with open('README.md') as f:
    for line in iter(f.readline, ''):
        print(line)

# print(memoryview(111))

oct(8)    # 转为八进制010
chr(97)   # a,ascii转字符
ord('a')  # 97,字符转ascii

print(pow(10, 3))    # 1000，10的3次方


class Person(object):
    def __init__(self):
        self._name = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name


for x in range(1, 10, 2):   # 不包含10，步长为2
    print(x)     # 1 3 5 7 9

print(repr(list))    # 可打印字符串。对象需要实现__repr__

a = [1, 2, 3]
reversed(a)    # 返回一个反转的可迭代的对象。a[0] == 3

round(2.472)           # 四舍五入 2
round(2.572)           # 3
round(2.472, 2)        # 2.47，保留2位小数


a = [3, 4, 5, 6, 7, 8, 9]
print(a[1:5])    # [4, 5, 6, 7]，5为步进最大数，不包含5
print(a[0:5:2])    # [3, 5, 7]，步进分别为:0,2,4，因此能显示3个数


# 下面2个等价
class Role:
    name = 'Yuri'

Role = type('Role', (object,), dict(name='Yuri'))

# Ellipsis相当于...
