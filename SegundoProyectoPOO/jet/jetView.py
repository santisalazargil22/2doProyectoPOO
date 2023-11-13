class jetView:
    def __init__(self):
        print()

    def pedirInformacion(self, mensaje):
        return input(mensaje)

    def agregarNuevoJet(self):
        print("Creacion de nuevo jet")

    def listaDeJets(self, lista):
        print("Visualizacion de los jets")
        for jet in lista:
            esteJet = lista[jet]
            print("Marca:", esteJet.marca, "/ Modelo:", esteJet.modelo, "/ Capacidad de pasajeros:",
                  esteJet.capacidadPasajeros, "/ Velocidad maxima:", esteJet.velocidadMaxima, "/ Autonomia:",
                  esteJet.autonomia, "/ Anio de fabricacion:", esteJet.anioFabricacion, "/ Estado:",
                  esteJet.estado, "/ Propietario:", esteJet.propietario, "/ Lista de servicios a bordo:",
                  esteJet.listaServiciosABordo, "/ Lista de destinos frecuentes:", esteJet.listaDestinosFrecuentes)

    def actualizarJet(self):
        print("Actualizacion de la informacion del jet")

    def idNoEncontrado(self):
        print("No se encontro el ID solicitado")
