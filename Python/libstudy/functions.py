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

# print(b)

