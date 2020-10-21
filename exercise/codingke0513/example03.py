"""
继承  ---> 从已经有的类创建新类的过程，提供继承信息的叫父类（超类，基类）
得到继承信息的叫子类（派生类）。继承是实现代码复用的方式。
继承关系也称为is-a关系。 a student is a person. a teacher is a person
"""


class Person:
    """人"""

    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
    def eat(self):
        print(f'{self.name}正在吃饭')

    def sleep(self):
        print(f'{self.name}正在睡觉')

    def walk(self):
        print(f'{self.name}正在行走')


class Artist:

    def play_piano(self):
        print(f'{self.name}正在弹钢琴')

    def play_violin(self):
        print(f'{self.name}正在拉小提琴')


class Monk:

    def chant(self):
        print(f'{self.name}正在念经')

    def knock_the_bell(self):
        print(f'{self.name}正在念经')

# Python中允许多重继承（一个类可以有多个父类）
# 但是实际开发时应该尽可能避免使用多重继承，因为可能会让代码变得混乱
class Student(Person, Artist):
    """学生类"""

    def __init__(self, stuid, name, nationality):
        self.id = stuid
        super().__init__(name, nationality)

    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}')


class Teacher(Person, Monk):
    """老师类"""

    def __init__(self, title, name, nationality):
        self.title = title
        super().__init__(name, nationality)

    def teach(self, course_name):
        print(f'{self.name}{self.title}正在讲授{course_name}')


def main():
    student = Student(1001, '赵白石', '湖南长沙')
    student.eat()
    student.study('官场职业技能')
    teacher = Teacher('王世均', '书童', '湖南长沙')
    teacher.sleep()
    teacher.teach('经商之路')
    student.play_piano()
    teacher.knock_the_bell()
    # MRO - Method Resolution Order 方法解析顺序
    print(Student.mro())

    # student.fly()
    print(isinstance(student, Person))
    print(isinstance(student, Student))

if __name__ == '__main__':
    main()
