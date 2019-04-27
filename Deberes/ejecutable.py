import funciones as func

def main(opcion):
    while opcion != 0:
        print("\nMENU CAMPEONES:")
        print("1) Ingresar un campeon   x")
        print("2) Mostrar lista de campeones   x")
        print("3) Buscar campeon por nombre")
        print("4) Eliminar campeon")
        print("5) Actualizar campeon")
        print("\nMENU ITEMS:")
        print("6) Ingresar conjunto de items")
        print("7) Obtener conjuntos de items")
        print("8) Itemizar campeon\n")
        print("9) Mostrar lista campeones itemizados\n")
        print("0) Salir")
        leer = input("Ingrese una opción: ")
        if (leer.isnumeric()):
            opcion = int(leer)
        try:
            if(opcion == 1):
                print("*******************************")
                print("INGRESAR UN NUEVO CAMPEON")
                print("*******************************")
                func.agregar_camp()

            elif(opcion ==2):
                print("*******************************")
                print("MOSTRAR LISTA DE CAMPEONES")
                print("*******************************")
                func.mostrar_campeones()

            elif (opcion == 3):
                print("*******************************")
                print("BUSCAR CAMPEON POR NOMBRE")
                print("*******************************")
                nombre = input('Ingrese el nombre del campeon').upper()
                func.buscar_campeon(nombre)


            elif (opcion == 4):
                print("*******************************")
                print("ELIMINAR")
                print("*******************************")
                nombre = input('Ingrese el nombre del campeon').upper()
                func.eliminar_campeon(nombre)


            elif (opcion == 5):
                print("*******************************")
                print("ACTUALIZAR CAMPEON ")
                print("*******************************")
                nombre = input('Ingrese el nombre del campeon').upper()
                func.actualizar_campeon(nombre)


            elif (opcion == 6):
                print("*******************************")
                print("INGRESAR UN NUEVO CONJUNTO DE ITEMS")
                print("*******************************")
                func.agregar_items()

            elif (opcion == 7):
                print("*******************************")
                print("MOSTRAR LISTA DE ITEMS")
                print("*******************************")
                func.mostrar_items()
            elif (opcion == 8):
                func.agregar_itemizado()
            else:
                print("lo que sea")

        except TypeError:
            print(f'{opcion}')

main(-1)