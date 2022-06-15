import citas.cita as modelo

class Acciones:

    def crear(self, doctor):
        print(f"Ok {doctor[1]}!!Crearemos una nueva cita...")

        paciente = input("Introduce el nombre completo de tu paciente: ")
        descripcion = input("Escribe el motivo de la consulta ")

        cita = modelo.Cita(doctor[0], paciente, descripcion)
        guardar = cita.guardar()

        if guardar[0] >= 1:
            print(f"\nPerfecto! Se a registrado la cita de: {cita.paciente}")

        else:
            print(f"\nNo se ha realizado la consulta, intentalo mas tarde")
        
    def mostrar(self, doctor):
        print(f"\n{doctor[1]}!!! Estas son sus proximas citas: ")

        cita = modelo.Cita(doctor[0])
        citas = cita.listar()


        for cita in citas:
            print("\n****************************")
            print(cita[2])
            print(cita[3])
            print("\n*****************************")

    def modificar(self, doctor):
            print(f"\n{doctor[1]} Editar cita ")
            print("Introduca los nuevos datos")

            paciente = input("Introduce el nombre del paciente: ")
            descripcion = input("Escribe la descripcion de la cita/consulta: ")
            cita = modelo.Cita(doctor[0], paciente, descripcion)
            modificar = cita.modificar()

    def borrar(self, doctor):
        print(f"\n{doctor[1]}!!! Borre sus citas")

        paciente = input("Introduzca el nombre del paciente de la cita a borrar: ")
        cita = modelo.Cita(doctor[0], paciente)
        eliminar = cita.eliminar()
        if eliminar[0]>= 1:
            print(f"Se borro la cita del paciente: {cita.paciente}")
        else:
            print("No se borro la cita, intente mas tarde...")