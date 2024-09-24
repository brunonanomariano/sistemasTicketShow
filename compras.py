from re import match;

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

        #Verifico que las coordenadas tenga el formato letra + numero de uno o dos digitos
        patron = "^[a-zA-Z][0-9]{1,2}$"
        coincide = match(patron,coordenadas)

        #si hay match me separo la letra y el numero
        if coincide:
            fila = coordenadas[0:1].upper() #La letra la transformo a mayuscula para comparar con la lista de asientos en  mayuscula
            asiento = int(coordenadas[1:])-1
            #Verifico que las filas y los asientos se encuentren en la sala
            if not(fila in filas) or not(asiento in asientos):
                print("Las coordenadas ingresadas no se encuentran en pantalla")
                coordenada_incorrecta = True
            else:
                coordenada_incorrecta = False
        else: #Sino informo que se ingresaron mal
            print("Las coordenadas ingresadas no poseen un formato valido")
            coordenada_incorrecta = True

    #Transforo el asiento elegido al indice correspondiente, como en pantalla la primera posicion
    #se muestra como 1, debo restarle 1 ya que los indices arrancan desde 0 en la matriz sala
    asiento_elegido = asiento

    #Transformo la fila elegida a un indice de la matriz sala, como "A" es 65 en ascii
    #entonces al pasarlo a valor en ascii debo restarla 65 para obtener el indice apartir de 0
    fila_elegida = ord(fila) - 65

    return asiento_elegido, fila_elegida