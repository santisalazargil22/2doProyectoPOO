from pasajero.pasajeroModel import listaPasajeros, pasajeroModel
from pasajero.pasajeroView import pasajeroView


class pasajeroController:
    def __init__(self):
        self.model = listaPasajeros()
        self.view = pasajeroView()
        self.contadorPasajeros = 0

    def incrementarContador(self):
        self.contadorPasajeros = self.contadorPasajeros + 1
        return self.contadorPasajeros

    def crearNuevoPasajero(self):
        self.view.agregarNuevoPasajero()
        cedula = self.view.pedirInformacion("Agregue el numero de cedula ")
        nombres = self.view.pedirInformacion("Agregue los nombres ")
        apellidos = self.view.pedirInformacion("Agregue los apellidos ")
        fechaNacimiento = self.view.pedirInformacion("Agregue la fecha de nacimiento ")
        genero = self.view.pedirInformacion("Agregue el genero ")
        direccion = self.view.pedirInformacion("Agregue la direccion ")
        numeroTelefono = self.view.pedirInformacion("Agregue el numero de telefono ")
        correoElectronico = self.view.pedirInformacion("Agregue el correo electronico ")
        nacionalidad = self.view.pedirInformacion("Agregue la nacionalidad ")
        cantidadMaletasEnBodega = self.view.pedirInformacion("Agregue la cantidad de maletas en bodega ")
        resumenInformacionMedica = self.view.pedirInformacion("Agregue el resumen de la informacion medica ")
        nuevoPasajero = pasajeroModel(cedula, nombres, apellidos, fechaNacimiento, genero, direccion, numeroTelefono,
                                      correoElectronico, nacionalidad, cantidadMaletasEnBodega,
                                      resumenInformacionMedica)
        self.model.agregarPasajero(self.incrementarContador(), nuevoPasajero)

    def listaDePasajeros(self):
        todosLosPasajeros = self.model.getPasajeros()
        self.view.listaDePasajeros(todosLosPasajeros)

    def actualizarPasajero(self):
        self.view.actualizarPasajero()
        while True:
            try:
                idAActualizar = int(self.view.pedirInformacion("Ingrese el ID del pasajero que desea actualizar: "))
                if idAActualizar in self.model.lista:
                    break
                else:
                    self.view.idNoEncontrado()
                    return 0
            except ValueError:
                print("El valor ingresado no es un numero entero. Intente nuevamente.")
        pasajero = self.model.getPasajeros().get(idAActualizar)
        cedula = self.view.pedirInformacion("Agregue el nuevo numero de cedula ")
        pasajero.setCedula(cedula)
        nombres = self.view.pedirInformacion("Agregue los nuevos nombres ")
        pasajero.setNombres(nombres)
        apellidos = self.view.pedirInformacion("Agregue los nuevos apellidos ")
        pasajero.setApellidos(apellidos)
        fechaNacimiento = self.view.pedirInformacion("Agregue la nueva fecha de nacimiento ")
        pasajero.setFechaNacimiento(fechaNacimiento)
        genero = self.view.pedirInformacion("Agregue el nuevo genero ")
        pasajero.setGenero(genero)
        direccion = self.view.pedirInformacion("Agregue la nueva direccion ")
        pasajero.setDireccion(direccion)
        numeroTelefono = self.view.pedirInformacion("Agregue el nuevo numero de telefono ")
        pasajero.setNumeroTelefono(numeroTelefono)
        correoElectronico = self.view.pedirInformacion("Agregue el nuevo correo electronico ")
        pasajero.setCorreoElectronico(correoElectronico)
        nacionalidad = self.view.pedirInformacion("Agregue la nueva nacionalidad ")
        pasajero.setNacionalidad(nacionalidad)
        cantidadMaletasEnBodega = self.view.pedirInformacion("Agregue la nueva cantidad de maletas en bodega ")
        pasajero.setCantidadMaletasEnBodega(cantidadMaletasEnBodega)
        resumenInformacionMedica = self.view.pedirInformacion("Agregue el nuevo resumen de la informacion medica ")
        pasajero.setResumenInformacionMedica(resumenInformacionMedica)
