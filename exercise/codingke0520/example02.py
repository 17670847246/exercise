"""
创建和使用线程

进程：操作系统分配内存的基本单元，每个进程的内存空间是独立的，进程之间不共享内存
线程：操作系统分配CPU的基本单元，如果程序使用了多线程会比单线程占用更多的CPU资源
一个程序通常是一个或多个进程，一个进程可以包含一个或多个线程
可以通过Windows的任务管理器或macOS系统的活动监视器来查看进程、

图形图像处理，音视频压缩解码，科学计算 ---> 计算密集型任务 ---> 多进程
联网获取数据，文件读写 ---> I/O密集型任务 ---> 多线程 / 异步编程

Python ---> CPython ---> GIL(全局解析器锁) ---> 无法使用多核多CPU优势

"""
import random
import time
from multiprocessing import Process


def upload(filename):
    print(f'开始上传{filename}')
    time.sleep(random.randint(3, 5))
    print(f'{filename}上传完成')

def download(filename):
    print(f'开始下载{filename}')
    time.sleep(random.randint(4, 6))
    print(f'{filename}下载完成')

def main():
    start = time.time()
    t1 = Process(target=download, args=('Python从入门到精通', ))
    t1.start()
    t2 = Process(target=download, args=('深入浅出MySQL', ))
    t2.start()
    t3 = Process(target=upload, args=('Python爬虫开发', ))
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    end = time.time()
    print(f'总共耗时：{end - start}秒')


if __name__ == '__main__':
    main()

