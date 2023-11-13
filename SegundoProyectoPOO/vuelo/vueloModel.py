class vueloModel:
    def __init__(self, numeroIdentificacion, fecha, ciudadesOrigen, destino):
        self.numeroIdentificacion = numeroIdentificacion
        self.fecha = fecha
        self.ciudadesOrigen = ciudadesOrigen
        self.destino = destino

    def setNumeroIdentificacion(self, numeroIdentificacion):
        self.numeroIdentificacion = numeroIdentificacion

    def setFecha(self, fecha):
        self.fecha = fecha

    def setCiudadesOrigen(self, ciudadesOrigen):
        self.ciudadesOrigen = ciudadesOrigen

    def setDestino(self, destino):
        self.destino = destino


class listaVuelos:
    def __init__(self):
        self.lista = {}

    def getVuelos(self):
        return self.lista

    def agregarVuelo(self, id, vuelo):
        self.lista[id] = vuelo
        print("El vuelo se agrego a la lista de vuelos")
