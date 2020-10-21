"""
装饰器 - 用一个函数去装饰另一个函数为其提供额外的功能

Python中函数可以嵌套的定义（一个函数里面还可以再定义函数）
"""
import random
import time


# 装饰器函数的参数就是被装饰的函数
# 结构
# def record_time(func):
#     # 带装饰功能的函数（除了执行被装饰的函数外，还要执行额外的代码）
#     def wrapper(*args, **kwargs):
#         # start = time.time()
#         result = func(*args, **kwargs)
#         # end = time.time()
#         # print(f'执行时间：{end-start: .3f}秒')
#         return result
#     # 返回一个带装饰功能的函数
#     return wrapper
#
# # download = record_time(download)
# @record_time
# def download(filename):
#     """下载"""
#     print(f'正在下载{filename}')
#     time.sleep(random.random() * 6)
#     print(f'{filename}下载完成')
#
# # upload = record_time(upload) ---> wrapper
# @record_time
# def upload(filename):
#     """上传"""
#     print(f'开始上传{filename}')
#     time.sleep(random.random() * 8)
#     print(f'{filename}下载完成')
#
#
# # download = record_time(download)
# # upload = record_time(upload)
# print(download.__name__, upload.__name__)
# download('Python从入门到住院.pdf')
# upload('数据库从删库到跑路.pdf')


def test(num):  # ---> test(text)

    def nnum(chu):  # ---> nnum(num)
        start = time.time()
        result = num(chu)   # ---> text(num)
        end = time.time()
        print(end - start)
        return result
    return nnum

@test
def text(num):
    z = int(input('请输入一个数'))
    return z + num


print(text(7))
