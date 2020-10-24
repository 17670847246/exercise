"""
生成器：生成器是迭代器的语法升级版本
"""

def fib(num):
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a+b
        yield a

fib_iter = fib(20)
print(fib_iter, type(fib_iter))
print(next(fib_iter))
print(next(fib_iter))
print(next(fib_iter))
for value in fib_iter:
    print(value)
print('-' * 40)
for value in fib_iter:
    print(value)