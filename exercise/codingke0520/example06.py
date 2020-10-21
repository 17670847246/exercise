from random import randint
from threading import Thread
from time import time, sleep


class DownloadTask(Thread):

    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print(f'开始下载{self._filename}')
        time_to_download = randint(5,7)
        sleep(time_to_download)
        print(f'{self._filename}下载完成!耗费了{time_to_download}')


def main():
    start = time()
    t1 = DownloadTask('从入门到精通')
    t1.start()
    t2 = DownloadTask('从入门到入狱')
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print(end-start)

if __name__ == '__main__':
    main()