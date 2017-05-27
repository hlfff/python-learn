# -*- coding: utf-8 -*-
from functools import reduce
# 在python中，函数名也是可变的，比如绝对值函数abs   如果a = abs，那么a就具有abs的方法

# map和reduce
def a(x):
    return x * x
# map  第一个参数是方法名，后面的每个元素都会作用于前面的参数
r = map(a, [1, 2, 3, 4, 5, 6, 7, 8, 9])

# reduce 和map类似，但是每次传入两个参数， 例如


def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))

# filter 跟map类似，但是他是根据返回值是ture或者false来决定元素是否保留
def is_odd(n):
    return n % 2 == 1

list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
# 结果: [1, 5, 9, 15]
