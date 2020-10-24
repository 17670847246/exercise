"""
迭代器：实现了迭代协议的对象。
迭代协议： __next__、__iter__
"""

class FibIter:

    def __init__(self, num):
        self.num =num
        self.count = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.num:
            self.a, self.b = self.b, self.a + self.b
            self.count += 1
            return self.a
        raise StopIteration()

fib_iter = FibIter(20)
print(next(fib_iter))
print(next(fib_iter))
for value in fib_iter:
    print(value)
print(4181/6765)