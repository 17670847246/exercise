import MySQLdb

no = int(input('请输入你要删除的编号'))

conn = MySQLdb.connect(host='112.124.20.195', port=3306,
                       user='baishi', password='baishi.123',
                       database='hrs', charset='utf8',
)
try:
    with conn.cursor() as cursor:
        result = cursor.execute(
            'delete from tb_emp where eno=%s', (no, )
        )

        conn.commit()

except MySQLdb.MySQLError as err:
    print(err)
    cursor.close()
finally:
    conn.close()



