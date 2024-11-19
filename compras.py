from re import match;


def elegir_lugares(filas,asientos):
    """
        Funcion     : elegir_lugares
        Descripcion : se elige y valida una ubicacion ingresada por el usuario para que la misma se encuentre
                        dentro de las opciones disponibles
        Entrada     : filas(lista de filas validas), asientos (lista de asientos validos)
        Salida      : asiento_elegido, fila_elegida (ambos en valores enteros)
    """
    coordenada_incorrecta = True

    while coordenada_incorrecta:
        coordenadas = input("Ingrese las coordenadas que desea comprar, indicando primero la fila y luego el asiento:\n")

        patron = "^[a-zA-Z][0-9]{1,2}$"
        coincide = match(patron,coordenadas)

        if coincide:
            fila = coordenadas[0:1].upper() 
            asiento = int(coordenadas[1:])-1

            if not(fila in filas) or not(asiento in asientos):
                print("Las coordenadas ingresadas no se encuentran en pantalla")
                coordenada_incorrecta = True
            else:
                coordenada_incorrecta = False
        else: 
            print("Las coordenadas ingresadas no poseen un formato valido")
            coordenada_incorrecta = True

    asiento_elegido = asiento

    fila_elegida = ord(fila) - 65

    return asiento_elegido, fila_elegida