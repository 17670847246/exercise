# break: 用来结束整个循环
# continue: 用来结束本轮循环， 开启下一轮循环

# i = 0
# while i < 5:
#     print(i)
#     i += 1
#     if i == 3:
#         break


# while True:
#     answer = input('咱们出对象呗')
#     if answer == '好':
#         break


# continue 结束当前这一次循环 重新判断条件 开启下一次循环

i = 0
sum = 0 #存和
while i <= 100:
    if i % 2 == 0:
        i += 1
        continue    #如果是偶数  那么退出这一次 继续下一次的循环
    sum += i
    i += 1

print(sum)

