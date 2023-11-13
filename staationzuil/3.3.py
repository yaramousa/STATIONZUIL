import psycopg2

connection_string= "dbname='stationzuil' user='postgres' password='123yy' host='localhost'"
conn = psycopg2.connect(connection_string)
cursor = conn.cursor()

query="SELECT feedback FROM feedback where  ORDER BY  invoerdatum DESC LIMIT 5;"


    # query1= "INSERT INTO feedback(feedback, naam, datum, tijd, filiaal_id) VALUES (feedback, naam, datum, tijd);"
    # cursor.execute(query1)


cursor.execute(query)
regels = cursor.fetchall()


for regel in regels:
    print(regel[0])
conn.close()