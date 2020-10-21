# if 语句里边嵌套 if 语句
ticket = input('是否买票Y/N')
if ticket == 'Y':
    print('请通过')
    safe = input('是否通过安检Y/N')
    if safe == 'Y':
        print('请在候车室等待')
    else:
        print('请打开你的行李')
else:
    print('滚')




