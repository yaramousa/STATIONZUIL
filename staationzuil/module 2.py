import psycopg2
from _datetime import datetime


connection_string = "dbname='stationzuil2' user='postgres' password='123yy' host='localhost'"
conn = psycopg2.connect(connection_string)
cursor = conn.cursor()



    #een leeg dic om gegevens van mod te slaan.
moderator ={}
bestand = open('Ns-bericht.csv')
gegevens = bestand.readlines()
for regel in gegevens:
        gegeven = regel.split(',')
        email = gegeven[1]
        wachtwoord = gegeven[2]
        samen= moderator[email]=wachtwoord # tovoegen aan mod dic
bestand.close()

file=open('Ns-bericht.csv')
test=file.readlines()
for  text in test:
         test=text.split(',')
         bericht=test[0]
         datum_tijd=test[2]
         naam=test[1]
         station=test[4].strip()
         beoordeling = True #'Goedgekeurd'

gegevens_berichten=[]


naam = input('voer u naam:')
emailadres = input('voer hier u email in:')
wachtwoord = input('voer hier u wachtwoord in:')

def moderator():

   if email in moderator and wachtwoord in moderator:
      login = True
   else:
      login = False

file1= open('Ns-bericht.csv')
bericht = file1.readlines()
for regel in bericht:
    berichten = regel.split(',')
    bericht = berichten[0]
    print('bericht')


    print('Geef hier je beoordeel in:')
    situatie = input('is het bericht goedgekeurd (ja) of afgekeurd(nee):')

    kies1='ja'
    kies2='nee'

    if situatie in kies1:
        beoordeel= True
        print(' het bericht is goedgekeurd')
    elif situatie in kies2:
         beoordeel= False
         print('het bericht is afgekeurd')

    query3_moderator = '''INSERT INTO Bericht (bericht_text, datum_tijd, gebruiker_naam, goedkeuring, station_city)
                    VALUES (%s, %s, %s, %s, %s);'''

    data3_moderator = (bericht, datum_tijd, naam, beoordeling, station)
    print(data3_moderator)
    cursor.execute(query3_moderator, data3_moderator)


    conn.commit()
    bestand.close()
    print('gegevens goed ingevoerd voor de tabel berichten en moderator')





def sQl():
    datum_tijd = datetime.now()

    query_moderator = '''INSERT INTO (naam, email) FROM Moderator VALUES (%s, %s);'''
    data_moderator= (naam,emailadres)
    cursor.execute(query_moderator,data_moderator)
    conn.commit()
    """ query1_moderator = '''SELECT station_city FROM station_service WHERE stationsnaam = %s;'''

        data1_moderator = (station,)
        cursor.execute(query1_moderator, data1_moderator)
        conn.commit()"""



def verwijder_bericht():
    # checklist.clear()
    delete = open('Ns-bericht.csv')
    y = delete.readlines()
    delete = open('Ns-bericht.csv', 'w')
    delete.writelines(y)
    print('Beoordelen is gelukt, het bericht is goed opgeslagen!')




login=moderator()
if login == False:
    print('helaas,ongeldig gegevens:')

if login == True:
   print('de gegevens zijn goed')
   sQl()
   verwijder_bericht()


beoordeling()







