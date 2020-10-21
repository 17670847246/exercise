import MySQLdb

no = int(input('请输入编号'))
name = input('请输入需要更改的姓名')
job = input('请输入需要更改的职业')
mgr = int(input('请输入需要更改的主管编号'))
sal = int(input('请输入需要更改的月薪'))
comm = int(input('请输入需要更改的补贴'))
dno = int(input('请输入需要更改的部门编号'))

conn = MySQLdb.connect(host='112.124.20.195', port=3306,
                       user='baishi', password='baishi.123',
                       database='hrs', charset='utf8'
)

try:
    with conn.cursor() as cursor:
        result = cursor.execute(
            'update tb_emp set ename=%s, job=%s, mgr=%s, sal=%s, comm=%s, dno=%s where eno=%s'
            , (name, job, mgr, sal, comm, dno, no)
        )
        if result == 1:
            print('更新成功')
        conn.commit()

except MySQLdb.MySQLError as err:
    print(err)
    cursor.close()
finally:
    conn.close()






