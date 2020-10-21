"""
打开文件 ---> open(文件路径，操作模式，字符编码）---> file object
---> read(size) ---> str/bytes / write(str/bytes)
try - except - finally --> 把可能会出状况的代码保护起来执行
如果出现了异常状况可以通过except进行异常捕获并作出相应的处理，保证程序的健壮性
with上下文语法 ---> with open(...) as file ---> 离开with上下文的时候会自动执行file.close()

gb18030 -> 收录了少数名族

utf-8
Unicode
ansi -> gbk
"""
import sys
print(sys.getdefaultencoding())


import time


class MyExcption(Exception):
    """自定义异常类型"""
    pass

def foo():
    # 代码
    # 如果函数执行的后续条件不满足，我们可以引发（抛出）自定义的异常对象
    raise MyExcption()
    # 代码

def main():
    try:
        foo()
    except MyExcption:
        print('出错')
    try:
        # with 对象 as 别名: ---> 上下文语法
        with open('filES/zxs.txt', mode='r', encoding='utf-8') as file:  # gbk -> 国标库（扩展码）
            data = file.read(32)
            while data:
                print(data, end='')
                time.sleep(2)
                data = file.read(32)
    except FileNotFoundError:
        print('文件不存在，请指定正确的文件路径')
    except LookupError:
        print('指定了无效的编码！！')
    except UnicodeDecodeError:
        print('指定的编码无法解码文件内容')


if __name__ == '__main__':
    main()
