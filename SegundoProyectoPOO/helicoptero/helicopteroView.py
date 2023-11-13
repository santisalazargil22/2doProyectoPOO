class helicopteroView:
    def __init__(self):
        print()

    def pedirInformacion(self, mensaje):
        return input(mensaje)

    def agregarNuevoHelicoptero(self):
        print("Creacion de nuevo helicoptero")

    def listaDeHelicopteros(self, lista):
        print("Visualizacion de los helicopteros")
        for helicoptero in lista:
            esteHelicoptero = lista[helicoptero]
            print("Marca:", esteHelicoptero.marca, "/ Modelo:", esteHelicoptero.modelo, "/ Capacidad de pasajeros:",
                  esteHelicoptero.capacidadPasajeros, "/ Velocidad maxima:", esteHelicoptero.velocidadMaxima,
                  "/ Autonomia:",
                  esteHelicoptero.autonomia, "/ Anio de fabricacion:", esteHelicoptero.anioFabricacion, "/ Estado:",
                  esteHelicoptero.estado, "/ Cantidad de rotores:", esteHelicoptero.cantidadRotores,
                  "/ Capacidad de elevacion:",
                  esteHelicoptero.capacidadElevacion, "/ Uso especifico:", esteHelicoptero.usoEspecifico)

    def actualizarHelicoptero(self):
        print("Actualizacion de la informacion del helicoptero")

    def idNoEncontrado(self):
        print("No se encontro el ID solicitado")
