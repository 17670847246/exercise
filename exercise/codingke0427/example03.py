import math
'''
用嵌套列表保存5个学生3门课程的成绩
'''
names = ['王大锤', '李二狗', '张三丰', '找死吹', '刘五牛']
courses = ['语文', '数学', '英语']
# 不能使用列表的重复运算来创建嵌套列表
# scores = [[0] * 3] * 5   error
# 通过列表生成式创建嵌套列表
scores = [[0] * 3 for _ in range(5)]
for i in range(len(names)):
    print('请输入%s的成绩'% names[i])
    for j in range(len(courses)):
        temp = float(input('%s：' % courses[j]))
        scores[i][j] = temp
print(scores)

# 计算每个学生的平均成绩
        
# 计算每门课程的平均成绩
