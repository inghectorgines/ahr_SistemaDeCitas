import doctores.doctor as modelo
import citas.acciones

class Acciones:

    def registro(self):
        print("Se realizara su registro en el sistema...")

        nombre = input("¿Cual es su nombre?: ")
        apellidos = input("Cuales son sus apellidos?: ")
        consultorio = input("Ingresa el numero de consultorio: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")

        doctor = modelo.Doctor(nombre, apellidos, consultorio, email, password)
        registro = doctor.registrar()

        if registro[0] >= 1:
            print(f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("\nNo te has registrado!!!")



    def login(self):
        print("Identifiquese en el sistema...")

        try:
            email = input("Introduzca su email: ")
            password = input("Introduzca su contraseña: ")

            doctor = modelo.Doctor('', '', '', email, password)
            login = doctor.identificar()

            if email == login[3]:
                print(f"Bienvenido doctor {login[1]}, se ha registrado en el sistema el {login[5]}")
                self.proximasAcciones(login)
        
        except Exception as e:
            #print(type(e))
            #print(type(e).__name__)
            print("\nLogin incorrecto!! Intentalo mas tarde")


    def proximasAcciones(self, doctor):
        print(""" 
            Acciones disponibles:
            - Registrar cita (registrar)
            - Mostrar citas (mostrar)
            - Eliminar cita (eliminar)
            - Modificar cita (modificar)
            - Salir (salir)
            
            """)
        accion = input("¿Que quiere realizar?: ")
        hazEl = citas.acciones.Acciones()

        if accion == "crear":
           # print("Crearemos una cita")
            hazEl.crear(doctor)
            self.proximasAcciones(doctor)

        elif accion == "mostrar":
            #print("Se mostraran todas las citas")
            hazEl.mostrar(doctor)
            self.proximasAcciones(doctor)

        elif accion == "modificar":
            hazEl.modificar(doctor)
            self.proximasAcciones(doctor)

        elif accion == "eliminar":
            #print("Se eliminara una cita ")
            hazEl.borrar(doctor)
            self.proximasAcciones(doctor)

        elif accion == "salir":
            exit()