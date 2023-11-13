class tripulacionModel:
    def __init__(self, cedula, nombres, apellidos, fechaNacimiento, genero, direccion, numeroTelefono,
                 correoElectronico, cargo, cantidadAniosExperiencia, cantidadMaximaHorasTrabajoDiarias):
        self.cedula = cedula
        self.nombres = nombres
        self.apellidos = apellidos
        self.fechaNacimiento = fechaNacimiento
        self.genero = genero
        self.direccion = direccion
        self.numeroTelefono = numeroTelefono
        self.correoElectronico = correoElectronico
        self.cargo = cargo
        self.cantidadAniosExperiencia = cantidadAniosExperiencia
        self.cantidadMaximaHorasTrabajoDiarias = cantidadMaximaHorasTrabajoDiarias

    def setCedula(self, cedula):
        self.cedula = cedula

    def setNombres(self, nombres):
        self.nombres = nombres

    def setApellidos(self, apellidos):
        self.apellidos = apellidos

    def setFechaNacimiento(self, fechaNacimiento):
        self.fechaNacimiento = fechaNacimiento

    def setGenero(self, genero):
        self.genero = genero

    def setDireccion(self, direccion):
        self.direccion = direccion

    def setNumeroTelefono(self, numeroTelefono):
        self.numeroTelefono = numeroTelefono

    def setCorreoElectronico(self, correoElectronico):
        self.correoElectronico = correoElectronico

    def setCargo(self, cargo):
        self.cargo = cargo

    def setCantidadAniosExperiencia(self, cantidadAniosExperiencia):
        self.cantidadAniosExperiencia = cantidadAniosExperiencia

    def setCantidadMaximaHorasTrabajoDiarias(self, cantidadMaximaHorasTrabajoDiarias):
        self.cantidadMaximaHorasTrabajoDiarias = cantidadMaximaHorasTrabajoDiarias


class listaTripulacion:
    def __init__(self):
        self.lista = {}

    def getTripulacion(self):
        return self.lista

    def agregarTripulacion(self, id, tripulacion):
        self.lista[id] = tripulacion
        print("El tripulante se agrego a la lista de tripulacion")
