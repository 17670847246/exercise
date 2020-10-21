# 定义函数
import random


# 给函数的参数赋默认值（带默认值的参数）
def roll_dice(num=2):
    """摇num颗骰子返回总的点数"""
    total = 0
    for _ in range(num):
        face = random.randint(1, 6)
        total += face
    return total


# 调用函数


for _ in range(5):
    # 调用函数时如果没有指定num参数的值，那么num会默认值
    print(roll_dice())
