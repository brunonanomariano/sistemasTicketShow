from re import match;


def separar_fila_asiento(coordenadas):
    """
        Funcion      : separar_fila_asiento
        Descripcion  : recibe una coordenada, y separa la fila y el asiento para devolverlos
        Entrada      : coordenadas
        Salida       : fila y asiento
    """
    fila = coordenadas[0:1].upper() 
    asiento = int(coordenadas[1:])-1

    return fila, asiento


def verificar_coordenadas(filas, asientos, coordenadas):
    """
        Funcion      : verificar_coordenadas
        Descripcion  : recibe un lista de filas y de asientos, y verifica que las coordenadas ingresadas sean validas
        Entrada      : filas, coordenadas
        Salida       : invalidez (True si las coordanadas no son validas, false si las coordenadas son validas)
    """
    patron = "^[a-zA-Z][0-9]{1,2}$"
    coincide = match(patron,coordenadas)

    if coincide:
        fila, asiento = separar_fila_asiento(coordenadas)

        if not(fila in filas) or not(asiento in asientos):
            print("Las coordenadas ingresadas no se encuentran en pantalla")
            invalidez = True
        else:
            invalidez = False
    else: 
        print("Las coordenadas ingresadas no poseen un formato valido")
        invalidez = True

    return invalidez


def elegir_lugares(filas,asientos,cant_tickets):
    """
        Funcion     : elegir_lugares
        Descripcion : se elige y valida una ubicacion ingresada por el usuario para que la misma se encuentre
                        dentro de las opciones disponibles
        Entrada     : filas(lista de filas validas), asientos (lista de asientos validos)
        Salida      : asiento_elegido, fila_elegida (ambos en valores enteros)
    """

    lista_fila=[]
    esta_compra=[]

    print(cant_tickets)

    while cant_tickets > 0:

        coordenada_incorrecta = True

        while coordenada_incorrecta:
            coordenadas = input("Ingrese las coordenadas que desea comprar, indicando primero la fila y luego el asiento:\n")
            coordenada_incorrecta = verificar_coordenadas(filas, asientos, coordenadas)

            if not(coordenada_incorrecta):
                if not(coordenadas in esta_compra):
                    esta_compra.append(coordenadas) #Guardo las coordenadas elegidas recien para validar duplicidad
                    fila_elegida, _ = separar_fila_asiento(coordenadas)
                    fila_elegida_numerica = ord(fila_elegida) - 65 #paso la fila de letra a numero para transformala a un indice
                    #Guardo una lista de filas que me servira para calcular el total de la compra
                    #ya que el precio de un asiento depende de su fila
                    lista_fila.append(fila_elegida_numerica)
                else:
                    print("Las cordenadas ya fueron elegidas en esta compra, por favor ingrese otra ubicacion disponible \n")
                    coordenada_incorrecta = True

        cant_tickets -=1

    return lista_fila, esta_compra