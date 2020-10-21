'''
求C(m,n)
如果代码中出现了想对独立且会被重复使用的功能，我们可以将这些代码写到函数中
将来想使用这些功能的使用，直接调用函数即可，不用再写重复的代码
'''
# def是定义函数的关键字（有特殊含义的单词）
# fac是函数的名字，命名规则跟变量的命名规则一致
# num是函数的参数（自变量），可以有0个或多个
def fac(num):
    result = 1
    # 在函数定义下保持缩进的代码都是函数的执行体
    # 保存运算结果的累乘变量
    # 通过1到num的循环做累乘
    for i in range(1, num + 1):
        result *= i
    # 返回累乘的结果（因变量）
    # 函数中一旦出现return语句，函数就会返回因变量，函数的执行就结束
    return result







m = int(input('m = '))
n = int(input('n = '))
# 调用函数并且赋值
mm = fac(m)
nn = fac(n)
m_n =fac(m-n)
print(mm // nn // m_n)

# k = m - n
# fm = 1
# for i in range(1, m + 1):
#     fm *= i
# fn = 1
# for i in range(1, n + 1):
#     fn *= i
# fk = 1
# for i in range(1, k + 1):
#     fk *= i
# print(fm // fn // fk)   # fm // (fn * fk)

