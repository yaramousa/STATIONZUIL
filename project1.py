import datetime
import random
BERICHT = input("Voer uw bericht in")
tijd = datetime.datetime.now()
naam = input("Voer uw naam in ")
if naam !="":
       naam = 'aanoniem'
stations = ['utrecht','enschede','henglo']
station = random.choice(stations)