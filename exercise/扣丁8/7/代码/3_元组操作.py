

# 元组和列表相似，但元组属于不可变序列，所以无组
# 不能修改元素的值


# 1.定义
t1 = 1,2,3
t2 = (1,2,3)
t3 = (1,)   # 只有一个元素的元组，逗号不能省略
t4 = (1)
print(t1)
print(t2)
print(t3)
print(t4)

# 下标用法和列表相同
# 元素不能修改
print(t1[2], t2[1])
# 遍历
# for value in t1:
#     print(value)

# for i in range(len(t1)):
#     print(t1[i])

# 通用操作
# res = (1,2,3) + t1
# res = (0,1)*10
# 元素个数
# res = len(t1)

# 切片
t1 = (10, 20, 30, 20, 40, 50)
print(t1[:4])   #(10, 20, 30, 40)

# 统计函数
print(sum(t1), max(t1))

#成员判断， in，not in
print(20 in t1)

# 查找
# rq = t1.index(20)
# print(t1.index(20, rq + 1))
# print(t1.count(20))

# 序列解包
# 解包就是把元组的元素赋值给变量
# a, b = (3, 4)
# 3赋值给a，5赋值给b， 其余元素赋值给_
# a, *_, b = (3,4,5,23,21)
# print(a,b)
# print(type(_))
#
# a,b,*_ = 3,4,523,23
# print(a,b,_)
#
# t1 = 1,2,3,4
# *_,a,b = t1
# print(_,a,b)
# print(t1)
#
# a, b = 3, 4
# a, b = b, a
# print(a,b)
#

list1 = []
for i in range(30):
    list1.append(i)
print(list1)

list2 = []
i = 1
while i <= 450:
    if i % 9 == 0:
        for ls in list:
            list2.append(ls)
            list1.remove(ls)
print(list2)






