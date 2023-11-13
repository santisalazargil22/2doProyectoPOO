class avionView:
    def __init__(self):
        print()

    def pedirInformacion(self, mensaje):
        return input(mensaje)

    def agregarNuevoAvion(self):
        print("Creacion de nuevo avion")

    def listaDeAviones(self, lista):
        print("Visualizacion de los aviones")
        for avion in lista:
            esteAvion = lista[avion]
            print("Marca:", esteAvion.marca, "/ Modelo:", esteAvion.modelo, "/ Capacidad de pasajeros:",
                  esteAvion.capacidadPasajeros, "/ Velocidad maxima:", esteAvion.velocidadMaxima, "/ Autonomia:",
                  esteAvion.autonomia, "/ Anio de fabricacion:", esteAvion.anioFabricacion, "/ Estado:",
                  esteAvion.estado, "/ Altitud maxima:", esteAvion.altitudMaxima, "/ Cantidad de motores:",
                  esteAvion.cantidadMotores, "/ Categoria:", esteAvion.categoria)

    def actualizarAvion(self):
        print("Actualizacion de la informacion del avion")

    def idNoEncontrado(self):
        print("No se encontro el ID solicitado")
