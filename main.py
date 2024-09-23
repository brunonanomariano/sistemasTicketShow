from salas import *;
from compras import *;
from pantallas import *;
import random;
from os import system

CANT_FILAS = 13
CANT_ASIENTOS = 10
PRECIO_DELANTERO = 55000

filas_en_letras = enumerar_filas(CANT_FILAS)
asientos = [elemento for elemento in range(CANT_ASIENTOS)]

sala = crear_sala(CANT_ASIENTOS,CANT_FILAS)
lista_precios = armar_lista_precios(CANT_FILAS, PRECIO_DELANTERO)
lugares_disponibles = calcular_disponibilidad(sala)

#Limpio la pantalla
system("cls")

#Seleccion de ubicaciones
selecionar_ubicacion_screen()
imprimir_sala(sala, lista_precios, filas_en_letras, asientos)
fila, asiento = elegir_lugares(filas_en_letras,asientos)