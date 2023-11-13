from aerolinea.aerolineaModel import listaAerolineas, aerolineaModel
from aerolinea.aerolineaView import aerolineaView


class aerolineaController:
    def __init__(self):
        self.model = listaAerolineas()
        self.view = aerolineaView()
        self.contadorAerolineas = 0

    def incrementarContador(self):
        self.contadorAerolineas = self.contadorAerolineas + 1
        return self.contadorAerolineas

    def crearNuevaAerolinea(self):
        self.view.agregarNuevaAerolinea()
        nombre = self.view.pedirInformacion("Agregue el nombre ")
        anioFundacion = self.view.pedirInformacion("Agregue el anio de fundacion ")
        nuevaAerolinea = aerolineaModel(nombre, anioFundacion)
        self.model.agregarAerolinea(self.incrementarContador(), nuevaAerolinea)

    def listaDeAerolineas(self):
        todasLasAerolineas = self.model.getAerolineas()
        self.view.listaDeAerolineas(todasLasAerolineas)

    def actualizarAerolinea(self):
        self.view.actualizarAerolinea()
        while True:
            try:
                idAActualizar = int(self.view.pedirInformacion("Ingrese el ID de la aerolinea que desea actualizar: "))
                if idAActualizar in self.model.lista:
                    break
                else:
                    self.view.idNoEncontrado()
                    return 0
            except ValueError:
                print("El valor ingresado no es un numero entero. Intente nuevamente.")
        aerolinea = self.model.getAerolineas().get(idAActualizar)
        nombre = self.view.pedirInformacion("Agregue el nuevo nombre ")
        aerolinea.setNombre(nombre)
        anioFundacion = self.view.pedirInformacion("Agregue el nuevo anio de fundacion ")
        aerolinea.setAnioFundacion(anioFundacion)
