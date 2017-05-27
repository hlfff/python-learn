# -*- coding: GBK -*-
import threading
import time
def loop():
    print(threading.current_thread().name)
    for a in range(1, 5):
        print('ing', threading.current_thread().name)
        time.sleep(1)
    print('end', threading.current_thread().name)

a = threading.Thread(target=loop, name='han')
a.start()
a.join()
print(threading.current_thread().name)

local_data = threading.local()
