'''
约瑟夫环问题
《幸运的女人》
'''

# persons = [True] * 30
# index, counter, num = 0, 0, 0
#
#
# while counter < 15:
#     if persons[index]:
#         num += 1
#         if num == 9:
#             persons[index] = False
#             counter += 1
#             num = 0
#     index += 1
#     index %= 30
#
#
#
# for person in persons:
#     if person:
#         print('女', end='')
#     else:
#         print('男', end='')

# persons = [True] * 30
# index, count, num = 0, 0, 0
#
# while count < 15:
#     if persons[index]:
#         num += 1
#         if num % 9 == 0:
#             persons[index] = False
#             num = 0
#             count += 1
#     index += 1
#     index %= 30
#
# print(persons)
#
# for i in persons:
#     if i:
#         print('男',end='')
#     else:
#         print('女',end='')

# 用一个有30个布尔值为True的列表表示船上的30个人
# 如果这个人被扔到了海里，就把对应的布尔值从True修改为False
persons = [True]*30
# 定义三个变量分别表示
# index - 操作列表的下标 （索引）
# count - 计数器（有多少个人被扔到海里）
# num - 报数的数字（从1报到9）
index, count, num = 0,0,0
# 只要还没扔掉15个人循环就继续下去
while count < 15:
    # 活着的人（在船上的人）可以报数
    if persons[index]:
        num += 1
        # 如果数字报的是9就扔到海里
        if num % 9 == 0:
            persons[index] = False
            num = 0
            count += 1
    index += 1
    index %= len(persons)


for person in persons:
    print('男' if person else '女', end='')
























