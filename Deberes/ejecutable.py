import funciones as func

def main(opcion):
    while opcion != 0:
        print("\nMENU PRINCIPALM:")
        print("1) Ingresar un campeon")
        print("2) Obtener lista de campeones")
        print("3) Buscar campeon")
        print("4) Eliminar campeon")
        print("5) Actualizar campeon")
        print("0) Salir")
        leer = input("Ingrese una opción: ")
        if (leer.isnumeric()):
            opcion = int(leer)
        try:
            if(opcion == 1):
                print("*******************************")
                print("INGRESAR UN NUEVO CAMPEON")
                print("*******************************")
                func.leer_archivo('./campeones.txt')


            elif(opcion ==2):
                print("esta es la opcion 2")
            else:
                print("lo que sea")

        except TypeError:
            print(f'Option {option}')

main(-1)