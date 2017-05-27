# -*- coding: utf-8 -*
from types import MethodType

class Student(object):
    # 类似下面的方法是python类里面的特殊方法,类似方法有很多  而init这个方法就相当于java的构造方法
    def __init__(self):
        pass
# 括号里面是基类

a = Student()
# 给类添加实例
a.name = 'han'

# 对于参数的封装类似于java的get  set方法.
# 在python中可以动态的给类添加属性或者方法,但是只是给实例化的a添加了此方法,改变实例化的name没有效果
def set_age():
    pass
a.set_age = MethodType(set_age, a)

# 但是当我们想给类添加属性或者方法是,加上限制,使用__slots__方法

# __slots__ = ('name', 'age')


# @property  可以用来定义只读属性   调用时赋值就代表set方法,不赋值相当于get

class Student1(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

# __iter__方法,将类可以被用于被迭代,但是不能类似list取指定index的值,如果想如此取值使用__getitem__方法
#     def __getitem__(self, n):
#         a, b = 1, 1
#         for x in range(n):
#             a, b = b, a + b
#         return a
