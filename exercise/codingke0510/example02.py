"""
使用for-in循环遍历集合中的元素
用in运算判断元素在不在集合中
"""

set1 = {num for num in range(1, 20) if num % 3 == 0 or num % 5 ==0}
print(6 in set1)    # True
print(7 in set1)    # False
print(8 not in set1)    # True
print(9 not in set1)    # False
for value in set1:
    print(value, end=' ')




