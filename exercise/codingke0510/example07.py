"""
字典的运算
"""

person1 = {
    'name': '王大锤', 'e_contact': '王二锤', 'sex': True,
    'age': 55, 'height': 175, 'weight': 60,
    'office': '科华北路62号', 'home': '中国仁路8号',
    'tel': '13117645448', 'e_tel': '15648412354'
}
# 索引运算 - 通过键获取对应的值
print(person1['name'])
print(person1['tel'])
print(person1['height'])
# 如果键不存在将引发KeyError错误
# print(person1['six'])
if 'six' in person1:
    print(person1['six'])
else:
    print('没有对应的值')
# get方法比[]更加安全，如果键不存在会返回None或用户指定的值
print(person1.get('six', '不存在'))

# 通过索引运算添加新的键值对或更新已有的键值对
person1['name'] = '王小美'
person1['sex'] = False
person1['signature'] = '你的男朋友是一个盖世英雄'
print(person1)

# 获取字典中键值对（元素）的数量
print(len(person1))
print(person1)



