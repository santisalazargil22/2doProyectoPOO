# NOTA: La presente documentacion solo se realizara en el MVC de esta clase, debido a que las implementaciones en las
# demas clases son muy similares a esta pero adaptadas para funcionar con sus respectivos atributos y funciones propias

# Metodo constructor que contiene e inicializa los atributos de la clase en cuestion

class aerolineaModel:
    def __init__(self, nombre, anioFundacion):
        self.nombre = nombre
        self.anioFundacion = anioFundacion

    # Metodos setters que permiten la asignacion de dichos atributos en la creacion de objetos

    def setNombre(self, nombre):
        self.nombre = nombre

    def setAnioFundacion(self, anioFundacion):
        self.anioFundacion = anioFundacion


# Inicializacion de diccionario que almacenara objetos de la presente clase y metodo get para retornar dicho diccionario

class listaAerolineas:
    def __init__(self):
        self.lista = {}

    def getAerolineas(self):
        return self.lista

    # Metodo que posteriormente permitira agregar al diccionario el objeto que he creado junto con su llave (un ID)

    def agregarAerolinea(self, id, aerolinea):
        self.lista[id] = aerolinea
        print("La aerolinea se agrego a la lista de aerolineas")
