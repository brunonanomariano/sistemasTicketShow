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
    Función: aplicar_descuento
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
        print("Cupón no válido. No se aplicó descuento.")
        return precio_total  # Si el cupón no es válido, no se aplica descuento




def procesar_pago(precio_total):
    """
    Nombre: procesar_pago
    Descripción: Procesa el pago de la compra utilizando tarjeta de crédito o débito.

    Entrada:El precio total a pagar.
    Salida: Un mensaje indicando si el pago fue exitoso o no.
    """

    print(f"El precio total de tu compra es: {precio_total:.2f}.")

    tarjeta_valida = False
    while not tarjeta_valida:
        tarjeta = input("Ingresa los datos de tu tarjeta (Número de tarjeta): ")

        if validar_tarjeta(tarjeta):
            tarjeta_valida = True  
        else:
            print("La tarjeta tiene un formato inválido. Asegúrate de que solo contenga números y tenga entre 13 y 19 dígitos.")
            
            cancelar = input("¿Quieres cancelar el pago? (sí/no): ").lower()
            if cancelar == 'sí':
                print("El pago ha sido cancelado.")
                return False  

    confirmacion_pago = input("¿Deseas confirmar el pago de esta compra? (sí/no): ").lower()

    if confirmacion_pago == 'sí':
        print(f"Procesando el pago de {precio_total:.2f}...")
        
        print("¡Pago procesado exitosamente! ¡Gracias por tu compra!")
        return True  
    else:
        print("El pago ha sido cancelado. Vuelve cuando estés listo para completar la compra.")
        return False  



def validar_tarjeta(tarjeta):
    """
    Función: validar_tarjeta
    Descripción: Valida el formato de un número de tarjeta de crédito o débito.

    Entrada: el número de tarjeta ingresado.
    Salida: True si el formato es válido, False si no lo es.
    """

    if tarjeta.isdigit() and 13 <= len(tarjeta) <= 19:
        return True
    else:
        return False


import random
import string

def generar_comprobante(cantidad_entradas, precio_total, cupón_aplicado, ubicación):
    
    """
    Función: generar_comprobante
    Descripción: genera un comprobante a partir de la información de la compra

    Entrada: cantidad de entradas, precio total de la compra, cupón y sector (ubicación)
    Salida: arma el comprobante con los datos proporcionados.
    """
        
    # Genera un ID aleatorio para la compra
    id_compra = f"#{random.randint(10000000, 99999999)}"

    if cupón_aplicado:
        descuento = "Descuento aplicado"
    else:
        descuento = "No se aplicó descuento"
    
    comprobante = (
        f"---        COMPROBANTE DE COMPRA       ---\n"
        f"--- GRACIAS POR USAR SIST. TICKET SHOW ---\n"
        f"ID de compra: {id_compra}\n"
        f"Cantidad de entradas: {cantidad_entradas}\n"
        f"Ubicación: {ubicación}\n"
        f"{descuento}\n"
        f"Precio total: ${precio_total:.2f}\n"
        f"-------------------------------------------"
    )

    print(comprobante)
    return comprobante
