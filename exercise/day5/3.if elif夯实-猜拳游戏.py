import random
# 剪刀 0  石头 1 布 2

#电脑
#我们输入
#三种结果   平输赢
#我们 0 电脑 2   1 0     2 1 我们赢

#0 0 11 22 平局

#否则就是输

player = int(input('请输入 剪刀（0） 石头（1） 布（2）'))
print('你出', player)
computer = random.randint(0,2)
print('电脑出', computer)

if (player == 1 and computer == 0) or (player == 2 and computer == 1) or (player == 0 and computer == 2):
    print('玩家赢')
elif (player == computer):
    print('平局')
else:
    print('你输了')











