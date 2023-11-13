class pasajeroView:
    def __init__(self):
        print()

    def pedirInformacion(self, mensaje):
        return input(mensaje)

    def agregarNuevoPasajero(self):
        print("Creacion de nuevo pasajero")

    def listaDePasajeros(self, lista):
        print("Visualizacion de los pasajeros")
        for pasajero in lista:
            estePasajero = lista[pasajero]
            print("Cedula:", estePasajero.cedula, "/ Nombres:", estePasajero.nombres, "/ Apellidos:",
                  estePasajero.apellidos, "/ Fecha de nacimiento:", estePasajero.fechaNacimiento, "/ Genero:",
                  estePasajero.genero, "/ Direccion:", estePasajero.direccion, "/ Numero de telefono:",
                  estePasajero.numeroTelefono, "/ Correo electronico:", estePasajero.correoElectronico,
                  "/ Nacionalidad:", estePasajero.nacionalidad, "/ Cantidad de maletas en bodega:",
                  estePasajero.cantidadMaletasEnBodega, "/ Resumen de la informacion medica:",
                  estePasajero.resumenInformacionMedica)

    def actualizarPasajero(self):
        print("Actualizacion de la informacion del pasajero")

    def idNoEncontrado(self):
        print("No se encontro el ID solicitado")
