class avionModel:
    def __init__(self, marca, modelo, capacidadPasajeros, velocidadMaxima, autonomia, anioFabricacion, estado,
                 altitudMaxima, cantidadMotores, categoria):
        self.marca = marca
        self.modelo = modelo
        self.capacidadPasajeros = capacidadPasajeros
        self.velocidadMaxima = velocidadMaxima
        self.autonomia = autonomia
        self.anioFabricacion = anioFabricacion
        self.estado = estado
        self.altitudMaxima = altitudMaxima
        self.cantidadMotores = cantidadMotores
        self.categoria = categoria

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

    def setAltitudMaxima(self, altitudMaxima):
        self.altitudMaxima = altitudMaxima

    def setCantidadMotores(self, cantidadMotores):
        self.cantidadMotores = cantidadMotores

    def setCategoria(self, categoria):
        self.categoria = categoria


class listaAviones:
    def __init__(self):
        self.lista = {}

    def getAviones(self):
        return self.lista

    def agregarAvion(self, id, avion):
        self.lista[id] = avion
        print("El avion se agrego a la lista de aviones")
