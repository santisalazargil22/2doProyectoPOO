class aerolineaModel:
    def __init__(self, nombre, anioFundacion):
        self.nombre = nombre
        self.anioFundacion = anioFundacion

    def setNombre(self, nombre):
        self.nombre = nombre

    def setAnioFundacion(self, anioFundacion):
        self.anioFundacion = anioFundacion


class listaAerolineas:
    def __init__(self):
        self.lista = {}

    def getAerolineas(self):
        return self.lista

    def agregarAerolinea(self, id, aerolinea):
        self.lista[id] = aerolinea
        print("La aerolinea se agrego a la lista de aerolineas")
