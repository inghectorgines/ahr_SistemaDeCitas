import doctores.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Cita:

    def __init__(self, doctor_id, paciente="", descripcion=""):
        self.doctor_id = doctor_id
        self.paciente = paciente
        self.descripcion = descripcion
    
    def guardar(self):
        sql= "INSERT INTO citas VALUES(null, %s, %s, %s, NOW())"
        cita = (self.doctor_id, self.paciente, self.descripcion)

        cursor.execute(sql, cita)
        database.commit()

        return [cursor.rowcount, self]

    def listar(self):
        sql = f"SELECT * FROM citas WHERE doctor_id = {self.doctor_id}"

        cursor.execute(sql)
        result = cursor.fetchall()

        return result 

    def eliminar(self):
        sql = f"DELETE FROM citas WHERE doctor_id = {self.doctor_id} AND titulo LIKE '%{self.paciente}%'"

        cursor.execute(sql)
        database.commit()

        return[cursor.rowcount, self]
    
    def modificar(self,paciente,descripcion):
        sql = f"UPDATE citas SET paciente = '{paciente}', descripcion = '{descripcion}' 'WHERE doctor_id = {self.doctor_id} AND paciente LIKE '%{self.paciente}%'"
        try:
            cursor.execute(sql)
            database.commit()

            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result