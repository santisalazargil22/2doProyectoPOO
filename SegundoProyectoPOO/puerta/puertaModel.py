class puertaModel:
    def __init__(self, numeroIdentificacion, ubicacion, disponibilidad, horaEmbarque):
        self.numeroIdentificacion = numeroIdentificacion
        self.ubicacion = ubicacion
        self.disponibilidad = disponibilidad
        self.horaEmbarque = horaEmbarque

    def setNumeroIdentificacion(self, numeroIdentificacion):
        self.numeroIdentificacion = numeroIdentificacion

    def setUbicacion(self, ubicacion):
        self.ubicacion = ubicacion

    def setDisponibilidad(self, disponibilidad):
        self.disponibilidad = disponibilidad

    def setHoraEmbarque(self, horaEmbarque):
        self.horaEmbarque = horaEmbarque


class listaPuertas:
    def __init__(self):
        self.lista = {}

    def getPuertas(self):
        return self.lista

    def agregarPuerta(self, id, puerta):
        self.lista[id] = puerta
        print("La puerta de embarque se agrego a la lista de puertas de embarque")
