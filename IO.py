# -*- coding: utf-8 -*-
from io import StringIO
# 该方法可以不使用close方法，第二个参数，r代表read，w是write  等等  第三个编码格式
with open('filepath', 'r') as f:
    print(f.read())

# 从内存中读取
a = StringIO()
a.write('aaa')
a.getvalue()


# byte跟stringIO一样，不过是写入二进制
