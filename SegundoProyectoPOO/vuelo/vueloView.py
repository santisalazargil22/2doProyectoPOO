class vueloView:
    def __init__(self):
        print()

    def pedirInformacion(self, mensaje):
        return input(mensaje)

    def agregarNuevoVuelo(self):
        print("Creacion de nuevo vuelo")

    def listaDeVuelos(self, lista):
        print("Visualizacion de los vuelos")
        for vuelo in lista:
            esteVuelo = lista[vuelo]
            print("Numero de identificacion:", esteVuelo.numeroIdentificacion, "/ Fecha:", esteVuelo.fecha,
                  "/ Ciudades de origen:", esteVuelo.ciudadesOrigen, "/ Destino:", esteVuelo.destino)

    def actualizarVuelo(self):
        print("Actualizacion de la informacion del vuelo")

    def idNoEncontrado(self):
        print("No se encontro el ID solicitado")
