import random

'''
双色球随机选号
红色球：1-33 ---> 选出6个
蓝色球：1-16 ---> 选出1个
'''
# n = int(input('机选几注：'))
# for _ in range(n):
#     # 列表生成式语法
#     red_balls = [num for num in range(1, 34)]
#     # for num in range(1, 34):
#     #     red_balls.append(num)
#     # print(red_balls)
#     # 使用random模块的sample函数做无放回随机抽样
#     # 第一个参数是抽样的总体， 第二个参数表示抽样的数量
#     selected_balls = random.sample(red_balls, 6)
#     # 对红色球排序（从小到大）
#     selected_balls.sort()
#     # 通过random模块的randint函数产生1-16的随机数表示蓝色球
#     blue_ball = random.randint(1, 16)
#     # 将蓝色球加入到列表中
#     selected_balls.append(blue_ball)
#     for ball in selected_balls:
#         print('%02d '% ball, end='')
#     print()

n = int(input('机选几注：'))
for _ in range(n):
    red_balls = [num for num in range(1, 31)]

    selected_balls = random.sample(red_balls, 6)
    selected_balls.sort()
    blue_balls = random.randint(1, 16)
    selected_balls.append(blue_balls)

    for ball in selected_balls:
        print('%02d '% ball, end='')
    print()



