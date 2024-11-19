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
    cupon = input("Si ud posee algun cupon de descuento por favor ingreselo a continuacion o presione enter para contiunar: ")

    return cupon