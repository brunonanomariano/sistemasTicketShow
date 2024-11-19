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

def calcular_descuento(precio, descuento):
    """
    Función: calcular_descuento
    Descripción: Calcula el precio de una entrada aplicando un descuento.

    Entrada: Precio original de la entrada y porcentaje de descuento a aplicar (float o int).
    Salida: Precio final después de aplicar el descuento.
    """

    descuento_monto = precio * (descuento / 100)
    
    precio_final = precio - descuento_monto
    
    return precio_final



def aplicar_descuento(cupon_ingresado, precio_total, cupones_validos):
    """
    Descripción: calcula y aplica el descuento basado en el cupón ingresado.

    Entrada: código del cupón ingresado por el usuario, precio total de la compra, diccionario con los cupones válidos y sus respectivos descuentos.
    Salida: Precio total con el descuento aplicado, o el precio total si el cupón no es válido.
    """
    # Verificar si el cupón ingresado existe en el diccionario de cupones válidos
    if cupon_ingresado in cupones_validos:
        descuento = cupones_validos[cupon_ingresado]  # Obtener el porcentaje de descuento
        precioFinal = calcular_descuento(precio_total, descuento)
        return precioFinal
    else:
        print("Cupón no válido.")
        return precio_total  # Si el cupón no es válido, no se aplica descuento