num1 = int(input('请输入一个数字：'))
num2 = int(input('请再次输入一个数字：'))
x = 0
# if num1 > num2:
#     x = num1
# else:
#     x = num2

x = num1 if num1 > num2 else num2   # 三元表达式
print('两个数中最大的一个值',x)
