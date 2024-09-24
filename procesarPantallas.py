from globales import *;

##########################################################################################################################################
#  Funcion     : verificar_opcion
#  Descripcion : recibe una opcion y una lista de posibles opciones e informa si la opcione es correcta o no
#  Entrada     : opcion
#                lista_opciones
#  Salida      : False (si la opcion no esta en la lista de opciones)
#                True  (si la opcion esta en la lista de opciones)
#######################################################################################################AAA###################################
def verificar_opcion(opcion, lista_opciones):
    if opcion in lista_opciones:
        return True
    else:
        print("La opcion ingresada no esta disponible")
        return False
    

##########################################################################################################################################
#  Funcion     : procesar_bienvenida
#  Descripcion : procesa la primera pantalla espreando recibir una opcion correcta y devolviendo la opcion elegida en ese caso
#  Entrada     : -
#  Salida      : opcion (una opcion validad elegida por el usuario)
##########################################################################################################################################
def procesar_bienvenida():
    opcionCorrecta = False

    while opcionCorrecta == False:
        opcion = int(input("Por favor ingrese una opcion para continuar ----> "))
        opcionCorrecta = verificar_opcion(opcion, [1,2,3])

    return opcion


##########################################################################################################################################
#  Funcion     : procesar_seleccion_shows
#  Descripcion : procesa la pantalla de seleccion de shows
#  Entrada     : -
#  Salida      : opcion (una opcion validad elegida por el usuario)
##########################################################################################################################################
def procesar_seleccion_shows():

    cantidad_conciertos = len(lista_conciertos)
    
    #Armo la lista de opciones tomando el tamaño de la lista de conciertos, como la lista de opciones arranca desde 1
    #mi range va de 1 hasta el largo de la lista + 1
    lista_opciones = list(range(1,cantidad_conciertos+1))

    opcionCorrecta = False
    while opcionCorrecta == False:
        opcion = int(input("Ingrese el show al cual desea asistir ----> "))-1 #La opcion elegida en realidad es una anterior en mi lista de opciones
        opcionCorrecta = verificar_opcion(opcion, lista_opciones)
        if lista_conciertos[opcion]["disponibilidadAsientos"] == 0:
            opcionCorrecta = False
            print("El show al cual desea asistir se encuentra agotado, por favor seleccione otra fecha")

    return opcion


    

