import math
# def perimeter(radius):
#     return
#
# def area(radius):
#     return math.pi * radius ** 2

def calc_circle(radius):
    return 2 * math.pi * radius, math.pi * radius ** 2

r = float(input('请输入圆的半径'))
# 元组的解包操作
peri, area = calc_circle(r)
print(f'圆的周长：{peri:.2f}')
print(area)
# result = calc_circle(4)
# print(type(result))
# print(result)


