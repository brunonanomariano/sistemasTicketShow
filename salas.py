from functools import reduce;
import random

##########################################################################################################################################
#  Funcion     : crear_sala
#  Descripcion : crea una sala con la cantidad de asientos y filas especificadas, el valor de cada asientos es un valor
#                de 0 o 1 (0 = asiento ocupado, 1 = asiento disponible)
#  Entrada     : cant_asientos, cant_filas
#  Salida      : sala (matriz creada con la cantidad de asientos y filas recibidas)
##########################################################################################################################################
def crear_sala(cant_asientos, cant_filas):
    sala = []
    for _ in range(cant_filas):
        #creo las filas con elmentos al azar de 0 y 1 (ocupado y libre)
        fila = [random.randint(0,1) for _ in range (cant_asientos)]
        sala.append(fila)
    
    return sala

##########################################################################################################################################
#  Funcion     : calcular_disponibilidad
#  Descripcion : calcula la cantidad de lugares disponibles de una sala basandose en el estado del asiento (1 = disponibles, 0 = ocupado)
#  Entrada     : sala
#  Salida      : cant_lugares (cantidad de lugares disponibles)
##########################################################################################################################################
def calcular_disponibilidad(sala):
    
    total_disponibles = 0

    #Como los asientos disponibles se representan con 1 y los ocupados con 0,
    #entonces reduzco cada fila a una suma de unos y ceros que da como resultado la cantidad disponible
    #y por cada fila acumulo este calculo
    for fila in sala:
        cant_en_fila = reduce(lambda asiento1, asiento2: asiento1 + asiento2, fila)
        total_disponibles += cant_en_fila
    
    return total_disponibles


##########################################################################################################################################
#  Funcion     : enumerar_filas
#  Descripcion : transforma una lista de filas expresadas en numeros a una lista de filas expresadas en letras 
#  Entrada     : cant_filas
#  Salida      : filas_en_letras (la lista de filas expresadas en letras A,B,C,D,....)
##########################################################################################################################################
def enumerar_filas(cant_filas):

    #armo la lista de filas (expresada con indices numericos 0,1,2,3....)
    fila_en_numeros = [indice for indice in range (cant_filas)]

    #transformo la lista de filas numericas a lista de filas alphanumericas
    #teniendo en cuenta que el caracter "A" en ascii es 65, por lo tanto
    # 0 + 65 = "A", 1 + 65 = "B", 2 + 65 = "C", ......
    obj_fila_en_letras = map(lambda numero: chr(numero+65), fila_en_numeros)

    fila_en_letras = list(obj_fila_en_letras)
    
    return fila_en_letras


##########################################################################################################################################
#  Funcion     : imprimir_sala
#  Descripcion : imprimi de una forma visual con coordenadas una sala 
#  Entrada     : sala
#                lista_precios
#                fila_en_letras (lista que contiene las filas en formato letras A,B,C,D....)
#                asientos (lista que contiene la posicion de los asientos)
##########################################################################################################################################
def imprimir_sala(sala, lista_precios, fila_en_letras, asientos):

    print(" " * (4), end=" ")
    print("_" * (76))

    for posicion in asientos:
        print(" " * 4, str(posicion+1), end=" ")
    print()    
    print(" " * (4), end=" ")
    print("_" * (76))
    
    #Genero un indice moverme entre la lista de precios y la lista que contiene las filas en formato de letras
    indice = 0

    for fila in sala:
        print(fila_en_letras[indice], "| ", end= " ")        
        
        #Imprimo el asiento con valores X (ocupado) y O (libre)
        for asiento in fila:
            if asiento == 1:
                estado_asiento = "O"
            else:
                estado_asiento = "X"

            print(estado_asiento, " " * 4, end= " ")
        
        print("--> $",lista_precios[indice])

        indice += 1

    print("")
    print("**************************************************************************************")
    print()

##########################################################################################################################################
#  Funcion     : armar_lista_precios
#  Descripcion : genera una lista de precios dependiendo de la cantidad de filas que hay en la sala, a medida
#                que avanzas las filas los precios van disminuyendo 
#  Entrada     : cant_filas
#                mayorPrecio (es el precio con el que se seteara la primera fila, el resto ira disminuyendo $2000)
##########################################################################################################################################
def armar_lista_precios(cant_filas, mayorPrecio):

    lista_precios = []

    #Seteo en la primera fila el mayor precio recibido por parametro    
    lista_precios.append(mayorPrecio)

    precio_fila = mayorPrecio

    #Agrego los siguientes precios a la lista, resto 1 porque el primero ya lo agregue
    #el resto de los precios que se van agregando van disminuyendo a medida que avanzas las filas    
    for _ in range(cant_filas - 1):
        precio_fila = precio_fila - 2000
        lista_precios.append(precio_fila)

    return lista_precios
    
