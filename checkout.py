from globales import *;
from compras import *;
import random;
from crearUsuario import *; 
from pantallas import *

def calcular_descuento(precio, descuento):
    """
    Función: calcular_descuento
    Descripción: Calcula el precio de una entrada aplicando un descuento.

    Entrada: Precio original de la entrada y porcentaje de descuento a aplicar (float o int).
    Salida: Precio final después de aplicar el descuento.
    """

    descuento_monto = precio * descuento
    
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
        print(" Cupón no válido. No se aplicó descuento.")
        return precio_total  # Si el cupón no es válido, no se aplica descuento




def procesar_pago(precio_total):
    """
    Nombre: procesar_pago
    Descripción: Procesa el pago de la compra utilizando tarjeta de crédito o débito.

    Entrada:El precio total a pagar.
    Salida: Un mensaje indicando si el pago fue exitoso o no.
    """
    print(f" El precio total de tu compra es: ${precio_total:.2f}.")

    tarjeta_valida = False
    while not tarjeta_valida:
        tarjeta = input(" Ingresa los datos de tu tarjeta (Número de tarjeta): ")

        if validar_tarjeta(tarjeta):
            tarjeta_valida = True  
        else:
            proceso_compra_screen()
            print(f" El precio total de tu compra es: ${precio_total:.2f}.")
            print(" La tarjeta tiene un formato inválido. Asegúrate de que solo contenga números y tenga entre 13 y 19 dígitos.")
    
    confirmacion_pago = ""
    while confirmacion_pago != "S" and confirmacion_pago != "N":
        proceso_compra_screen()
        print(f" El precio total de tu compra es: ${precio_total:.2f}.")
        print(f" Medio de pago utlizado: {tarjeta}")
        confirmacion_pago = input(" ¿Deseas confirmar el pago de esta compra? (S/N): ").upper()

    if confirmacion_pago == "S":
        print(f" Procesando el pago de ${precio_total:.2f}...")
        
        print("¡Pago procesado exitosamente! ¡Gracias por tu compra!")
        return True  
    else:
        print(" El pago ha sido cancelado. Vuelve cuando estés listo para completar la compra.")
        input(" Presione ENTER para poder continuar...")
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

def generar_comprobante(cantidad_entradas, precio_total, cupón_aplicado, ubicacion, usuario, nombreArtista, fecha, indiceSala):
    
    """
    Función: generar_comprobante
    Descripción: genera un comprobante a partir de la información de la compra

    Entrada: cantidad de entradas, precio total de la compra, cupón, usuario y sector (ubicación)
    Salida: arma el comprobante con los datos proporcionados.
    """
        
    # Genera un ID aleatorio para la compra
    id_compra = f"#{random.randint(10000000, 99999999)}"

    if cupón_aplicado:
        descuento = "Descuento aplicado"
    else:
        descuento = "No se aplico descuento"
    
    print("")
    comprobante = (
        f" ---------- COMPROBANTE DE COMPRA ---------\n"
        f" --- GRACIAS POR USAR SIST. TICKET SHOW ---\n"
        f"                                           \n"
        f"     Usuario: {usuario}                    \n"
        f"     Artista: {nombreArtista}              \n" 
        f"     Fecha: {fecha}                         \n" 
        f"     ID de compra: {id_compra}               \n"
        f"     Cantidad de entradas: {cantidad_entradas}\n"
        f"     Ubicación: {ubicacion}\n"
        f"     {descuento}\n"
        f"     Precio total: ${precio_total:.2f}\n"
        f"     Estado: APROBADO\n"
        f"                                            \n"
        f"--------------------------------------------"
    )

    print(comprobante)

    input("Presione ENTER para continuar")
    comprobante = {
                   "usuario": usuario, 
                   "artista": nombreArtista,
                   "fecha": fecha,
                   "idcompra": id_compra, 
                   "cantentradas": cantidad_entradas, 
                   "ubicacion": ubicacion,
                   "descuento": descuento, 
                   "preciotot": precio_total,
                   "estado": "APROBADO",
                   "indiceSala": indiceSala
                   }
    
    
    if existe_archivo(archivo_comprobantes):
        with open(archivo_comprobantes, "r") as archivo:
            try:
                lista_comprobantes = json.load(archivo)
            except json.JSONDecodeError:
                lista_comprobantes = []
    else:
        lista_comprobantes = []

    lista_comprobantes.append(comprobante)

    estado_operacion = True

    # Intento guardar los datos actualizados en el archivo
    try:
        with open(archivo_comprobantes, "w") as archivo:
            json.dump(lista_comprobantes, archivo, indent=4)
    except Exception as e:
        estado_operacion = False
    
    return estado_operacion 



def calcular_total_compra(filas_elegidas, lista_precios):
    """
      Funcion     : calcular_total_compra
      Descripcion : recibe las filas elegidas en una compra y calcula el precio en base al valor de la fila
      Entrada     : filas_elegidas(lista de filas seleccionadas), lista_precios
      Salida      : total (total de la compra calculado)
    """
    
    total=0

    for fila in filas_elegidas:
        total += lista_precios[fila]

    return total


def procesar_checkout(total_compra, lugares_elegidos):
    """
      Funcion     : procesar_checkout
      Descripcion : informa por pantalla el resumen de compra antes de proceder con el pago
      Entrada     : total_compra, lugares_elegidos
      Salida      : cupon (que puedo o no presentar el usuario)
    """
    print(" Asientos elegidos:" ,end="")
    for lugar in lugares_elegidos:
        print(" ",lugar, end="")
    print("")
    print(f" Total de la compra: ${total_compra}")
    print("")
    cupon = input(" Ingrese el cupon de descuento o presiones ENTER para continuar : ")

    reintentar = True

    if cupon !="":
        while reintentar:
            total_a_pagar = aplicar_descuento(cupon, total_compra, cupones_validos)
            if total_a_pagar == total_compra:
                respuesta = ""
                while respuesta != "S" and respuesta != "N":
                    checkout_screen()
                    print(" Asientos elegidos:" ,end="")
                    for lugar in lugares_elegidos:
                        print(" ",lugar, end="")
                    print("")
                    print(f" Total de la compra: ${total_compra}")
                    print("")
                    print(" Cupón no válido. No se aplicó descuento.")
                    respuesta = input(" Desea reingresar el codigo de descuento? (S/N)").upper()
                
                if respuesta == "S":
                    cupon = input(" Ingrese el cupon de descuento o presiones ENTER para continuar : ")
                    reintentar = True
                else:
                    reintentar = False

            else:
                print(f" Descuento aplicado, el nuevo subtotal es: ${total_a_pagar}")
                reintentar = False
    else:
        total_a_pagar = total_compra

    print("")
    input(" Presione ENTER para continuar con el proceso de pago")

    return total_a_pagar, cupon
