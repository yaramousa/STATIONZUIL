import csv
import datetime
import random



#module1
def feedeback():
    bericht = input("Voer uw bericht in:")
    if len(bericht) > 140:
           print ('u kunt helaas niet meer schrijven')
    else:
           datum = datetime.date.today()
           tijd= datetime.datetime.now().time().strftime('%H:%M:%S')

           naam = input("Voer uw naam in: ")
           if len(naam)== 0:
              print ('aanoniem')
           station = ['Enschede','Utrecht','Almelo']
           station_city = random.choice(station)
           print( station_city)
           print('u bericht is goed ingevoerd')



           with open  ('Ns-bericht.csv', 'a',newline='',encoding='utf-8') as bestand:
                 writer = csv.writer(bestand)
                 writer.writerow([bericht, naam, datum,tijd, station_city])



while True:
    feedeback()


