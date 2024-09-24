from salas import *;
from compras import *;
from pantallas import *;
from procesarPantallas import *;
from crearUsuario import *;
from login import *
import random;
from os import system

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
            sala_elegida = procesar_seleccion_shows()

            #Una vez elegido el show comienzo a armar las claves para imprimir la sala
            sala = lista_conciertos[sala_elegida-1]["sala"]
            cant_filas = len(sala)
            precio_base = lista_conciertos[sala_elegida]["precioBase"]
            lista_precios = armar_lista_precios(cant_filas,precio_base,1000)
            fila_en_letras = enumerar_filas(sala)
            cant_asientos = len(sala[0])
            lista_asientos = list(range(cant_asientos))
            
            selecionar_ubicacion_screen()
            imprimir_sala(sala, lista_precios, fila_en_letras, lista_asientos)
            elegir_lugares(fila_en_letras,lista_asientos)
        else:
            pass


