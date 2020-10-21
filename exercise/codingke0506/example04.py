"""
Lambda函数 - 只有一行代码而且没有名字的函数（匿名函数）
Lambda函数就是把一个简单函数携程表达式的形式
处理数据：过滤(filter) ---> 映射(map) ---> 归约（reduce）
from functools inport reduce
Python中的函数的参数可以用*进行分割
*前面的参数成为位置参数，调用函数传入参数时只需要对号入座即可
*后面的参数称为命名关键字参数，调用函数传入参数时必须携程“参数名=参数值”的形式
"""
from random import sample, choices

print(sample('0123456789', 6))
print(choices('1234567', k=4))
fruits = ['banana', 'grape', 'waxberry', 'durian', 'watermelon']
fruits2 = sorted(fruits, key=len, reverse=True)
print(fruits2)

# def is_odd(num):
#     return num % 2

nums = [4, 13, 5, 153, 134, 1345, 135]
# num2 = sorted(nums)
# print(num2)
nums.sort(key=str)
print(nums)
# print(list(map(lambda x: x ** 2, filter(lambda num: num % 2, nums))))
# # 返回值 遍历 条件
# print([num ** 2 for num in nums if num % 2])


# def calc(init_value, fn, *nums):
#     result = init_value
#     for num in nums:
#         result =  fn(result, num)
#     return result
#
# add = lambda x, y: x + y
#
#
# print(calc(0, add, 1, 2))
# print(calc(3, lambda x, y: x - y, 1, 2))
# print(calc(1, lambda x, y: x * y, 1, 2))
# print(calc(1, lambda x, y: x * y, 1, 2, 42, 13))
