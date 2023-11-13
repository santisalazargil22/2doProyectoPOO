from avion.avionModel import listaAviones, avionModel
from avion.avionView import avionView


class avionController:
    def __init__(self):
        self.model = listaAviones()
        self.view = avionView()
        self.contadorAviones = 0

    def incrementarContador(self):
        self.contadorAviones = self.contadorAviones + 1
        return self.contadorAviones

    def crearNuevoAvion(self):
        self.view.agregarNuevoAvion()
        marca = self.view.pedirInformacion("Agregue la marca ")
        modelo = self.view.pedirInformacion("Agregue el modelo ")
        capacidadPasajeros = self.view.pedirInformacion("Agregue la capacidad de pasajeros ")
        velocidadMaxima = self.view.pedirInformacion("Agregue la velocidad maxima ")
        autonomia = self.view.pedirInformacion("Agregue la autonomia ")
        anioFabricacion = self.view.pedirInformacion("Agregue el anio de fabricacion ")
        estado = self.view.pedirInformacion("Agregue el estado ")
        altitudMaxima = self.view.pedirInformacion("Agregue la altitud maxima ")
        cantidadMotores = self.view.pedirInformacion("Agregue la cantidad de motores ")
        categoria = self.view.pedirInformacion("Agregue la categoria ")
        nuevoAvion = avionModel(marca, modelo, capacidadPasajeros, velocidadMaxima, autonomia, anioFabricacion, estado,
                                altitudMaxima, cantidadMotores, categoria)
        self.model.agregarAvion(self.incrementarContador(), nuevoAvion)

    def listaDeAviones(self):
        todosLosAviones = self.model.getAviones()
        self.view.listaDeAviones(todosLosAviones)

    def actualizarAvion(self):
        self.view.actualizarAvion()
        while True:
            try:
                idAActualizar = int(self.view.pedirInformacion("Ingrese el ID del avion que desea actualizar: "))
                if idAActualizar in self.model.lista:
                    break
                else:
                    self.view.idNoEncontrado()
                    return 0
            except ValueError:
                print("El valor ingresado no es un numero entero. Intente nuevamente.")
        avion = self.model.getAviones().get(idAActualizar)
        marca = self.view.pedirInformacion("Agregue la nueva marca: ")
        avion.setMarca(marca)
        modelo = self.view.pedirInformacion("Agregue el nuevo modelo: ")
        avion.setModelo(modelo)
        capacidadPasajeros = self.view.pedirInformacion("Agregue la nueva capacidad de pasajeros: ")
        avion.setCapacidadPasajeros(capacidadPasajeros)
        velocidadMaxima = self.view.pedirInformacion("Agregue la nueva velocidad maxima: ")
        avion.setVelocidadMaxima(velocidadMaxima)
        autonomia = self.view.pedirInformacion("Agregue la nueva autonomia: ")
        avion.setAutonomia(autonomia)
        anioFabricacion = self.view.pedirInformacion("Agregue el nuevo anio de fabricacion: ")
        avion.setAnioFabricacion(anioFabricacion)
        estado = self.view.pedirInformacion("Agregue el nuevo estado: ")
        avion.setEstado(estado)
        altitudMaxima = self.view.pedirInformacion("Agregue la nueva altitud maxima: ")
        avion.setAltitudMaxima(altitudMaxima)
        cantidadMotores = self.view.pedirInformacion("Agregue la nueva cantidad de motores: ")
        avion.setCantidadMotores(cantidadMotores)
        categoria = self.view.pedirInformacion("Agregue la nueva categoria: ")
        avion.setCategoria(categoria)
