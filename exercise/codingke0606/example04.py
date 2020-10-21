import time

class Dept:

    def __init__(self, no, name, location):
        self.no = no
        self.name = name
        self.location = location

    def __str__(self):
        return self.location


import MySQLdb # mysqlclient
from MySQLdb.cursors import DictCursor

conn = MySQLdb.connect(host='112.124.20.195', port=3306,
                       user='baishi', password='baishi.123',
                       database='hrs', charset='utf8',
                       cursorclass=DictCursor)
try:
    with conn.cursor() as cursor:
        result = cursor.execute('select dno as no, dname as name, dloc as location from tb_dept')

        depts = [Dept(**row) for row in cursor.fetchall()]
        for dept in depts:
            print(f'编号： {dept.no}')
            print(f'名称: {dept.name}')
            print(f'所在地：{dept.location}')
            print('-' * 20)
        # print(cursor.fetchmany(3))

        # print(type(depts))
        # for row in depts:
        #     print(row)

        # result1 = cursor.fetchone()
        # while result1:
        #     print(result1['location'])
        #     result1 = cursor.fetchone()
        # for resu in result1:
        #     print(resu)
except MySQLdb.MySQLError as err:
    print(err)
finally:
    conn.close()








