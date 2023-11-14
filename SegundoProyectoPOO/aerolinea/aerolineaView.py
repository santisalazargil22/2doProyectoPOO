# NOTA: La presente documentacion solo se realizara en el MVC de esta clase, debido a que las implementaciones en las
# demas clases son muy similares a esta pero adaptadas para funcionar con sus respectivos atributos y funciones propias

class aerolineaView:
    def __init__(self):
        print()

    # Metodo que me permitira recibir una entrada de dato por parte del usuario junto con un mensaje personalizable

    def pedirInformacion(self, mensaje):
        return input(mensaje)

    def agregarNuevaAerolinea(self):
        print("Creacion de nueva aerolinea")

    # Metodo que recorrera el diccionario de objetos creado e imprimira todos los datos de dichos objetos creados

    def listaDeAerolineas(self, lista):
        print("Visualizacion de las aerolineas")
        for aerolinea in lista:
            estaAerolinea = lista[aerolinea]
            print("Nombre:", estaAerolinea.nombre, "/ Anio de fundacion:", estaAerolinea.anioFundacion)

    def actualizarAerolinea(self):
        print("Actualizacion de la informacion de la aerolinea")

    def idNoEncontrado(self):
        print("No se encontro el ID solicitado")
