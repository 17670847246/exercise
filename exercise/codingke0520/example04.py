"""
多个线程竞争一个资源的场景 ---> 被多个线程竞争的资源称为临界资源
临界资源需要适当的保护 否则就会导致资源的状态是不正确的 ---> 锁对象

创建和释放线程开销都是很大的，程序中（服务器断代码）尽量不要频繁的创建和释放线程
我们可以选择一种空间换区时间的方式 ---> 线程池 ---> 用一个容器保存预创建的线程
使用线程的过程中不创建也不释放线程，只需要向线程池借用线程，用完之后归还即可

"""
import time
from concurrent.futures.thread import ThreadPoolExecutor
from threading import Thread, RLock


class Account:
    """银行账户"""

    def __init__(self):
        self.balance = 0.0
        self.lock = RLock()

    def deposit(self, money):
        # 获得锁 self.lock.acquire() / self.lock.release()
        with self.lock:
            new_balance = self.balance + money
            time.sleep(0.01)
            self.balance = new_balance

def main():
    """主函数"""
    account = Account()
    pool = ThreadPoolExecutor(max_workers=32)
    futures = []
    for _ in range(100):
        future = pool.submit(account.deposit, 1)
        futures.append(future)
    for f in futures:
        f.result()
    print(account.balance)

if __name__ == '__main__':
    main()
