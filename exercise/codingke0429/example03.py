"""
写一个生成指定长度的验证码的函数
"""
import random


def generate_code(length=5):
    """生成长度为length的验证码，验证码由数字和英文字母构成"""
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    selected_chars = random.choices(all_chars, k=length)
    return ''.join(selected_chars)


for _ in range(10):
    print(generate_code(length=7))
