class helicopteroModel:
    def __init__(self, marca, modelo, capacidadPasajeros, velocidadMaxima, autonomia, anioFabricacion, estado,
                 cantidadRotores, capacidadElevacion, usoEspecifico):
        self.marca = marca
        self.modelo = modelo
        self.capacidadPasajeros = capacidadPasajeros
        self.velocidadMaxima = velocidadMaxima
        self.autonomia = autonomia
        self.anioFabricacion = anioFabricacion
        self.estado = estado
        self.cantidadRotores = cantidadRotores
        self.capacidadElevacion = capacidadElevacion
        self.usoEspecifico = usoEspecifico

    def setMarca(self, marca):
        self.marca = marca

    def setModelo(self, modelo):
        self.modelo = modelo

    def setCapacidadPasajeros(self, capacidadPasajeros):
        self.capacidadPasajeros = capacidadPasajeros

    def setVelocidadMaxima(self, velocidadMaxima):
        self.velocidadMaxima = velocidadMaxima

    def setAutonomia(self, autonomia):
        self.autonomia = autonomia

    def setAnioFabricacion(self, anioFabricacion):
        self.anioFabricacion = anioFabricacion

    def setEstado(self, estado):
        self.estado = estado

    def setCantidadRotores(self, cantidadRotores):
        self.cantidadRotores = cantidadRotores

    def setCapacidadElevacion(self, capacidadElevacion):
        self.capacidadElevacion = capacidadElevacion

    def setUsoEspecifico(self, usoEspecifico):
        self.usoEspecifico = usoEspecifico


class listaHelicopteros:
    def __init__(self):
        self.lista = {}

    def getHelicopteros(self):
        return self.lista

    def agregarHelicoptero(self, id, helicoptero):
        self.lista[id] = helicoptero
        print("El helicoptero se agrego a la lista de helicopteros")
