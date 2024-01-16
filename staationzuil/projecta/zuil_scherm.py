import csv
import datetime
import random
import psycopg2 as pg

# Verbinding maken met de database

conn = pg.connect(dbname='stationzuil2', user='postgres', password='123456yaradilmon', host='20.90.189.40')
cursor = conn.cursor()

def feedback():
    # Vraag de gebruiker om een bericht in te voeren
    bericht = input("Voer uw bericht in:")

    # Controleer of het bericht niet meer dan 140 tekens bevat
    if len(bericht) > 140:
        print('U kunt helaas niet meer schrijven')
    else:
        datum_tijd = datetime.datetime.now()

        # Vraag om de naam in te voeren,als leeg is geef anoniem.
        naam = input("Voer uw naam in: ")
        if naam == '':
               naam = 'anoniem'
               print('anonniem')

        # met random om een  willekeurig station te kiezen
        stations = ['Enschede', 'Utrecht', 'Almelo']
        station_city = random.choice(stations)
        print(station_city)

        # Voeg gegevens toe aan de tabel (Bericht)
        cursor.execute("""
            INSERT INTO Bericht (gebruiker_naam, datum_tijd, bericht_text, station_city)
            VALUES (%s, %s, %s, %s);
        """, (naam, datum_tijd, bericht, station_city))

        # hier wordt de bestand geopend om de gegevens intevoegen
        file=open('Ns-bericht.csv','a')
        y=csv.writer(file)
        y.writerow([bericht,datum_tijd,naam,station_city])

        conn.commit()

# Roep de functie aan
feedback()



