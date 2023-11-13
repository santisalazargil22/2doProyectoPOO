class jetModel:
    def __init__(self, marca, modelo, capacidadPasajeros, velocidadMaxima, autonomia, anioFabricacion, estado,
                 propietario, listaServiciosABordo, listaDestinosFrecuentes):
        self.marca = marca
        self.modelo = modelo
        self.capacidadPasajeros = capacidadPasajeros
        self.velocidadMaxima = velocidadMaxima
        self.autonomia = autonomia
        self.anioFabricacion = anioFabricacion
        self.estado = estado
        self.propietario = propietario
        self.listaServiciosABordo = listaServiciosABordo
        self.listaDestinosFrecuentes = listaDestinosFrecuentes

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

    def setPropietario(self, propietario):
        self.propietario = propietario

    def setListaServiciosABordo(self, listaServiciosABordo):
        self.listaServiciosABordo = listaServiciosABordo

    def setListaDestinosFrecuentes(self, listaDestinosFrecuentes):
        self.listaDestinosFrecuentes = listaDestinosFrecuentes


class listaJets:
    def __init__(self):
        self.lista = {}

    def getJets(self):
        return self.lista

    def agregarJet(self, id, jet):
        self.lista[id] = jet
        print("El jet se agrego a la lista de jets")
