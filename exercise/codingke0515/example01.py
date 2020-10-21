"""
倒计时计时器
"""
import time


class CountdownClock:

    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def is_over(self):
        return self.hour == 0 and self.minute == 0 and self.second == 0

    def run(self):
        if self.hour > 0 or self.minute > 0 or self.second > 0:
            self.second -= 1
            if self.second < 0:
                if self.minute > 0:
                    self.second = 59
                    self.minute -= 1
                    if self.minute < 0:
                        self.minute = 59
                        self.hour -= 1
                elif self.hour > 0:
                    self.second = 59
                    self.minute = 59
                    self.hour -= 1

    def show(self):
        print(f'{self.hour:0>2d}:{self.minute:0>2d}:{self.second:0>2d}')


def main():
    clock = CountdownClock(1, 0, 2)
    clock.show()
    while not clock.is_over():
        time.sleep(0.001)
        clock.run()
        clock.show()
    print('时间到')
if __name__ == '__main__':
    main()