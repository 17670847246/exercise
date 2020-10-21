"""
JSON ---> JavaScript Object Notation ---> JavaScript创建对象的字面量语法 ---> 数据格式



JSON:{name:'大锤', age: 30, sex: true}
Python字典:{'name': '大锤', 'age': 30, 'sex': True}

网络API（数据接口）---> 免费的/付费的 ---> 获取程序中需要的数据 ---> JSON


Python中要实现并发编程有三种方式：
    1. 多线程
    2. 多进程
    3. 异步编程
"""

import time
from threading import Thread
import ujson

import requests

def download(pic_url, filename):
    resp = requests.get(pic_url)
    with open(f'Images/{filename}', 'wb') as file:
        file.write(resp.content)

def main():
    resp = requests.get('http://api.tianapi.com/meinv/index?key=90c02279d2964b0d1e6c70d99e291a6c&rand=1&num=20')
    print(type(resp.text), resp.text)
    data_dict = ujson.loads(resp.text)
    items = data_dict['newslist']
    start = time.time()
    threads = []
    for item in items:
        pic_url = item['picUrl']
        filename = pic_url[pic_url.rfind('/') + 1:]
        # target - 线程启动之后要执行的任务，通常是一个函数或对象方法
        # args - 线程启动后要执行的任务的参数
        t = Thread(target=download, args=(pic_url, filename))
        threads.append(t)
        # 调用start方法启动线程
        t.start()
    # 等待所有线程结束
    for t in threads:
        # 等待t线程对象执行结束
        t.join()
    end = time.time()
    print(f'下载图片所需要的时间{end - start}')

if __name__ == '__main__':
    main()












