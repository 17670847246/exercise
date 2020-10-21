import MySQLdb
from MySQLdb.cursors import DictCursor

no = int(input('请输入编号'))
name = input('请输入姓名')
job = input('请输入职业')
mgr = int(input('请输入主管编号'))
sal = int(input('请输入月薪'))
comm = int(input('请输入补贴'))
dno = int(input('请输入部门编号'))

conn = MySQLdb.connect(host='112.124.20.195', port=3306,
                       user='baishi', password='baishi.123',
                       database='hrs', charset='utf8'
                        )


try:
    with conn.cursor() as cursor:
        result = cursor.execute(
            'insert into tb_emp values(%s, %s, %s, %s, %s, %s, %s)',(no, name, job, mgr, sal, comm, dno)
        )
        if result == 1:
            print('1')
        conn.commit()
except MySQLdb.MySQLError as err:
    print(err)
    cursor.close()
finally:
    conn.close()







