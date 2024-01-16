
import tkinter as tk
from PIL import Image, ImageTk
import requests
import psycopg2 as pg

#connection_string = "dbname='stationzuil2', 'user='postgres', 'password='123456 yara dilmon', host='20.90.189.40'"
conn = pg.connect(dbname='stationzuil2', user='postgres', password='123456yaradilmon', host='20.90.189.40')
cursor = conn.cursor()




# deze functie is voor de logo ns
def NS_logo():
    NS_path = "img/Logo-NS-v2.png"
# in deze om de afbeeldign van logo ns te openen
    ns_logo = Image.open(NS_path)
    ns_logoo = ns_logo.resize((200, 200))
# hier om de foto weertegeven in Tk
    ns_logophoto = ImageTk.PhotoImage(ns_logoo)

    ns_logo_label = tk.Label(master=logoFrame, image=ns_logophoto, background='LightBlue1')
    ns_logo_label.image = ns_logophoto
    ns_logo_label.pack(side=tk.TOP)
    # ns_logo_label.pack(side=tk.LEFT)

# in deze functie om de gegevens uit de specfiek station uit tabel te halen
def stations(station):
    query = f"SELECT * FROM station_service WHERE station_city = '{station}';"
    cursor.execute(query)
    # hier door fetchone wordt de enige rij van de specfiek station te halen uit de tabel en  retourneert de gegevens
    facilitteiten = cursor.fetchone()
    print(f"Faciliteitteninformatie zijn: {facilitteiten}")
    return facilitteiten

    # gegevens = stations(station)

station = input('Voer stationsnaam in, Je mag kiezen tussen( Enschede, Almelo en Utrecht:) ')
gegevens=stations(station)

# in deze functie om de laatste 5 goedgekeurde berichten te halen
def berichten():
    query = f"SELECT * FROM Bericht WHERE goedkeuring = TRUE AND station_city = '{station}' ORDER BY datum_tijd DESC LIMIT 5;"
    cursor.execute(query)
    # hier om de laatse 5 berichten te halen voor het specfiek station
    return cursor.fetchall()

# in deze functie om facilliteiten te halen voor de gekozen station
def facilitteiten(station):
    query = f"SELECT * FROM station_service WHERE station_city = '{station}';"
    cursor.execute(query)
    regels = cursor.fetchone()

    if regels:
        # om te bepalen de situatie van de verschillende facilliteiten als aanwezig is of niet
        ov_bike = "aanwezig" if regels[2] else "niet aanwezig"
        elevator = "aanwezig" if regels[3] else "niet aanwezig"
        toilet = "aanwezig" if regels[4] else "niet aanwezig"
        park_and_ride = "aanwezig" if regels[5] else "niet aanwezig"

        ov_bike_img = f"img/img_ovfiets.png"
        elevator_img = f"img/img_lift.png"
        toilet_img = f"img/img_toilet.png"
        park_and_ride_img = f"img/img_pr.png"

        # hier om de images te openen en de groote te passen
        ov_bike_img = Image.open(ov_bike_img).resize((50, 50))
        elevator_img = Image.open(elevator_img).resize((50, 50))
        toilet_img = Image.open(toilet_img).resize((50, 50))
        park_and_ride_img = Image.open(park_and_ride_img).resize((50, 50))

        ov_bike_img = ImageTk.PhotoImage(ov_bike_img)
        elevator_img = ImageTk.PhotoImage(elevator_img)
        toilet_img = ImageTk.PhotoImage(toilet_img)
        park_and_ride_img = ImageTk.PhotoImage(park_and_ride_img)
        # hier een dic genaakt met de informatie over de facilliteiten en afbeelding
        images = {
            "ov_bike": {"text": f'Ov_bike: {ov_bike}', "image": ov_bike_img},
            "elevator": {"text": f'Elevator: {elevator}', "image": elevator_img},
            "toilet": {"text": f'Toilet: {toilet}', "image": toilet_img},
            "park_and_ride": {"text": f'P+R: {park_and_ride}', "image": park_and_ride_img},
        }
        return images
    else:
        return f"Faciliteiteninformatie niet beschikbaar voor {station}."


# in deze functie om een nieuwe frame te maken
def nieuwe (regel):
    centerframe = tk.Frame(master=root, bg='LightBlue1')
    centerframe.pack(side=tk.LEFT, anchor=tk.CENTER, padx=20)
    # om de text en afbeelding te halen
    for bericht, data in regel.items():
        facilitty_test = data["text"]
        image = data["image"]
        # hier om label voor test en afbeelding te maken
        label = tk.Label(centerframe, text=facilitty_test, compound="left", image=image, font=('Helvetica', 12), bg='LightBlue1')
        label.image = image
        label.pack(pady=6)


# deze functie om het weer weertegevne voor de gekozen station
def weer(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    api_key = "56470f387c7d2f1a05a790af71d3e4fe"
    city_url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}'
    city_response = requests.get(city_url)
    city_data = city_response.json()[0]
    lat = city_data['lat']
    lon = city_data['lon']
    weather_url = f'{base_url}?lat={lat}&lon={lon}&appid={api_key}'
    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()
    weather = weather_data['weather'][0]['main']
    temp = weather_data['main']['temp']
    pres = weather_data['main']['pressure']
    humidity = weather_data['main']['humidity']
    deftemp = round(temp - 273.15, 2)
    # data = f'Current weather: {weather}\nTemperature: {deftemp}°C\nHumidity: {humidity}%'
    data = f'Current weather: {weather}\nTemprature: {deftemp}°C\nPressure: {pres}Pa\nhumidity: {humidity}W'
    return str(data)

# deze functie haalt de goede berichten en weer en facilitteiten voor station
def update_berict_weer():
    goedgekeurde = berichten()
    weerr = weer(station)
    facilititeitenn = facilitteiten(station)

    #update van berichten i
    berichtLabel.config(text="\n".join([f"{message[1]} - {message[4]}" for message in goedgekeurde]))
    berichtLabel.config(font=('Helvetica', 20))

    #update van het weer
    weatherLabel.config(text=weerr)
    weatherLabel.config(font=('Helvetica', 20))
    nieuwe(facilititeitenn)


root = tk.Tk()
root.geometry('1000x600')
root.configure(bg='LightBlue1')
logoFrame = tk.Frame(master=root, bg='LightBlue1')
logoFrame.pack(anchor=tk.N)
# om ne logo weertegeven
NS_logo()
berichtFrame = tk.Frame(master=root, bg='LightBlue1')
berichtFrame.pack(side=tk.LEFT, anchor=tk.CENTER, padx=20)
weatherFrame = tk.Frame(master=root, bg='LightBlue1')
weatherFrame.pack(side=tk.RIGHT, anchor=tk.CENTER, padx=20)
# label voor goedgekeurde berichte weertegeven
berichtLabel = tk.Label(master=berichtFrame, background='LightBlue1', height=13, width=40, font=('Helvetica', 12))
berichtLabel.pack(pady=20)
# om het weer weertegeven
weatherLabel = tk.Label(master=weatherFrame, background='LightBlue1',font=('Helvetica', 12))
weatherLabel.pack(pady=50)

update_berict_weer ()
root.mainloop()
