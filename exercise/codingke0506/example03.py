"""
高阶函数 - 把函数作为函数的参数或返回值
在Python语言中，函数是一等公民（一等函数）
1，函数可以赋值给变量
2，函数可以作为函数的参数
3，函数可以作为函数的返回值

通过高阶函数的用法，我们可以写出通用性和灵活性更强的代码
"""


def calc(*nums, init_value, fn):
    result = init_value
    for num in nums:
        result = fn(result, num)
    return result


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


print(calc(155, 22, init_value=0, fn=add))
print(calc(156, 14, init_value=0, fn=sub))
print(calc(165, 789, init_value=0, fn=add))
print(calc(15, 65, init_value=1, fn=mul))
