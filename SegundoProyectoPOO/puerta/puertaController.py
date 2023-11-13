from puerta.puertaModel import listaPuertas, puertaModel
from puerta.puertaView import puertaView


class puertaController:
    def __init__(self):
        self.model = listaPuertas()
        self.view = puertaView()
        self.contadorPuertas = 0

    def incrementarContador(self):
        self.contadorPuertas = self.contadorPuertas + 1
        return self.contadorPuertas

    def crearNuevaPuerta(self):
        self.view.agregarNuevaPuerta()
        numeroIdentificacion = self.view.pedirInformacion("Agregue el numero de identificacion ")
        ubicacion = self.view.pedirInformacion("Agregue la ubicacion ")
        disponibilidad = self.view.pedirInformacion("Agregue la disponibilidad ")
        horaEmbarque = self.view.pedirInformacion("Agregue la hora de embarque ")
        nuevaPuerta = puertaModel(numeroIdentificacion, ubicacion, disponibilidad, horaEmbarque)
        self.model.agregarPuerta(self.incrementarContador(), nuevaPuerta)

    def listaDePuertas(self):
        todasLasPuertas = self.model.getPuertas()
        self.view.listaDePuertas(todasLasPuertas)

    def actualizarPuerta(self):
        self.view.actualizarPuerta()
        while True:
            try:
                idAActualizar = int(
                    self.view.pedirInformacion("Ingrese el ID de la puerta de embarque que desea actualizar: "))
                if idAActualizar in self.model.lista:
                    break
                else:
                    self.view.idNoEncontrado()
                    return 0
            except ValueError:
                print("El valor ingresado no es un numero entero. Intente nuevamente.")
        puerta = self.model.getPuertas().get(idAActualizar)
        numeroIdentificacion = self.view.pedirInformacion("Agregue el nuevo numero de identificacion ")
        puerta.setNumeroIdentificacion(numeroIdentificacion)
        ubicacion = self.view.pedirInformacion("Agregue la nueva ubicacion ")
        puerta.setUbicacion(ubicacion)
        disponibilidad = self.view.pedirInformacion("Agregue la nueva disponibilidad ")
        puerta.setDisponibilidad(disponibilidad)
        horaEmbarque = self.view.pedirInformacion("Agregue la nueva hora de embarque ")
        puerta.setHoraEmbarque(horaEmbarque)
