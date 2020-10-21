"""
设计一个多个数求和的函数
"""
# 参数名前带*的参数成为可变参数（调用函数时可以传入0个或任意多个参数）
# 传入的参数会组装成一个元组型的变量，type(nums) ---> tuple
def add(*nums):
    total = 0
    for num in nums:
        total += num

    return total


print(add(1, 3, 5))

