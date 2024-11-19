from salas import *;
from compras import *;
from pantallas import *;
from procesarPantallas import *;
from crearUsuario import *;
from login import *
import random;
from os import system

def limpiar_pantalla():
    system("cls")


def main():
    opcionElegida = 0 
    while opcionElegida != 3: 
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
                sala_elegida, cant_tickets = procesar_seleccion_shows()

                sala = lista_conciertos[sala_elegida]["sala"]
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

main()


