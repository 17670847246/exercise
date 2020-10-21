
list = [10, 20, 30, 40, 30, 50, 60]
# 列表的增删元素

# append在末尾追加元素
# list.append(31)
# list.append([1, 3])
# print(list)



# extend 在列表末尾追加多个元素，参数可以是列表
# list.extend([82, 67])
# list.extend(100)    # error 'int' object is not iterable

# insert 在任意位置插入元素，原来的元素会往后移动
# list.insert(0,100)

# 删除元素
# pop(i) 删除指定下标的元素
# res = list.pop(0) # 删除下标为0的元素
# res = list.pop() # 删除末尾元素

# remove 按元素的值删除, 从左向右删除第一个等于指定值的元素
# list.remove(50)

# clear 清空列表
# list.clear()

# 切片删除, 可以删除任何连续的元素
# list[:2] = []

# 查找
# index 从左向右查找第一个等于指定值的元素的下标
# list.index(x,start=0, end=len(list))

print(list)
res = list.index(30)

# 查找所有值等30的元素下标
# result = []
# for i in range(len(list)):
#     if list[i] == 30:
#         result.append(i)

# result = []
# for i in range(len(list)):
#     if list[i] == 20:
#         result.append(i)
# print(result)

# res = list.index(30)
# print(res)
# print(list.index(30, res+1))

# count 找出列表中有多少个值等于x的元素
res = list.count(30)
# 从list中删除值等30的元素全部删除
# for i in list:
#     if i == 30:
#         list.remove(i)

# 不要在遍历中直接删除元素
# for i in range(len(list)):
#     if i == 30:
#         list.remove(list[i])
# while 40 in list:
#     list.remove(40)
# print(list)

#列表翻转
# print(list)
# list.reverse()
# print(list)

# 列表排序
# print(list)
# list.sort() # 从小到大排序
# print(list)
# reverse默认等于False 从小到大排序
# reverse= Ture从大到小排序
# list.sort(reverse=True)
# print(list)

# 二维列表
list2 = [[1,22,33], [44,55,66]]

# 元素访问
# print(list2[0])
# 取元素要用到两个[]
# print(list2[1][1])
for elem in list2:
    for value in elem:
        print(value)





print(res)






