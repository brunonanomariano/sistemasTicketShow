from salas import *;
from globales import *;
from compras import *;
from pantallas import *;
from procesarPantallas import *;
from crearUsuario import *;
from login import *
from checkout import *;
import random;
from comprobantes import *;
from cancelacion import *;
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
            login_exitoso, usuario = logear_usuario()
            if login_exitoso:
                opcion_menu_usuario = 0
                while opcion_menu_usuario != 4:
                    opciones_inicio_sesion(usuario)
                    opcion_menu_usuario = procesar_bienvenida_usuario(usuario)
                    if opcion_menu_usuario == 1:
                        selecionar_shows_screen()
                        listar_shows()
                        sala_elegida, cant_tickets, indice_sala = procesar_seleccion_shows()
                        if indice_sala != -1: #Recibir un -1 signfica que el usuario quiso volver hacia atras
                            cant_filas = len(sala_elegida["sala"])
                            precio_base = sala_elegida["precioBase"]
                            lista_precios = armar_lista_precios(cant_filas,precio_base,1000)
                            fila_en_letras = enumerar_filas(sala_elegida["sala"])
                            cant_asientos = len(sala_elegida["sala"][0])
                            lista_asientos = list(range(cant_asientos))

                            selecionar_ubicacion_screen()
                            imprimir_sala(sala_elegida["sala"], lista_precios, fila_en_letras, lista_asientos)
                            filas_elegidas, lugares_elegidos = elegir_lugares(fila_en_letras,lista_asientos, cant_tickets, sala_elegida, lista_precios)
                            checkout_screen()
                            total_compra = calcular_total_compra(filas_elegidas, lista_precios)
                            total_pagar, cupon_aplicado = procesar_checkout(total_compra, lugares_elegidos)
                            proceso_compra_screen()
                            resultado_operacion = procesar_pago(total_pagar)
                            if resultado_operacion == True:
                                marcar_asientos(lugares_elegidos, indice_sala, OCUPADO)
                                generar_comprobante(cant_tickets, total_pagar, cupon_aplicado, lugares_elegidos, usuario,sala_elegida["nombreArtista"],sala_elegida["fecha"], indice_sala)
                    elif opcion_menu_usuario == 2:
                        consultar_comprobantes_screen(usuario)
                        obtener_comprobantes(usuario)
                        input("Presione ENTER para volver al menu principal")
                    elif opcion_menu_usuario == 3:
                        procesar_cancelacion(usuario)
                        input("Presione ENTER para volver al menu principal")
            else:
                pass

main()


