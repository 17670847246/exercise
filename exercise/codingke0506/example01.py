"""
每个Python文件就是一个模块（modele），模块可以管理函数
同名的函数可以放到不同的模块下
每个文件夹（有一个__init__.py文件）就一个包（package），包可以管理模块
同名的模块可以放到不同的包下
使用模块和包可以解决Python程序中命名冲突的问题
相关的关键字：from / import / as
"""

# from 模块 import 函数
# from 模块 import *
from homework.homework09 import is_prime
from homework.homework10 import is_palindrome
# import 模块
# 模块名.函数名（参数）
# import homework09 as  h09
# import homework10 as  h10
def is_palindromic_prime(num):
    return is_prime(num) and is_palindrome(num)



print(is_palindromic_prime(123321))
print(is_palindromic_prime(22))
print(is_palindromic_prime(11))