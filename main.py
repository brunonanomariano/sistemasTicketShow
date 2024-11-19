from salas import *;
from compras import *;
from pantallas import *;
from procesarPantallas import *;
from crearUsuario import *;
from login import *
from checkout import *;
import random;
from os import system

def limpiar_pantalla():
    system("cls")


def main():
    #grabar_salas()
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
                listar_shows()
                sala_elegida, cant_tickets, indice_sala = procesar_seleccion_shows()
                cant_filas = len(sala_elegida["sala"])
                precio_base = sala_elegida["precioBase"]
                lista_precios = armar_lista_precios(cant_filas,precio_base,1000)
                fila_en_letras = enumerar_filas(sala_elegida["sala"])
                cant_asientos = len(sala_elegida["sala"][0])
                lista_asientos = list(range(cant_asientos))

                selecionar_ubicacion_screen()
                imprimir_sala(sala_elegida["sala"], lista_precios, fila_en_letras, lista_asientos)
                filas_elegidas, lugares_elegidos = elegir_lugares(fila_en_letras,lista_asientos, cant_tickets, sala_elegida)
                checkout_screen()
                total_compra = calcular_total_compra(filas_elegidas, lista_precios)
                total_pagar, cupon_aplicado = procesar_checkout(total_compra, lugares_elegidos)
                proceso_compra_screen()
                resultado_operacion = procesar_pago(total_pagar)
                if resultado_operacion == True:
                    marcar_asientos_ocupados(lugares_elegidos, indice_sala)
                    generar_comprobante(cant_tickets, total_pagar, cupon_aplicado, lugares_elegidos)
                input()
            else:
                pass

main()


