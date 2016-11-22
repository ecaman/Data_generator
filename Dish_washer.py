from Home import *
class Dish_washer:
    def __init__(self, home):
        self.dish_washer_sec = self.generate_device_consumption()
        self.home = home
    def generate_device_consumption(self):
        dish_washer_sec = []
        dish_washer_min = \
            [0, 60, 100, 93, 93, 93, 93, 93, 93, 93, 93, 73, 60, 107, 93, 93, 1332, 1951, 2005, 2005, 2005, 2005, 2005,
            2005, 2005, 2005, 2005, 2011, 2005, 2011, 2005, 2005, 2011, 2005, 2005, 2005, 2005, 2011, 2018, 1665, 566,
            107, 107, 107, 107, 107, 100, 60, 53, 107, 107, 107, 107, 100, 60, 80, 107, 1971, 2005, 2005, 2018, 2031,
            2018, 946, 1259, 1891, 2005, 2011, 2018, 2005, 2011, 2018, 2018, 2018, 2018, 2018, 1212, 60, 0]
        for i in range(0, len(dish_washer_min)):
            for j in range(0, 59):
                dish_washer_sec.append(dish_washer_min[i])
        return dish_washer_sec

    def generate_usage_hours(self):
        usage_hours = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0]
        if(self.home.nb_people == 2):
            pass




