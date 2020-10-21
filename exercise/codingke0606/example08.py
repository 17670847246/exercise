import MySQLdb
from MySQLdb.cursors import DictCursor


class Dept:

    def __init__(self, eno, ename, job, mgr, sal, comm, dno):
        self.no = eno
        self.name = ename
        self.job = job
        self.mgr = mgr
        self.sal = sal
        self.comm = comm
        self.dno = dno

    def __str__(self):
        return self.name


conn = MySQLdb.connect(host='112.124.20.195', port=3306,
                       user='baishi', password='baishi.123',
                       database='hrs', charset='utf8',
                       cursorclass=DictCursor
                       )

try:
    with conn.cursor() as cursor:
        result = cursor.execute(
            'select * from tb_emp'
        )
        des = cursor.fetchall()
        des = [Dept(**de) for de in des]
        for de in des:
            print(f'{de.no}')
            print(f'{de.name}')
            print(f'{de.job}')
            print(f'{de.mgr}')
            print(f'{de.sal}')
            print(f'{de.comm}')
            print(f'{de.dno}')
            print('-' * 20)
except MySQLdb.MySQLError as err:
    print(err)
    cursor.close()
finally:
    conn.close()




