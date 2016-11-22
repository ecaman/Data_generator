from Home import *


#tests
class Device:
    def __init__(self, home):
        self.home = home
    def print_home(self):
        print(self.home.nb_people)
        print (self.home.nb_dish_washer)


home = Home()
device = Device(home)
device.print_home()



