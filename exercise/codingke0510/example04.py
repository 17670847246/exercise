"""
集合是可变类型，可以通过集合的方法来添加删除元素
集合底层使用哈希存储，所以元素在内存中不是连续防止的二十离散存储的
集合的方法
- 添加元素： add / update
- 删除元素：discard / remove / pop / clear
- 判断两个集合有无公共元素：isdisjoint
"""
# 创建一个空集合
set1 = set()
print(type(set1))
set1.add(31)
set1.add(23)
print(set1)
set1.update({22, 1, 10, 100, 1000})
print((set1))
# 通过discard方法删除指定元素
set1.discard(1000)
set1.discard(88)
print(set1)
# 通过remove方法删除指定元素，建议先做成员运算再删除
# 否则元素如果不在集合中就会引发KeyError异常
if 98 in set1:
    set1.remove(98)
# pop方法可以从集合中随机删除一个元素并返回该元素
print(set1.pop())
print(set1)

# clear方法可以清空整个集合
set1.clear()
print(set1)
lios = []


