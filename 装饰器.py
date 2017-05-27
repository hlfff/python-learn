# -*- coding: utf-8 -*-
# 装饰器  类似于java的装饰者模式，通过在函数上面添加@log(参数)增加方法的行为
import functools
# 标准写法，不带参数
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# 带参数
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
