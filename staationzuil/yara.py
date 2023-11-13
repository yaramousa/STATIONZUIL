def toon_informatie():
    laatste_berichten = bericht()
    weer = current_weather()
    station_faciliteiten = faciliteiten(station)

    info_venster = Toplevel(root)

    bericht_label = Label(info_venster, text="Laatste 5 Berichten:")
    bericht_label.pack()

    bericht_text = Text(info_venster, height=5, width=50)
    for bericht in laatste_berichten:
        bericht_text.insert(END, f"{bericht}\n")
    bericht_text.pack()

    weer_label = Label(info_venster, text="Weersinformatie:")
    weer_label.pack()

    weer_text = Text(info_venster, height=5, width=50)
    weer_text.insert(END, weer)
    weer_text.pack()

    faciliteiten_label = Label(info_venster, text="Station Faciliteiten:")
    faciliteiten_label.pack()

    faciliteiten_text = Text(info_venster, height=5, width=50)
    faciliteiten_text.insert(END, station_faciliteiten)
    faciliteiten_text.pack()

toon_informatie()





