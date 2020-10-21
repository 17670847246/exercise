import os
import time
class count_down:

    def __init__(self, secord):
        self.secord = secord

    def show(self):
        print(self.secord)

    def run(self):
        self.secord -= 1

secords = count_down(2)

while True:
    os.system('cls')
    secords.show()
    time.sleep(1)
    secords.run()
    if secords.secord == 0:
        secords.show()
        break
