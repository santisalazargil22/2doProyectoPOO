from jet.jetModel import listaJets, jetModel
from jet.jetView import jetView


class jetController:
    def __init__(self):
        self.model = listaJets()
        self.view = jetView()
        self.contadorJets = 0

    def incrementarContador(self):
        self.contadorJets = self.contadorJets + 1
        return self.contadorJets

    def crearNuevoJet(self):
        self.view.agregarNuevoJet()
        marca = self.view.pedirInformacion("Agregue la marca ")
        modelo = self.view.pedirInformacion("Agregue el modelo ")
        capacidadPasajeros = self.view.pedirInformacion("Agregue la capacidad de pasajeros ")
        velocidadMaxima = self.view.pedirInformacion("Agregue la velocidad maxima ")
        autonomia = self.view.pedirInformacion("Agregue la autonomia ")
        anioFabricacion = self.view.pedirInformacion("Agregue el anio de fabricacion ")
        estado = self.view.pedirInformacion("Agregue el estado ")
        propietario = self.view.pedirInformacion("Agregue el propietario ")
        listaServiciosABordo = self.view.pedirInformacion("Agregue la lista de servicios a bordo ")
        listaDestinosFrecuentes = self.view.pedirInformacion("Agregue la lista de destinos frecuentes ")
        nuevoJet = jetModel(marca, modelo, capacidadPasajeros, velocidadMaxima, autonomia, anioFabricacion, estado,
                            propietario, listaServiciosABordo, listaDestinosFrecuentes)
        self.model.agregarJet(self.incrementarContador(), nuevoJet)

    def listaDeJets(self):
        todosLosJets = self.model.getJets()
        self.view.listaDeJets(todosLosJets)

    def actualizarJet(self):
        self.view.actualizarJet()
        while True:
            try:
                idAActualizar = int(self.view.pedirInformacion("Ingrese el ID del jet que desea actualizar: "))
                if idAActualizar in self.model.lista:
                    break
                else:
                    self.view.idNoEncontrado()
                    return 0
            except ValueError:
                print("El valor ingresado no es un numero entero. Intente nuevamente.")
        jet = self.model.getJets().get(idAActualizar)
        marca = self.view.pedirInformacion("Agregue la nueva marca: ")
        jet.setMarca(marca)
        modelo = self.view.pedirInformacion("Agregue el nuevo modelo: ")
        jet.setModelo(modelo)
        capacidadPasajeros = self.view.pedirInformacion("Agregue la nueva capacidad de pasajeros: ")
        jet.setCapacidadPasajeros(capacidadPasajeros)
        velocidadMaxima = self.view.pedirInformacion("Agregue la nueva velocidad maxima: ")
        jet.setVelocidadMaxima(velocidadMaxima)
        autonomia = self.view.pedirInformacion("Agregue la nueva autonomia: ")
        jet.setAutonomia(autonomia)
        anioFabricacion = self.view.pedirInformacion("Agregue el nuevo anio de fabricacion: ")
        jet.setAnioFabricacion(anioFabricacion)
        estado = self.view.pedirInformacion("Agregue el nuevo estado: ")
        jet.setEstado(estado)
        propietario = self.view.pedirInformacion("Agregue el nuevo propietario ")
        jet.setPropietario(propietario)
        listaServiciosABordo = self.view.pedirInformacion("Agregue la nueva lista de servicios a bordo ")
        jet.setListaServiciosABordo(listaServiciosABordo)
        listaDestinosFrecuentes = self.view.pedirInformacion("Agregue la nueva lista de destinos frecuentes ")
        jet.setListaDestinosFrecuentes(listaDestinosFrecuentes)
