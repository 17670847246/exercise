import time



class Clock:

    def __init__(self, second):
        self.second = second

    def has(self):
        return self.second

    def run(self):
        self.second -= 1
        return self.second

    def write(self):
        print(f'{self.second}')

def main():
    clock = Clock(50)
    while clock.has():
        clock.run()
        time.sleep(1)
        clock.write()



if __name__ == '__main__':
    main()

