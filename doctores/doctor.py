import mysql.connector
import datetime
import hashlib
import doctores.conexion as conexion


#Llamar la clase conectar
connect =  conexion.conectar()
database = connect[0]
cursor = connect[1]

#print(database)

class Doctor:

    def __init__(self, nombre, apellidos, consultorio, email, password):
        self.nombre  = nombre
        self.apellidos = apellidos
        self.consultorio = consultorio
        self.email = email
        self.password = password

    def registrar(self):
        fecha = datetime.datetime.now()

    #Cifrar contraseña
        cifrado =  hashlib.sha3_256()
        cifrado.update(self.password.encode('utf8'))    

        sql = "INSERT INTO usuarios VALUE(null, %s, %s, %s, %s, %s, %s)"
        doctor = (self.nombre, self.apellidos, self.consultorio, self.email, cifrado.hexdigest(), fecha)

        try:
            cursor.execute(sql, doctor)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result


    def identificar(self):
        sql = "SELECT * FROM doctores WHERE email = %s AND password = %s"

        #cifrar contraseña
        cifrado =  hashlib.sha3_256()
        cifrado.update(self.password.encode('utf8'))  

        #Datos para consultar
        doctor = (self.email, cifrado.hexdigest())

        cursor.execute(sql, doctor)
        result = cursor.fetchone()

        return result