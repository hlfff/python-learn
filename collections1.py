# -*- coding: utf-8 -*-
from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict
from collections import Counter
b = namedtuple('b', ['x', 'y'])
a = b(1, 2)
print(a.x)
print(a.y)

c = deque([1, 2, 3])
c.append('c')
c.appendleft('d')
print(c)

# 给dict添加一个默认的返回值defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'

# dict无序，如果想让他有序可以使用orderDict 顺序是按照插入顺序的,当长度超出限制，准从先进先出的原则
d = dict([('a', 1), ('b', 2), ('c', 3)])
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# Counter是一个简单的计数器，例如，统计字符出现的个数
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1

print(c)
