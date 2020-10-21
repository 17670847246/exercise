"""
一个小孩爬楼梯，每次可以爬1个，2个或3个台阶
编程求出这个小孩爬完10个台阶的楼梯一共有多少种走法。
"""
from functools import lru_cache


# f(n) = f(n-1) + f(n - 2) + f(n - 3)
# 1 - 1
# 2 - 2
# 3 - 4 (111 / 12 / 21 / 33)
# 4 - 7 (1111 / 112 / 121 / 13 / 211 / 22 / 31)

@lru_cache()
def go_upstairs(num):
    if num == 0:
        return 1
    if num < 0:
        return 0
    return go_upstairs(num - 1) + go_upstairs(num - 2) + go_upstairs(num - 3)
for n in range(1, 101):
    print(f'{n}:{go_upstairs(n)}')