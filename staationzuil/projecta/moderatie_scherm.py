from datetime import datetime
import psycopg2 as pg

# Verbinding maken met de database

conn = pg.connect(dbname='stationzuil2', user='postgres', password='123456yaradilmon', host='20.90.189.40')
cursor = conn.cursor()

def moderator():
    # Invoer van e-mail en wachtwoord van moderator
    email = input('Voer uw e-mail in: ').strip()
    wachtwoord = input('Voer uw wachtwoord in: ').strip()
    combinatie = email + ',' + wachtwoord + '\n'

    # om bestand van mod te olezen
    file = open('moderator.txt')
    regel = file.readlines()
    file.close()

    # controleren of de combinatie klopt is
    if combinatie not in regel:
        print('helaas, uw gegevens kloppen niet')

    # als de gegevens van moderator klopt niet
    else:
        print('Uw heeft succesvol ingelogd')

        moderator_email = email
        # hier om de bestand van bericht te lezen.
        file2 = open('Ns-bericht.csv')
        berichten = file2.readlines()
        file2.close()

        # Loop door de berichten
        for bericht in berichten:
            details = bericht.strip().split(',')

            # hier om te controleren als de lijst met 4 element is .
            if len(details) >= 4:
                bericht_text = details[0]
                naam = details[2]
                station = details[3]

                # hier ald de bericht niet leeg is wordt de bericht geprint
                if bericht_text != "":
                    print(f"Bericht: {bericht_text}")

                # Vragen om goedkeuring of afkeuring voor de bericht te geven (ja of nee)
                goedkeuring = input('Geef goedgekeurd of afgekeurd (ja of nee)?')
                kies1 = 'ja'
                kies2 = 'nee'

                # datum_tijd = datetime.now()

                # als de keuze is ja wordt datum bericht geprint
                if goedkeuring == kies1:
                    print('Het bericht is goedgekeurd en wordt in de tabel opgeslagen')
                    datum_tijd = datetime.now()
                    print(datum_tijd)

                    # en wordt de bericht met de goedkeurd in de tabel toegevoegd
                    cursor.execute(
                        "INSERT INTO bericht (bericht_text, goedkeuring, datum_tijd, gebruiker_naam, station_city,email) VALUES (%s, %s, %s, %s, %s,%s)",
                        (bericht_text, True, datum_tijd, naam, station,moderator_email))

                # als is afgekeurd,wordt deze bericht en de datum geprint
                elif goedkeuring == kies2:
                    print('de bericht is afgekeurd')

                    datum_tijd = datetime.now()
                    print(datum_tijd)

                    # hier wordt de bericht aan da database toegevoegd
                    cursor.execute(
                        "INSERT INTO bericht (bericht_text, goedkeuring, datum_tijd, gebruiker_naam, station_city,email) VALUES (%s, %s, %s, %s, %s,%s)",
                        (bericht_text, False, datum_tijd, naam, station,moderator_email))

# deze functie om de bestand leef te maken
def verwijder_bericht():

    with open('Ns-bericht.csv', 'w'):
        pass
    print('Beoordelen is gelukt, het bericht is goed opgeslagen!')

# hier wordt de functie geroept
result = moderator()
verwijder_bericht()


conn.commit()
conn.close()








