class tripulacionView:
    def __init__(self):
        print()

    def pedirInformacion(self, mensaje):
        return input(mensaje)

    def agregarNuevoTripulante(self):
        print("Creacion de nuevo tripulante")

    def listaDeTripulacion(self, lista):
        print("Visualizacion de la tripulacion")
        for tripulacion in lista:
            esteTripulante = lista[tripulacion]
            print("Cedula:", esteTripulante.cedula, "/ Nombres:", esteTripulante.nombres, "/ Apellidos:",
                  esteTripulante.apellidos, "/ Fecha de nacimiento:", esteTripulante.fechaNacimiento, "/ Genero:",
                  esteTripulante.genero, "/ Direccion:", esteTripulante.direccion, "/ Numero de telefono:",
                  esteTripulante.numeroTelefono, "/ Correo electronico:", esteTripulante.correoElectronico,
                  "/ Cargo:", esteTripulante.cargo, "/ Cantidad de anios de experiencia:",
                  esteTripulante.cantidadAniosExperiencia, "/ Cantidad maxima de horas de trabajo diarias:",
                  esteTripulante.cantidadMaximaHorasTrabajoDiarias)

    def actualizarTripulacion(self):
        print("Actualizacion de la informacion de la tripulacion")

    def idNoEncontrado(self):
        print("No se encontro el ID solicitado")
