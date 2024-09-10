##########################################################################################################################################
#  Funcion     : elegir_lugares
#  Descripcion : se elige y valida una ubicacion ingresada por el usuario para que la misma se encuentre
#                dentro de las opciones disponibles
#  Entrada     : filas(lista de filas validas), asientos (lista de asientos validos)
#  Salida      : asiento_elegido, fila_elegida (ambos en valores enteros)
##########################################################################################################################################
def elegir_lugares(filas,asientos):
    coordenada_incorrecta = True

    while coordenada_incorrecta:
        coordenadas = input("Ingrese las coordenadas que desea comprar, indicando primero la fila y luego el asiento:\n")

        #Separo las cordenadas recibidas en 2 cadenas, para luego poder aplicar los metodos de validacion
        #isalpha y isnumeric y asi validar que los valores ingresados sean los esperados
        fila  =""
        asiento =""
        fila += coordenadas[0].upper() #Lo seteo en mayuscula para poder comparar con la lista de filas
        asiento += coordenadas[1]

        #Valido que las coordenadas sean validas:
        #No pueden ser mas 2, ni estar vacias
        if len(coordenadas) > 2 or len(coordenadas) == 0:
            print("Las coordenadas ingresadas no son validas, debe tener solo dos valores")
        #La primera debe ser una letra y la segunda un numero
        elif not(fila.isalpha()) or not(asiento.isnumeric()):
            print("Las coordenadas ingresadas no son validas, el primer valor debe ser alfanumerico y el segundo numerico")
        #La fila y el asiento deben estar dentro de las listas de filas y asientos pasado por parametros
        elif not(fila in filas) or not(int(asiento) in asientos):
            print("Las coordenadas ingresadas no se encuentran en pantalla")
        else:
            coordenada_incorrecta = False

    #Transforo el asiento elegido al indice correspondiente, como en pantalla la primera posicion
    #se muestra como 1, debo restarle 1 ya que los indices arrancan desde 0 en la matriz sala
    asiento_elegido = int(asiento)-1

    #Transformo la fila elegida a un indice de la matriz sala, como "A" es 65 en ascii
    #entonces al pasarlo a valor en ascii debo restarla 65 para obtener el indice apartir de 0
    fila_elegida = ord(fila) - 65

    return asiento_elegido, fila_elegida