import random

def roll_dice(num):
    nu = 0
    for _ in range(1, num + 1):
        a = random.randint(1, 6)
        nu += a
    return nu

cc = int(input('请输入你要的色子的数量: '))
print(roll_dice(cc))


def calc_avg(items):
    pass



