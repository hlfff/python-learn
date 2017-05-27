# -*- coding: utf-8 -*-
from collections import namedtuple
from collections import deque
b = namedtuple('b', ['x', 'y'])
a = b(1, 2)
print(a.x)
print(a.y)

c = deque([1, 2, 3])
c.append('c')
c.appendleft('d')
print(c)
