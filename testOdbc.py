import pyodbc
import random


server = '402team5server.database.windows.net'
database = '402Team5Database'
username = 'ianroach'
password = '!Jrir1662!'

random_number = random.uniform(20, 30)

conn = pyodbc.connect('DRIVER=FreeTDS;SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+password+';TDS_Version=8.0;')
cursor = conn.cursor()

print('Connection succesful')

cursor.execute("SET IDENTITY_INSERT TeamFive ON")
cursor.execute("insert into TeamFive(DeviceId, TeamId, Temperature, Measure) values (1, 5, "+str(random_number)+", 'Farenheit')")
conn.commit()

print("Data inserted into TemFive")


