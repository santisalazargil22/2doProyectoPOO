from vuelo.vueloModel import listaVuelos, vueloModel
from vuelo.vueloView import vueloView


class vueloController:
    def __init__(self):
        self.model = listaVuelos()
        self.view = vueloView()
        self.contadorVuelos = 0

    def incrementarContador(self):
        self.contadorVuelos = self.contadorVuelos + 1
        return self.contadorVuelos

    def crearNuevoVuelo(self):
        self.view.agregarNuevoVuelo()
        numeroIdentificacion = self.view.pedirInformacion("Agregue el numero de identificacion ")
        fecha = self.view.pedirInformacion("Agregue la fecha ")
        ciudadesOrigen = self.view.pedirInformacion("Agregue las ciudades de origen ")
        destino = self.view.pedirInformacion("Agregue el destino ")
        nuevoVuelo = vueloModel(numeroIdentificacion, fecha, ciudadesOrigen, destino)
        self.model.agregarVuelo(self.incrementarContador(), nuevoVuelo)

    def listaDeVuelos(self):
        todosLosVuelos = self.model.getVuelos()
        self.view.listaDeVuelos(todosLosVuelos)

    def actualizarVuelo(self):
        self.view.actualizarVuelo()
        while True:
            try:
                idAActualizar = int(self.view.pedirInformacion("Ingrese el ID del vuelo que desea actualizar: "))
                if idAActualizar in self.model.lista:
                    break
                else:
                    self.view.idNoEncontrado()
                    return 0
            except ValueError:
                print("El valor ingresado no es un numero entero. Intente nuevamente.")
        vuelo = self.model.getVuelos().get(idAActualizar)
        numeroIdentificacion = self.view.pedirInformacion("Agregue el nuevo numero de identificacion ")
        vuelo.setNumeroIdentificacion(numeroIdentificacion)
        fecha = self.view.pedirInformacion("Agregue la nueva fecha ")
        vuelo.setFecha(fecha)
        ciudadesOrigen = self.view.pedirInformacion("Agregue las nuevas ciudades de origen ")
        vuelo.setCiudadesOrigen(ciudadesOrigen)
        destino = self.view.pedirInformacion("Agregue el nuevo destino ")
        vuelo.setDestino(destino)
