import mysql.connector
dataBase = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = 'Pj@123456'
)

#creating a cursor object
cursorObject = dataBase.cursor()

#creating a database
cursorObject.execute("CREATE DATABASE MinorProject")
print('All Done!')