"""
生成式和生成器的区别
"""
# 生成式一开始就将元素放到了列表中，比较耗费空间
items = [num ** 2 for num in range(1, 10)]
print(items)
# 生成器是每次需要元素的时候通过计算获得该元素,几乎不耗费存储空间,
# 每次取出元素时需要耗费额外的运算时间
items = (num ** 2 for num in range(1, 10))
# try:
#     while True:
#         print(next(items))
# except StopIteration:
#     pass
for value in items:
    print(value)
