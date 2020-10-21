import MySQLdb # mysqlclient


no = int(input('请输入部门编号'))
conn = MySQLdb.connect(host='112.124.20.195', port=3306,
                       user='baishi', password='baishi.123',
                       database='hrs', charset='utf8'
                       )
try:
    with conn.cursor() as cursor:
        result = cursor.execute(
            'delete from tb_dept where dno=%s', (no, )
        )
        if result == 1:
            print('1')
        conn.commit()
except MySQLdb.MySQLError as err:
    print(err)
    conn.rollback()
finally:
    conn.close()








