from helicoptero.helicopteroModel import listaHelicopteros, helicopteroModel
from helicoptero.helicopteroView import helicopteroView


class helicopteroController:
    def __init__(self):
        self.model = listaHelicopteros()
        self.view = helicopteroView()
        self.contadorHelicopteros = 0

    def incrementarContador(self):
        self.contadorHelicopteros = self.contadorHelicopteros + 1
        return self.contadorHelicopteros

    def crearNuevoHelicoptero(self):
        self.view.agregarNuevoHelicoptero()
        marca = self.view.pedirInformacion("Agregue la marca ")
        modelo = self.view.pedirInformacion("Agregue el modelo ")
        capacidadPasajeros = self.view.pedirInformacion("Agregue la capacidad de pasajeros ")
        velocidadMaxima = self.view.pedirInformacion("Agregue la velocidad maxima ")
        autonomia = self.view.pedirInformacion("Agregue la autonomia ")
        anioFabricacion = self.view.pedirInformacion("Agregue el anio de fabricacion ")
        estado = self.view.pedirInformacion("Agregue el estado ")
        cantidadRotores = self.view.pedirInformacion("Agregue la cantidad de rotores ")
        capacidadElevacion = self.view.pedirInformacion("Agregue la capacidad de elevacion ")
        usoEspecifico = self.view.pedirInformacion("Agregue el uso especifico ")
        nuevoHelicoptero = helicopteroModel(marca, modelo, capacidadPasajeros, velocidadMaxima, autonomia,
                                            anioFabricacion, estado,
                                            cantidadRotores, capacidadElevacion, usoEspecifico)
        self.model.agregarHelicoptero(self.incrementarContador(), nuevoHelicoptero)

    def listaDeHelicopteros(self):
        todosLosHelicopteros = self.model.getHelicopteros()
        self.view.listaDeHelicopteros(todosLosHelicopteros)

    def actualizarHelicoptero(self):
        self.view.actualizarHelicoptero()
        while True:
            try:
                idAActualizar = int(self.view.pedirInformacion("Ingrese el ID del helicoptero que desea actualizar: "))
                if idAActualizar in self.model.lista:
                    break
                else:
                    self.view.idNoEncontrado()
                    return 0
            except ValueError:
                print("El valor ingresado no es un numero entero. Intente nuevamente.")
        helicoptero = self.model.getHelicopteros().get(idAActualizar)
        marca = self.view.pedirInformacion("Agregue la nueva marca: ")
        helicoptero.setMarca(marca)
        modelo = self.view.pedirInformacion("Agregue el nuevo modelo: ")
        helicoptero.setModelo(modelo)
        capacidadPasajeros = self.view.pedirInformacion("Agregue la nueva capacidad de pasajeros: ")
        helicoptero.setCapacidadPasajeros(capacidadPasajeros)
        velocidadMaxima = self.view.pedirInformacion("Agregue la nueva velocidad maxima: ")
        helicoptero.setVelocidadMaxima(velocidadMaxima)
        autonomia = self.view.pedirInformacion("Agregue la nueva autonomia: ")
        helicoptero.setAutonomia(autonomia)
        anioFabricacion = self.view.pedirInformacion("Agregue el nuevo anio de fabricacion: ")
        helicoptero.setAnioFabricacion(anioFabricacion)
        estado = self.view.pedirInformacion("Agregue el nuevo estado: ")
        helicoptero.setEstado(estado)
        cantidadRotores = self.view.pedirInformacion("Agregue la nueva cantidad de rotores: ")
        helicoptero.setCantidadRotores(cantidadRotores)
        capacidadElevacion = self.view.pedirInformacion("Agregue la nueva capacidad de elevacion: ")
        helicoptero.setCapacidadElevacion(capacidadElevacion)
        usoEspecifico = self.view.pedirInformacion("Agregue el nuevo uso especifico: ")
        helicoptero.setUsoEspecifico(usoEspecifico)
