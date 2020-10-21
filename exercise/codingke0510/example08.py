"""
字典的方法
- 删除元素：pop / popitem / clear
- 更新元素：update
- del
"""
person1 = {
    'name': '王大锤', 'e_contact': '王二锤', 'sex': True,
    'age': 55, 'height': 175, 'weight': 60,
    'office': '科华北路62号', 'home': '中国仁路8号',
    'tel': '13117645448', 'e_tel': '15648412354'
}
print(person1.pop('e_contact'))
print(person1.popitem())
print(person1.popitem())
del person1['name']
print(person1)
person1.update({'salary': 1200, 'has_car': True})
print(person1)
person1.clear()
print(person1)

nums = [1, 2, 3, 4, 5, 3, 2, 1]
nums = set(nums)
nums = list(nums)
print(nums)