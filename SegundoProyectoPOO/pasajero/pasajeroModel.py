class pasajeroModel:
    def __init__(self, cedula, nombres, apellidos, fechaNacimiento, genero, direccion, numeroTelefono,
                 correoElectronico, nacionalidad, cantidadMaletasEnBodega, resumenInformacionMedica):
        self.cedula = cedula
        self.nombres = nombres
        self.apellidos = apellidos
        self.fechaNacimiento = fechaNacimiento
        self.genero = genero
        self.direccion = direccion
        self.numeroTelefono = numeroTelefono
        self.correoElectronico = correoElectronico
        self.nacionalidad = nacionalidad
        self.cantidadMaletasEnBodega = cantidadMaletasEnBodega
        self.resumenInformacionMedica = resumenInformacionMedica

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

    def setNacionalidad(self, nacionalidad):
        self.nacionalidad = nacionalidad

    def setCantidadMaletasEnBodega(self, cantidadMaletasEnBodega):
        self.cantidadMaletasEnBodega = cantidadMaletasEnBodega

    def setResumenInformacionMedica(self, resumenInformacionMedica):
        self.resumenInformacionMedica = resumenInformacionMedica


class listaPasajeros:
    def __init__(self):
        self.lista = {}

    def getPasajeros(self):
        return self.lista

    def agregarPasajero(self, id, pasajero):
        self.lista[id] = pasajero
        print("El pasajero se agrego a la lista de pasajeros")
