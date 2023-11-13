class puertaView:
    def __init__(self):
        print()

    def pedirInformacion(self, mensaje):
        return input(mensaje)

    def agregarNuevaPuerta(self):
        print("Creacion de nueva puerta de embarque")

    def listaDePuertas(self, lista):
        print("Visualizacion de las puertas de embarque")
        for puerta in lista:
            estaPuerta = lista[puerta]
            print("Numero de identificacion:", estaPuerta.numeroIdentificacion, "/ Ubicacion:", estaPuerta.ubicacion,
                  "/ Disponibilidad:", estaPuerta.disponibilidad, "/ Hora de embarque:", estaPuerta.horaEmbarque)

    def actualizarPuerta(self):
        print("Actualizacion de la informacion de la puerta de embarque")

    def idNoEncontrado(self):
        print("No se encontro el ID solicitado")
