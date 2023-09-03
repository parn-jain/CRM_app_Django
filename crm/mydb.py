import mysql.connector
dataBase = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    passwd = 'Pj@123456',
    port = '3306',
)

cursorObject = dataBase.cursor()

cursorObject.execute('CREATE DATABASE projectX')
print('All done!!')