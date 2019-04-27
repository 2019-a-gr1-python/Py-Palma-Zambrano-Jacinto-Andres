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
        'item_inicial': un_item[0],
        'item_core': un_item[1],
        'item_opcional':un_item[2]
    }
    return item

def textocampeones(campeones):
    return f"{campeones['nombre']};{campeones['rol']};{campeones['tipo']}"

def texto_items(items):
    return f"{items['item_principal']};{items['item_core']};{items['item_opcional']}"


def texto_campeonItemizado(campeonItemizado):
    return f"{campeonItemizado['nombre']};{campeonItemizado['rol']};" \
           f"{campeonItemizado['tipo']};{campeonItemizado['item_inicial']};" \
           f"{campeonItemizado['item_core']};{campeonItemizado['item_opcional']}"


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


#########################################################################################
#Funciones CRUD

#CREATE
def agregar_camp():
    print("Campeon Nuevo")
    nombre = input("Ingrese el nombre").upper
    rol = input("Ingrese el rol").upper()
    tipo = input("Ingrese el tipo de campeon:").upper()

    nuevo_campeon = nombre + ";" + rol + ";" + tipo

    escribir_archivo('./campeones.txt','a', nuevo_campeon)

def agregar_items():
    print("Conjunto Nuevo")
    item_inicial = input("Ingrese el nombre")
    item_core = input("Ingrese el nombre")
    item_opcional = input("Ingrese el nombre")

    nuevo_conjunto = item_inicial + ";" + item_core + ";" + item_opcional

    escribir_archivo('./items.txt','a', nuevo_conjunto)

def agregar_itemizado():
    campeones = llamar_campeones()
    items = llamar_items()

    for campeon in campeones:
       for item in items:
          if(campeon == 'SOPORTE'):
              nuevo = campeon + item
    print ('%(item_core)-30s' % item)





#READ
def mostrar_campeones():
    archivo = leer_archivo('./campeones.txt')
    campeones = []
    for campeon in archivo:
        campeones.append(diccionario_campeones(campeon))
    print('%-20s%-20s%-20s'%('Nombre','Rol','Tipo'))
    for champ in campeones:
        print('%(nombre)-20s%(rol)-20s%(tipo)-20s' % champ)

def mostrar_items():
    archivo = leer_archivo('./items.txt')
    items = []
    for item in archivo:
        items.append(diccionario_items(item))
    print('%-30s%-30s%-30s'%('Inicial','Core','Opcional'))
    for item in items:
        print('%(item_inicial)-30s%(item_core)-30s%(item_opcional)-30s' % item)

def mostrar_itemizados():
    archivo = leer_archivo('./campeonesItemizados.txt')
    itemizados = []
    for campeonI in archivo:
        itemizados.append(diccionario_items(campeonI))
    print('%-20s%-20s%-20s%-30s%-30s%-30s'%('Nombre','Rol','Tipo','Inicial','Core','Opcional'))
    for itemizado in itemizados:
        print('%(nombre)-20s%(rol)-20s%(tipo)-20s%(item_inicial)-30s%(item_core)-30s%(item_opcional)-30s' % itemizado)

#UPDATE
def buscar_campeon(nombre):
    campeones = llamar_campeones()
    champ = ""
    for campeon in campeones:
        if(campeon.get('nombre')==nombre):
            champ = campeon
            break
    else:
        campeones = None

    if campeones != None:
        print('%-20s%-20s%-20s' % ('Nombre', 'Rol', 'Tipo'))
        print('%(nombre)-20s%(rol)-20s%(tipo)-20s' % champ)
    else:
        print('El campeon: ' + nombre + ' no se encuentra registrado')



def actualizar_campeon(nombre):
    campeones = llamar_campeones()
    champ = ""
    for campeon in campeones:
        if (campeon.get('nombre') == nombre):
            champ = campeon
            break
    else:
        campeones = None

    if campeones != None:
        print('%-20s%-20s%-20s' % ('Nombre', 'Rol', 'Tipo'))
        print('%(nombre)-20s%(rol)-20s%(tipo)-20s' % champ)
        print('Ingrese los nuevos datos')
        nombre2 = input("Ingrese el nombre").upper()
        rol = input("Ingrese el rol").upper()
        tipo = input("Ingrese el tipo de campeon:").upper()
        campeon_actualizado = nombre2 + ";" + rol + ";" + tipo
    campeones1 = llamar_campeones()
    index = campeones1.index(campeones)
    campeones.update(campeon_actualizado)
    campeones1 [index] =campeones
    for champ1 in campeones1:
        fila = diccionario_campeones(champ1)
        campeones1.append(fila)
        escribir_archivo('./campeones.txt','w',campeones)


#DELETE
def eliminar_campeon(nombre):
    campeones = llamar_campeones()
    champ = ""
    for campeon in campeones:
        if (campeon.get('nombre') == nombre):
            champ = campeon
            print('%-20s%-20s%-20s' % ('Nombre', 'Rol', 'Tipo'))
            print('%(nombre)-20s%(rol)-20s%(tipo)-20s' % champ)
            break
    else:
        campeones = None

    if campeones != None:
        campeones.remove(champ)
    for campi in campeones:
        texto = textocampeones(campi)
    campeones_salida = []
    campeones_salida.append(texto)
    escribir_archivo('./campeones.txt','w',campeones_salida)


#Funciones Adicionales
def llamar_campeones():
    archivo = leer_archivo('./campeones.txt')
    campeones = []
    for campeon in archivo:
        campeones.append(diccionario_campeones(campeon))
    return campeones

def llamar_items():
    archivo = leer_archivo('./items.txt')
    items = []
    for item in archivo:
        items.append(diccionario_items(item))
    return items