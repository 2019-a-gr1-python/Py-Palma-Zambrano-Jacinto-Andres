import funciones as func

def main(opcion):
    while opcion != 0:
        print("\nMENU CAMPEONES:")
        print("1) Ingresar un campeon")
        print("2) Mostrar lista de campeones")
        print("3) Buscar campeon")
        print("4) Eliminar campeon")
        print("5) Actualizar campeon")
        print("\nMENU ITEMS:")
        print("6) Ingresar conjunto de items")
        print("7) Obtener conjuntos de items")
        print("8) Itemizar campeon\n")
        print("8) Mostrar lista campeones itemizados\n")
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
                print("esta es la opcion 2")

            elif (opcion == 4):
                print("esta es la opcion 2")
            elif (opcion == 5):
                print("esta es la opcion 2")
            elif (opcion == 6):
                print("esta es la opcion 2")
            elif (opcion == 7):
                print("esta es la opcion 2")
            elif (opcion == 8):
                print("esta es la opcion 2")
            else:
                print("lo que sea")

        except TypeError:
            print(f'Option {option}')

main(-1)