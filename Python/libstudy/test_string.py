# encoding: utf-8
"""
字符串
@author Yuriseus
@create 2016-6-29 14:48
"""

import string
s = """abc
hehe"""
s += 'd'
print(s)
print(string.punctuation)

s = 'hello, {0.name}'
class A():
    def __init__(self):
        self.name = 'world'
s = s.format(A())

s = "hello: {roles[0]}"
s = s.format(roles=['Yuri'])    # hello: Yuri
print(s)
