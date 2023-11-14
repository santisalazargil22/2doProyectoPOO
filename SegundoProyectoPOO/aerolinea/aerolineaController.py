from aerolinea.aerolineaModel import listaAerolineas, aerolineaModel
from aerolinea.aerolineaView import aerolineaView


# NOTA: La presente documentacion solo se realizara en el MVC de esta clase, debido a que las implementaciones en las
# demas clases son muy similares a esta pero adaptadas para funcionar con sus respectivos atributos y funciones propias

class aerolineaController:
    def __init__(self):
        self.model = listaAerolineas()
        self.view = aerolineaView()
        self.contadorAerolineas = 0

    # Contador que sirve como ID para objetos que se crean, aumenta en uno en este metodo para cambiar su valor

    def incrementarContador(self):
        self.contadorAerolineas = self.contadorAerolineas + 1
        return self.contadorAerolineas

    # Metodo que primero pide informacion sobre todos los atributos de la presente clase, posteriormente sobreescribe
    # los datos previamente ingresados en un objeto creandolo con dicha informacion y finaliza agregando ese objeto
    # creado con su contador como llave a la lista PROPIA de dicho objeto (el diccionario que creamos en el model)

    def crearNuevaAerolinea(self):
        self.view.agregarNuevaAerolinea()
        nombre = self.view.pedirInformacion("Agregue el nombre ")
        anioFundacion = self.view.pedirInformacion("Agregue el anio de fundacion ")
        nuevaAerolinea = aerolineaModel(nombre, anioFundacion)
        self.model.agregarAerolinea(self.incrementarContador(), nuevaAerolinea)

    # Primero retorna el diccionario que contiene a mis objetos creados, despues se encarga de recorrelo e imprimir su
    # informacion (metodo que se encuentra en el view)

    # En este punto un dato importante a tener en cuenta es que cuando se cree el primer objeto de una clase su llave
    # asignada sera el contador en 1, posteriormente cuando se creen mas objetos de la misma clase los IDs de asignacion
    # seran este contador incrementado en 1 (como se observa arriba)

    def listaDeAerolineas(self):
        todasLasAerolineas = self.model.getAerolineas()
        self.view.listaDeAerolineas(todasLasAerolineas)

    # En este metodo primero se somete el ingreso de ID a actualizar en un bucle donde verifican varias cosas, mediante
    # manejo de excepciones primero verifica que el ID ingresado no sea ninguna cadena de caracteres o tipo de valor
    # diferente a un entero, una vez pasa esta prueba corrobora que el ID exista dentro del diccionario de objetos como
    # llave de algun objeto, en caso afirmativo se pedira la nueva informacion correspondiente a este objeto que se
    # actualiza y con los metodos setters se sobreescribira la informacion, de lo contrario (no encuentra el ID) se
    # mostrara un mensaje indicando que no se encontro el ID y se retornara 0 para que se salga del metodo en ejecucion

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
