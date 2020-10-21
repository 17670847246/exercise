"""
为什么需要字典类型？想一想如果要用一个变量保存一个人的信息应该怎么做
列表好用吗？
字典 - 用键值对的方式组织数据， 通过键可以获取到对应的值，实现有的放矢的取值
"""

#创建字典的方式一：字面量语法
person1 = {}
print(type(person1))


person1 = {
    'name': '王大锤', 'e_contact': '王二锤', 'sex': True,
    'age': 55, 'height': 175, 'weight': 60,
    'office': '科华北路62号', 'home': '中国仁路8号',
    'tel': '13117645448', 'e_tel': '15648412354'
}
# 创建字典的方式二：dict函数（构造器）
person2 = dict(name='王大锤', age=33, weight=60, home='机构奥杰')
print(person2)

# zip函数 ---> 拉链 / 压缩
items1 = dict(zip('ABCDE', '12345'))
items2 = dict(zip('12345', 'ABCDE'))
items3 = dict(zip('ABCDE',range(1, 8)))
print(items1)
print(items2)
print(items3)

# 创建字典的方式三：生成式
items3 = {x: x ** 3 for x in range(1, 6)}
print(items3)