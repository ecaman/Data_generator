from Home import Home
from random import *
from settings import *

actual_time = 0
actual_time_hours = 0
tmp = 0
home = Home()
print home.nb_people
print home.nb_dish_washer
for actual_time in range (1, 2592001/4): # 1 mois = 2592001 secs
    tmp += 1
    if(tmp == 3600):
        actual_time_hours +=1
        tmp = 0
    if(actual_time_hours == 24):
        actual_time_hours = 0

    #check if device could be turned on
    if (home.dish_washer.usage_hours[actual_time_hours] == 1):
        actual_percentage_usage = ((actual_time - home.dish_washer.last_usage)*100)/(432000/home.nb_people)
        rdm = randrange(1, 100)
        print (actual_percentage_usage, rdm)
        if (rdm < actual_percentage_usage):
            home.dish_washer.launch_device(actual_time)


    print actual_time
    print actual_time_hours

    print home.total_consumption, " Watts"