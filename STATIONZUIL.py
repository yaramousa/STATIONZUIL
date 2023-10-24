import csv
import datetime
import random
bericht = input("Voer uw bericht in:")
if len(bericht) > 140:
       print ('u kunt helaas niet meer schrijven')
tijd = datetime.datetime.now()
print(tijd)
naam = input("Voer uw naam in: ")
if not naam:
       print ('aanoniem')
station = ['enschede','utrecht','henglo']
stations = random.choice(station)
print(stations)
veldnamen = ['bericht','naam', 'tijd','station','beoordeling']
bestand = open('Ns-bericht.csv', 'w')
writer = csv.DictWriter(bestand, veldnamen)
writer.writeheader()
writer.writerow(
       {'bericht': bericht,
        'naam': naam,
        'tijd': tijd,
        'station': stations,
        })
beoordeling =input('goedegekeurd of afgekeurd')
tid= datetime.datetime.now()
k= input('voer je naam van mod:')
j=input('voer je email van mod:')

if beoordeling == 'goedgekeurd':



    y=open('Ns-berichten','r')
    writer = csv.DictWriter(bestand,veldnamen)
    writer.writerow({
          'beoordeling': beoordeling
    })
    print('als is in de bestand')
else:
    print('er is niks in de bestand opgeslan')














