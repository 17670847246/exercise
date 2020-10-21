"""
遍历字典中的键值对
"""
person1 = {
    'name': '王大锤', 'e_contact': '王二锤', 'sex': True,
    'age': 55, 'height': 175, 'weight': 60,
    'office': '科华北路62号', 'home': '中国仁路8号',
    'tel': '13117645448', 'e_tel': '15648412354'
}

# for elem in person1:
#     print(elem)
#
for key in person1.keys():
    print(key)
    # print(key, person1[key]
for value in person1.values():
    print(value)

for key, value in person1.items():
    print(key, value, sep=': ')



