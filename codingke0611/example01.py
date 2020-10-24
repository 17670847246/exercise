"""
作用域： local ---> Embedded ---> global ---> Built-in
        局部          嵌套          全局          内置
local / global
"""

a = 100

def foo():

    def bar():
        global a
        a = 300
        print(a)
    bar()
    print(a)

foo()
print(a)

