class aerolineaView:
    def __init__(self):
        print()

    def pedirInformacion(self, mensaje):
        return input(mensaje)

    def agregarNuevaAerolinea(self):
        print("Creacion de nueva aerolinea")

    def listaDeAerolineas(self, lista):
        print("Visualizacion de las aerolineas")
        for aerolinea in lista:
            estaAerolinea = lista[aerolinea]
            print("Nombre:", estaAerolinea.nombre, "/ Anio de fundacion:", estaAerolinea.anioFundacion)

    def actualizarAerolinea(self):
        print("Actualizacion de la informacion de la aerolinea")

    def idNoEncontrado(self):
        print("No se encontro el ID solicitado")
