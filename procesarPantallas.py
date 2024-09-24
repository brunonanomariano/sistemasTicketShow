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
#######################################################################################################AAA###################################
def procesar_bienvenida():
    opcionCorrecta = False

    while opcionCorrecta == False:
        opcion = int(input("Por favor ingrese una opcion para continuar ----> "))
        opcionCorrecta = verificar_opcion(opcion, [1,2,3])

    return opcion


    

