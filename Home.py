from random import *
from Dish_washer import *

class Home:


    #Constructeur
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
            dish_washer = Dish_washer(self)
        return dish_washer

    def calculate_consumption(self):
        self.total_consumption = self.dish_washer.current_consumption
        return self.total_consumption

