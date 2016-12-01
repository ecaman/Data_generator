from settings import *
from random import *
from time import *


class DishWasher:
    def __init__(self, home):
        self.dish_washer_sec = self.generate_device_consumption()
        self.usage_hours = self.generate_usage_hours()
        self.home = home
        self.isOn = False
        self.last_usage = 0
        self.current_consumption = 0

    def generate_device_consumption(self):
        dish_washer_sec = []
        dish_washer_min = \
            [0, 60, 100, 93, 93, 93, 93, 93, 93, 93, 93, 73, 60, 107, 93, 93, 1332, 1951, 2005, 2005, 2005, 2005, 2005,
            2005, 2005, 2005, 2005, 2011, 2005, 2011, 2005, 2005, 2011, 2005, 2005, 2005, 2005, 2011, 2018, 1665, 566,
            107, 107, 107, 107, 107, 100, 60, 53, 107, 107, 107, 107, 100, 60, 80, 107, 1971, 2005, 2005, 2018, 2031,
            2018, 946, 1259, 1891, 2005, 2011, 2018, 2005, 2011, 2018, 2018, 2018, 2018, 2018, 1212, 60, 0]
        for i in range(0, len(dish_washer_min)):
            for j in range(1, 61):
                dish_washer_sec.append(dish_washer_min[i])
        return dish_washer_sec

    def generate_usage_hours(self):
        usage_hours = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0]
        return usage_hours

    def launch_device(self, start_time, actual_time):
        self.isOn = True

        if (self.isOn == True):
            for count in range (0, len(self.dish_washer_sec)):
                actual_time += 1
                print "test 1"
                self.current_consumption = self.dish_washer_sec[count]
                print actual_time
                print start_time + len(self.dish_washer_sec)
                print self.current_consumption
                # ligne en dessous a revoir...
            self.last_usage = actual_time
            isOn = False

        else:
            pass
        return actual_time


class Home:
    # Constructeur
    def __init__(self):
        self.nb_people = self.generate_nb_people()
        self.nb_dish_washer = self.generate_nb_dish_washer()
        self.dish_washer = self.create_dish_washer()
        self.total_consumption = 0

    def generate_nb_people(self):
        var = randrange(0, 278, 1)
        if (var <= 97):
            nb_people = 1
        elif (var > 97 and var <= 189):
            nb_people = 2
        elif (var > 189 and var <= 228):
            nb_people = 3
        elif (var > 228 and var <= 261):
            nb_people = 4
        elif (var > 261 and var <= 273):
            nb_people = 5
        else:
            nb_people = 6
        return nb_people

    def generate_nb_dish_washer(self):
        if(self.nb_people == 1):
            nb_dish_washer = 0
        elif(self.nb_people > 5):
            nb_dish_washer = 1
        else :
            # proportion in france: 57% of houses own a dish_washer
            rdm = randrange(0, 100, 1)
            if(rdm < 57):
                nb_dish_washer = 1
            else:
                nb_dish_washer = 0
        return nb_dish_washer

    def create_dish_washer(self):
        if(self.nb_people == 1):
            dish_washer = None
        else:
            dish_washer = DishWasher(self)
        return dish_washer

    def calculate_consumption(self):
        self.total_consumption = self.dish_washer.current_consumption
        return self.total_consumption


actual_time = 0
actual_time_hours = 0
tmp = 0
home = Home()
print home.nb_people
print home.nb_dish_washer
print home.dish_washer.dish_washer_sec
sleep(2)
for actual_time in range(1, 2592001): # 1 mois = 2592000 secs
    tmp += 1
    if(tmp == 3600):
        actual_time_hours += 1
        tmp = 0
    if(actual_time_hours == 24):
        actual_time_hours = 0

    #check if device could be turned on every hour
    if (actual_time % 3600 == 0):

        if (home.dish_washer.usage_hours[actual_time_hours] == 1):
            actual_percentage_usage = ((actual_time - home.dish_washer.last_usage)*100)/(432000/home.nb_people)
            rdm = randrange(1, 100)
            print (actual_percentage_usage, rdm)
            if (rdm < actual_percentage_usage):
                print "Device launched"
                print actual_time
                print actual_time_hours
                print home.total_consumption
                actual_time = home.dish_washer.launch_device(actual_time, actual_time)
                continue



    print actual_time
    print actual_time_hours

    print home.total_consumption, " Watts"













