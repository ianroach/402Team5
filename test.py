import pyodbc

server = '402team5server.database.windows.net'
database = '402Team5Database'
username = 'ianroach'
password = '!Jrir1662!'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
print("Connection to db succesful")


