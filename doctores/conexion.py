import mysql.connector

def conectar(): 
    database = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "",
        database = "ahr_citas",
        port = 3306
    )

    cursor = database.cursor(bufferd = True)

    return [database, cursor]