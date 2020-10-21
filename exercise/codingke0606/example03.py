import MySQLdb # mysqlclient


no = int(input('请输入部门编号'))
name = input('请输入部门名称')
location = input('请输入部门所在地')


# 1. 创建数据库连接
conn = MySQLdb.connect(host='112.124.20.195', port=3306,
                       user='baishi', password='baishi.123',
                       database='hrs', charset='utf8'
                       )
try:
    # 2. 获取游标对象(通过游标对象可以向MySQL数据库发出SQL语句)
    with conn.cursor() as cursor:
        # 3.通过游标执行SQL语句并获取结果(多少行受影响)
        result = cursor.execute(
            'update tb_dept set dname=%s, dloc=%s where dno=%s', (name, location, no)
        )
        if result == 1:
            print('1')
        # 4. 提交上面的操作（数据真正写入数据库反映到物理储存中）
        conn.commit()
except MySQLdb.MySQLError as err:
    print(err)
    # 4. 回滚 - 撤销之前的操作（之前的操作都不会写入数据库）
    conn.rollback()
finally:
    # 5.释放数据库连接(一定放在finally中，保证正常和异常情况连接都能被释放)
    conn.close()








