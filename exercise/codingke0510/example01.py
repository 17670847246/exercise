"""
集合 - 把一定范围的，确定的，可以区别的事物当作一个整体来看待
1. 无序性 - 元素之间没有所谓的顺序，也不能使用索引的方式获取元素
2. 互异性 - 任何两个元素都可以互相区分，每个元素只能出现一次
3. 确定性 - 给定一个集合和一个元素，该元素或者属于或者不属于该集合
"""
# 创建集合的第一种方式 - 字面量语法
set1 = {1, 2, 3, 4, 3, 2, 1, 11, 33}
print(set1)
print(len(set1))

# 创建集合的第二种方式 - set函数（构造器）
set2 = set('hello')
print(set2)
print(len(set2))

# 创建集合的第三种方法 - 集合生成式
set3 = {x for x in range(10)}
print(set3)
print(len(set3))

# set4 = {'apple', 'zao', 'dog', 'banana', 'apple', 'dog'}
# print(set4)
# print(len(set4))