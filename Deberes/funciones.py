#Lectura de archivos
def leer_archivo(ruta):
    try:
        filas = []
        archivo = open(ruta)
        archivoInterno = archivo.readlines()
        for fila in archivoInterno:
            filas.append(fila)
        archivo.close()
        return filas
    except Exception:
        print("El archivo no puede ser leido desde la ruta: " + ruta)


#Manipulación de datos
def diccionario_campeones(fila):
    un_campeon = (fila + "").replace("\n","").split(';')
    campeon = {
        'nombre': un_campeon[0],
        'rol': un_campeon[1],
        'tipo':un_campeon[2]
    }
    return campeon

def diccionario_items(fila):
    un_item = (fila + "").replace("\n","").split(';')
    item = {
        'item inicial': un_item[0],
        'item core': un_item[1],
        'item opcional':un_item[2]
    }
    return item

def texto_campeonItemizado(campeonItemizado):
    return f"{campeonItemizado['nombre']};{campeonItemizado['rol']};" \
           f"{campeonItemizado['tipo']};{campeonItemizado['item inicial']};" \
           f"{campeonItemizado['item core']};{campeonItemizado['item opcional']}"


#Escritura de archivos
def escribir_archivo(ruta, opcion, *campeones):
    try:
        archivo = open(ruta, opcion)
        for campeon in campeones:
            archivo.write(campeon + '\n')

        archivo.close()
        print('ESCRITURA COMPLETADA...')
    except Exception as exp:
        print(exp)

#Funciones CRUD

#CREATE
def agregar_camp():
    print("Campeon Nuevo")
    nombre = input("Ingrese el nombre")
    rol = input("Ingrese el rol").upper()
    tipo = input("Ingrese el tipo de campeon:").upper()

    nuevo_campeon = nombre + ";" + rol + ";" + tipo

    escribir_archivo('./campeones.txt','a', nuevo_campeon)

#READ
def mostrar_campeones():
    archivo = leer_archivo('./campeones.txt')
    campeones = []
    for campeon in archivo:
        campeones.append(diccionario_campeones(campeon))
    print()

#def mostrar_items():

#def mostrar_itemizados():
