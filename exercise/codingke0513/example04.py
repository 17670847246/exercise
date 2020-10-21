"""
多态 - 向对象发出相同的消息，不同类型的对象会对消息产生不同的响应，这就是多态

实现多态最为关键的一步就是方法重写，不同的子类对相同的方法给出不同的实现版本。

父类有一个方法（可以有实现也可以没有实现），子类在继承父类的过程中
重新实现了这个方法，方法重写（override)

抽象类不能实例化（创建对象），它存在的价值是让其他类来继承它。
一个类如果有抽象方法，这个类必须被生命为抽象类，但是一个抽象类却可以没有抽象方法

工资结算系统：三种类型的员工，部门经理，销售员，程序员
部门经理固定月薪15000
程序员计时，每小时200
销售员底薪1800，销售额提成5%
"""
from abc import abstractmethod, ABCMeta


# 抽象类（不能创建对象的类，专门用于继承）
class Employee(metaclass=ABCMeta):
    """员工"""

    def __init__(self, name):
        self.name = name

    # 抽象方法（留给子类去实现的方法）
    @abstractmethod
    def get_salary(self):
        pass


class Managers(Employee):
    """经理"""

    # 工资
    def get_salary(self):
        return 15000


class Programmer(Employee):
    """程序员"""

    def __init__(self, name):
        self.hour = 0
        super().__init__(name)
    # 工资
    def get_salary(self):
        return 200 * self.hour


class Salesman(Employee):
    """销售员"""

    def __init__(self, name):
        self.sales = 0
        super().__init__(name)
    # 工资
    def get_salary(self):
        return 1800 + self.sales * 0.05



def main():

    emps = [
        Managers('曹操'), Programmer('小乔'), Programmer('郭嘉'),
        Salesman('典韦'), Salesman('大桥'), Programmer('张辽')
    ]
    for emp in emps:
        if type(emp) == Programmer:
            emp.hour = int(input(f'请输入{emp.name}本月的工作时间'))
        # isinstance 判断是不是子集
        elif type(emp) == Salesman:
            emp.sales = int(input(f'请输入{emp.name}本月的销售额'))
        print(f'{emp.name}本月的工资为：{emp.get_salary():.2f}元')


if __name__ == '__main__':
    main()
