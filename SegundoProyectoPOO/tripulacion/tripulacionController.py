from tripulacion.tripulacionModel import listaTripulacion, tripulacionModel
from tripulacion.tripulacionView import tripulacionView


class tripulacionController:
    def __init__(self):
        self.model = listaTripulacion()
        self.view = tripulacionView()
        self.contadorTripulacion = 0

    def incrementarContador(self):
        self.contadorTripulacion = self.contadorTripulacion + 1
        return self.contadorTripulacion

    def crearNuevoTripulante(self):
        self.view.agregarNuevoTripulante()
        cedula = self.view.pedirInformacion("Agregue el numero de cedula ")
        nombres = self.view.pedirInformacion("Agregue los nombres ")
        apellidos = self.view.pedirInformacion("Agregue los apellidos ")
        fechaNacimiento = self.view.pedirInformacion("Agregue la fecha de nacimiento ")
        genero = self.view.pedirInformacion("Agregue el genero ")
        direccion = self.view.pedirInformacion("Agregue la direccion ")
        numeroTelefono = self.view.pedirInformacion("Agregue el numero de telefono ")
        correoElectronico = self.view.pedirInformacion("Agregue el correo electronico ")
        cargo = self.view.pedirInformacion("Agregue el cargo ")
        cantidadAniosExperiencia = self.view.pedirInformacion("Agregue la cantidad de anios de experiencia ")
        cantidadMaximaHorasTrabajoDiarias = self.view.pedirInformacion(
            "Agregue la cantidad maxima de horas de trabajo diarias ")
        nuevoTripulante = tripulacionModel(cedula, nombres, apellidos, fechaNacimiento, genero, direccion,
                                           numeroTelefono,
                                           correoElectronico, cargo, cantidadAniosExperiencia,
                                           cantidadMaximaHorasTrabajoDiarias)
        self.model.agregarTripulacion(self.incrementarContador(), nuevoTripulante)

    def listaDeTripulacion(self):
        todaLaTripulacion = self.model.getTripulacion()
        self.view.listaDeTripulacion(todaLaTripulacion)

    def actualizarTripulacion(self):
        self.view.actualizarTripulacion()
        while True:
            try:
                idAActualizar = int(self.view.pedirInformacion("Ingrese el ID del tripulante que desea actualizar: "))
                if idAActualizar in self.model.lista:
                    break
                else:
                    self.view.idNoEncontrado()
                    return 0
            except ValueError:
                print("El valor ingresado no es un numero entero. Intente nuevamente.")
        tripulacion = self.model.getTripulacion().get(idAActualizar)
        cedula = self.view.pedirInformacion("Agregue el nuevo numero de cedula ")
        tripulacion.setCedula(cedula)
        nombres = self.view.pedirInformacion("Agregue los nuevos nombres ")
        tripulacion.setNombres(nombres)
        apellidos = self.view.pedirInformacion("Agregue los nuevos apellidos ")
        tripulacion.setApellidos(apellidos)
        fechaNacimiento = self.view.pedirInformacion("Agregue la nueva fecha de nacimiento ")
        tripulacion.setFechaNacimiento(fechaNacimiento)
        genero = self.view.pedirInformacion("Agregue el nuevo genero ")
        tripulacion.setGenero(genero)
        direccion = self.view.pedirInformacion("Agregue la nueva direccion ")
        tripulacion.setDireccion(direccion)
        numeroTelefono = self.view.pedirInformacion("Agregue el nuevo numero de telefono ")
        tripulacion.setNumeroTelefono(numeroTelefono)
        correoElectronico = self.view.pedirInformacion("Agregue el nuevo correo electronico ")
        tripulacion.setCorreoElectronico(correoElectronico)
        cargo = self.view.pedirInformacion("Agregue el nuevo cargo ")
        tripulacion.setCargo(cargo)
        cantidadAniosExperiencia = self.view.pedirInformacion("Agregue la nueva cantidad de anios de experiencia ")
        tripulacion.setCantidadAniosExperiencia(cantidadAniosExperiencia)
        cantidadMaximaHorasTrabajoDiarias = self.view.pedirInformacion(
            "Agregue la nueva cantidad maxima de horas de trabajo diarias ")
        tripulacion.setCantidadMaximaHorasTrabajoDiarias(cantidadMaximaHorasTrabajoDiarias)
