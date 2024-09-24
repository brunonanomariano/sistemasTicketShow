from salas import *;
from compras import *;
from pantallas import *;
from procesarPantallas import *;
from crearUsuario import *;
from login import *
import random;
from os import system

CANT_FILAS = 13
CANT_ASIENTOS = 10
PRECIO_DELANTERO = 55000

#filas_en_letras = enumerar_filas(CANT_FILAS)
#asientos = [elemento for elemento in range(CANT_ASIENTOS)]

#sala = crear_sala(CANT_ASIENTOS,CANT_FILAS)
#lista_precios = armar_lista_precios(CANT_FILAS, PRECIO_DELANTERO)
#lugares_disponibles = calcular_disponibilidad(sala)

#Limpio la pantalla
system("cls")

#Seleccion de ubicaciones
#selecionar_ubicacion_screen()
#imprimir_sala(sala, lista_precios, filas_en_letras, asientos)
#fila, asiento = elegir_lugares(filas_en_letras,asientos)


opcionElegida = 0 # Seteo opcion elegida en 0 para entrar al ciclo de pantallas
while opcionElegida != 3: #Si opcion elegida es 3 entonces termino el programa
    bienvenida_screen()
    opcionElegida = procesar_bienvenida()
    if opcionElegida == 1:
        crear_usuario_screen()
        crearUsuario()
    elif opcionElegida == 2:
        iniciar_sesion_screen()
        login_exitoso = logear_usuario()
        if login_exitoso:
            selecionar_shows_screen()
            listar_shows(lista_conciertos)
            input()
        else:
            pass


