"""
类的初始方法

把对象造出来通过给对象发消息达到解决问题的目标 ---> 面向对象程序设计
"""
import math


class Circle:
    """圆类"""
    def __init__(self, radius):
        self.radius = radius

    def calc_perimeter(self):
        """求周长"""
        return self.radius * math.pi * 2

    def calc_area(self):
        """求面积"""
        return math.pi * self.radius ** 2

# 1. 定义类（数据抽象和行为抽象）
class Rectangle:
    """矩形类"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calc_perimeter(self):
        """计算周长"""
        return (self.width + self.height) * 2

    def calc_area(self):
        """计算面积"""
        return self.height * self.width

def main():
    # 2. 创建对象（构造器语法）
    r1 = Rectangle(77,22)
    r2 = Rectangle(height=88, width=77)

    # 3. 向对象发消息（访问成员运算符）
    print(r1.calc_perimeter())
    print(r2.calc_area())

    C = Circle(33)
    print(f'{C.calc_perimeter():.3f}')
    print(f'{C.calc_area():.3f}')


if __name__ == '__main__':
    main()