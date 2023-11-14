from aerolinea.aerolineaController import aerolineaController
from avion.avionController import avionController
from helicoptero.helicopteroController import helicopteroController
from jet.jetController import jetController
from pasajero.pasajeroController import pasajeroController
from puerta.puertaController import puertaController
from tripulacion.tripulacionController import tripulacionController
from vuelo.vueloController import vueloController


def main():
    aerolineaControl = aerolineaController()
    avionControl = avionController()
    helicopteroControl = helicopteroController()
    jetControl = jetController()
    pasajeroControl = pasajeroController()
    puertaControl = puertaController()
    tripulacionControl = tripulacionController()
    vueloControl = vueloController()

    print("Buen dia usuario")
    print("El presente sistema le permitira crear, consultar y modificar diferentes aspectos del aeropuerto")
    print("Recuerde que al crear un elemento en especifico su ID se asignara desde 1 y este aumentara si crea mas")
    while True:
        print("Con que vamos a trabajar el dia de hoy?")
        print("1. Aerolineas")
        print("2. Aviones")
        print("3. Helicopteros")
        print("4. Jets")
        print("5. Pasajeros")
        print("6. Puertas de embarque")
        print("7. Tripulacion")
        print("8. Vuelos")
        print("9. Salir")

        opcionPrincipal = input("Opcion: ")

        if opcionPrincipal == "1":
            while True:
                print("Que opcion desea utilizar?")
                print("1. Crear")
                print("2. Mostrar Todos")
                print("3. Actualizar")
                print("4. Salir")

                opcionGestionamiento = input("Opcion: ")

                if opcionGestionamiento == "1":
                    aerolineaControl.crearNuevaAerolinea()
                elif opcionGestionamiento == "2":
                    aerolineaControl.listaDeAerolineas()
                elif opcionGestionamiento == "3":
                    aerolineaControl.actualizarAerolinea()
                elif opcionGestionamiento == "4":
                    print("Volviendo al menu")
                    break
                else:
                    print("Opcion invalida, intente de nuevo")
        elif opcionPrincipal == "2":
            while True:
                print("Que opcion desea utilizar?")
                print("1. Crear")
                print("2. Mostrar Todos")
                print("3. Actualizar")
                print("4. Salir")

                opcionGestionamiento = input("Opcion: ")

                if opcionGestionamiento == "1":
                    avionControl.crearNuevoAvion()
                elif opcionGestionamiento == "2":
                    avionControl.listaDeAviones()
                elif opcionGestionamiento == "3":
                    avionControl.actualizarAvion()
                elif opcionGestionamiento == "4":
                    print("Volviendo al menu")
                    break
                else:
                    print("Opcion invalida, intente de nuevo")
        elif opcionPrincipal == "3":
            while True:
                print("Que opcion desea utilizar?")
                print("1. Crear")
                print("2. Mostrar Todos")
                print("3. Actualizar")
                print("4. Salir")

                opcionGestionamiento = input("Opcion: ")

                if opcionGestionamiento == "1":
                    helicopteroControl.crearNuevoHelicoptero()
                elif opcionGestionamiento == "2":
                    helicopteroControl.listaDeHelicopteros()
                elif opcionGestionamiento == "3":
                    helicopteroControl.actualizarHelicoptero()
                elif opcionGestionamiento == "4":
                    print("Volviendo al menu")
                    break
                else:
                    print("Opcion invalida, intente de nuevo")
        elif opcionPrincipal == "4":
            while True:
                print("Que opcion desea utilizar?")
                print("1. Crear")
                print("2. Mostrar Todos")
                print("3. Actualizar")
                print("4. Salir")

                opcionGestionamiento = input("Opcion: ")

                if opcionGestionamiento == "1":
                    jetControl.crearNuevoJet()
                elif opcionGestionamiento == "2":
                    jetControl.listaDeJets()
                elif opcionGestionamiento == "3":
                    jetControl.actualizarJet()
                elif opcionGestionamiento == "4":
                    print("Volviendo al menu")
                    break
                else:
                    print("Opcion invalida, intente de nuevo")
        elif opcionPrincipal == "5":
            while True:
                print("Que opcion desea utilizar?")
                print("1. Crear")
                print("2. Mostrar Todos")
                print("3. Actualizar")
                print("4. Salir")

                opcionGestionamiento = input("Opcion: ")

                if opcionGestionamiento == "1":
                    pasajeroControl.crearNuevoPasajero()
                elif opcionGestionamiento == "2":
                    pasajeroControl.listaDePasajeros()
                elif opcionGestionamiento == "3":
                    pasajeroControl.actualizarPasajero()
                elif opcionGestionamiento == "4":
                    print("Volviendo al menu")
                    break
                else:
                    print("Opcion invalida, intente de nuevo")
        elif opcionPrincipal == "6":
            while True:
                print("Que opcion desea utilizar?")
                print("1. Crear")
                print("2. Mostrar Todos")
                print("3. Actualizar")
                print("4. Salir")

                opcionGestionamiento = input("Opcion: ")

                if opcionGestionamiento == "1":
                    puertaControl.crearNuevaPuerta()
                elif opcionGestionamiento == "2":
                    puertaControl.listaDePuertas()
                elif opcionGestionamiento == "3":
                    puertaControl.actualizarPuerta()
                elif opcionGestionamiento == "4":
                    print("Volviendo al menu")
                    break
                else:
                    print("Opcion invalida, intente de nuevo")
        elif opcionPrincipal == "7":
            while True:
                print("Que opcion desea utilizar?")
                print("1. Crear")
                print("2. Mostrar Todos")
                print("3. Actualizar")
                print("4. Salir")

                opcionGestionamiento = input("Opcion: ")

                if opcionGestionamiento == "1":
                    tripulacionControl.crearNuevoTripulante()
                elif opcionGestionamiento == "2":
                    tripulacionControl.listaDeTripulacion()
                elif opcionGestionamiento == "3":
                    tripulacionControl.actualizarTripulacion()
                elif opcionGestionamiento == "4":
                    print("Volviendo al menu")
                    break
                else:
                    print("Opcion invalida, intente de nuevo")
        elif opcionPrincipal == "8":
            while True:
                print("Que opcion desea utilizar?")
                print("1. Crear")
                print("2. Mostrar Todos")
                print("3. Actualizar")
                print("4. Salir")

                opcionGestionamiento = input("Opcion: ")

                if opcionGestionamiento == "1":
                    vueloControl.crearNuevoVuelo()
                elif opcionGestionamiento == "2":
                    vueloControl.listaDeVuelos()
                elif opcionGestionamiento == "3":
                    vueloControl.actualizarVuelo()
                elif opcionGestionamiento == "4":
                    print("Volviendo al menu")
                    break
                else:
                    print("Opcion invalida, intente de nuevo")
        elif opcionPrincipal == "9":
            print("Hasta luego, tenga un buen dia")
            break
        else:
            print("Opcion invalida, intente de nuevo")


main()
