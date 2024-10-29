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


    for fila in sala:
        cant_en_fila = reduce(lambda asiento1, asiento2: asiento1 + asiento2, fila)
        total_disponibles += cant_en_fila
    
    return total_disponibles


##########################################################################################################################################
#  Funcion     : enumerar_filas
#  Descripcion : transforma una lista de filas expresadas en numeros a una lista de filas expresadas en letras 
#  Entrada     : sala (matriz de la cual obtendra la cantidad de filas)
#  Salida      : filas_en_letras (la lista de filas expresadas en letras A,B,C,D,....)
##########################################################################################################################################
def enumerar_filas(sala):

    cant_filas = len(sala)

 
    fila_en_numeros = [indice for indice in range (cant_filas)]

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
    
    indice = 0

    for fila in sala:
        print(fila_en_letras[indice], "| ", end= " ")        
        
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
#  Descripcion : genera una lista de precios, partiendo desde un precio base y aumentando de acuerdo a un incremento X
#  Entrada     : cant_filas
#                precioBase (es el precio de la ultima fila)
#                incremento (es el precio con el que ira aumentando a medida que avancen las filas)
#  Salida      : lista_precios (es la lista que contiene los precios de cada fila, siendo la primera fila la mas cara)
##########################################################################################################################################
def armar_lista_precios(cant_filas, precioBase, incremento):

    lista_precios = []
   
    lista_precios.append(precioBase)

    precio_fila = precioBase
   
    for _ in range(cant_filas - 1):
        precio_fila = precio_fila + incremento
        lista_precios.append(precio_fila)

    lista_precios = lista_precios[::-1]

    return lista_precios

##########################################################################################################################################
#  Funcion     : listar_shows
#  Descripcion : recibe una lista de show y lista las caracteristicas del mismo
#  Entrada     : lista_shows (la lista de shows cargados en sistema)
##########################################################################################################################################
def listar_shows(lista_shows):
    i = 0 
    for show in lista_shows:
        i += 1 
        print("                                               ____________________________________")
        print(f"""                                              | Artista: {show["nombreArtista"]}
                                          {i}   | Fecha: {show["fecha"]} 
                                              | Lugares disponibles: {show["disponibilidadAsientos"]}
                                              | Precios desde: ${show["precioBase"]} """)
        print("                                               ------------------------------------")