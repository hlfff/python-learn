# -*- coding: utf-8 -*-
import sqlite3

a = sqlite3.connect('han.db')
cursor = a.cursor()
def exist():
    try:
        cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
        cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
    except:
        print('已经存在')
        return False
    cursor.rowcount
    cursor.close()
    a.commit()
    a.close()


print(cursor)
conn = sqlite3.connect('han.db')
cursor1 = conn.cursor()
cursor1.execute('insert into user (id, name) values (\'2\', \'feifei\')')
cursor1.execute('select * from user where id =?', ('2',))
values = cursor1.fetchall()
print(values)
cursor1.close()
conn.close()
