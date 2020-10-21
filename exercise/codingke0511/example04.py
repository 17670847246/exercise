"""

"""
import os
import time


class Clock:

    def __init__(self, hour=0, minute=0, secord=0):
        self.hour = hour
        self.minute = minute
        self.secord = secord

    def show(self):
        """报时"""
        print('%02d:%02d:%02d'% (self.hour, self.minute, self.secord))

    def run(self):
        """走字"""
        self.secord += 1
        if self.secord == 60:
            self.minute += 1
            self.secord = 0
            if self.minute == 60:
                self.hour += 1
                self.minute = 0
                if self.hour == 24:
                    self.hour = 0




clock = Clock(0, 0, 2)
clock.show()
while True:
    os.system('cls')
    clock.show()
    time.sleep(1)
    clock.run()
