"""
属性装饰器
静态方法和类方法
"""

import math


class Triangle:
    """三角形"""

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # 类方法 - 不是发给对象的消息，而是发给类的消息
    # @classmethod
    # 静态方法 - 也不是发给对象的消息，而是发给类的消息，少了一个保存类相关信息的变量     @staticmethod
    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and a + c > b

    @property
    def perimeter(self):
        """周长"""
        return self.a + self.b + self.c

    @property
    def area(self):
        """面级"""
        p = self.perimeter / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5


class Circle:

    def __init__(self, radius):
        self.radius = radius

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

    @property
    def area(self):
        return math.pi * self.radius ** 2


def main():
    # circle = Circle(5.2)
    # # 计算属性
    # print(f'圆的周长：{circle.perimeter}')
    # print(f'圆的面积：{circle.area}')
    if Triangle.is_valid(3, 4, 5):
        t1 = Triangle(3, 4, 5)
        print(f'周长{t1.perimeter}')
        print(f'面级{t1.area}')
    else:
        print('无效的边长，你输入的不是一个三角形')


if __name__ == '__main__':
    main()
