"""
魔法方法：
__str__ / __repr__ / __lt__ less than <
"""


class Student:
    """学生类"""

    def __init__(self, stuid, stuname):
        self.id = stuid
        self.name = stuname

    # string
    def __str__(self):
        return f'{self.id}:{self.name}'

    # representation
    def __repr__(self):
        return f'{self.id}:{self.name}'

    # less than
    def __lt__(self, other):
        return self.name < other.name

    # great than or equal than
    def __ge__(self, other):
        return self.id >= self.id
    def study(self, ccourse_name):
        """学习
        :param course_name: 学习的课程名称
        """
        print(f'{self.name}正在学习{ccourse_name}')

    def eat(self):
        """吃饭"""
        print(f'{self.name}正在吃饭')

    def sleep(self):
        """睡觉"""
        print(f'{self.name}正在睡觉')


def main():
    """主函数"""
    stu1 = Student(1001, '赵白石')
    stu2 = Student(1002, '王世均')
    print(stu1)
    print(stu2)
    studens = [stu1, stu2]
    print(studens)
    stu1.eat()
    stu1.study('官场如何锤炼')
    print(ord('赵'),ord('王'))
    print(stu1 < stu2)
    stu3 = Student(1003, '周')
    print(stu3 > stu2 > stu1)
    # for code in range(0x4e00, 0x9fa6):
    #     print(chr(code), end=' ')

if __name__ == '__main__':
    main()
