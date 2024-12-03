from os import system

def bienvenida_screen():
    system("cls")
    print("**************************************************************************************")
    print("                                                                                      ")
    print("              ▂▃▄▅▆▇█▓▒░ SISTEMAS TICKET SHOW ░▒▓█▇▆▅▄▃▂                      ")
    print("                                                                                      ")
    print("**************************************************************************************")
    print("                                                                                      ")
    print("   Bienvenido a SISTEMAS TICKET SHOW                                                  ")
    print("                                                                                      ")
    print("                                                                                      ")
    print("   Por favor para continuar seleccione una opcion:                                    ")
    print("                                                                                      ")
    print("                                                                                      ")
    print("   1- Crear usuario                                                                   ")
    print("   2- Iniciar sesion                                                                  ")
    print("   3- Salir                                                                           ")
    print("                                                                                      ")
    print("                                                                                      ")

def crear_usuario_screen():
    system("cls")
    print("**************************************************************************************")
    print("                                                                                      ")
    print("              ▂▃▄▅▆▇█▓▒░ SISTEMAS TICKET SHOW ░▒▓█▇▆▅▄▃▂                      ")
    print("                                                                                      ")
    print("                                CREAR USUARIO                                         ")
    print("                                                                                      ")
    print("**************************************************************************************")
    print("                                                                                      ")
    print("   Por favor a continuacion brinde un correo electronico y una contraseña             ")
    print("   O presiones ENTER para volver al menu principal                                    ")
    print("                                                                                      ")
    print("   La contraseña debe estar formada por:                                              ")
    print("     - 8 caracteres                                                                   ")
    print("     - La primer letra mayuscula                                                      ")
    print("     - Al menos 1 caracter numerico                                                   ")
    print("     - Al menos 1 caracter especial (# & _ ! %)                                       ")
    print("                                                                                      ")
    print("                                                                                      ")


def selecionar_ubicacion_screen():
    system("cls")
    print("***********************************************************************************************************")
    print("                                                                                      ")
    print("                             ▂▃▄▅▆▇█▓▒░ SISTEMAS TICKET SHOW ░▒▓█▇▆▅▄▃▂                      ")
    print("                                                                                      ")
    print("                                      SELECCION DE UBICACIONES                                  ")
    print("                                                                                      ")
    print("***********************************************************************************************************")
    print("                                                                                      ")
    print("   ╔════════════════════════════════════════════════════════════════════════════════════════════════════╗     ")
    print("                                S        T        A        G        E                                       ")
    print("   ╚════════════════════════════════════════════════════════════════════════════════════════════════════╝     ")
    print("                                                                                      ")
    print("                                                                                      ")


def iniciar_sesion_screen():
    system("cls")
    print("**************************************************************************************")
    print("                                                                                      ")
    print("              ▂▃▄▅▆▇█▓▒░ SISTEMAS TICKET SHOW ░▒▓█▇▆▅▄▃▂                      ")
    print("                                                                                      ")
    print("                                INICIAR SESION                                        ")
    print("                                                                                      ")
    print("**************************************************************************************")
    print("                                                                                      ")
    print("   Por favor ingrese usuario y contraseña para operar                                 ")
    print("                                                                                      ")
    print("   Tenga en cuenta que 3 ingresos erroneos de usuario o contraseña lo devolvera       ")
    print("   al menu principal                                                                  ")
    print("                                                                                      ")
    print("                                                                                      ")

def selecionar_shows_screen():
    system("cls")
    print("**************************************************************************************")
    print("                                                                                      ")
    print("              ▂▃▄▅▆▇█▓▒░ SISTEMAS TICKET SHOW ░▒▓█▇▆▅▄▃▂                      ")
    print("                                                                                      ")
    print("                              SELECCION DE SHOW                                       ")
    print("                                                                                      ")
    print("**************************************************************************************")
    print("                                                                                      ")
    print("  Seleccione el show al cual desea asistir:                                           ")
    print("                                                                                      ")
    print("                                                                                      ")

def checkout_screen():
    system("cls")
    print("**************************************************************************************")
    print("                                                                                      ")
    print("              ▂▃▄▅▆▇█▓▒░ SISTEMAS TICKET SHOW ░▒▓█▇▆▅▄▃▂                      ")
    print("                                                                                      ")
    print("                                 CHECKOUT                                             ")
    print("                                                                                      ")
    print("**************************************************************************************")
    print("                                                                                      ")
    print("  Resumen de compra:                                                                  ")
    print("                                                                                      ")
    print("                                                                                      ")

def proceso_compra_screen():
    system("cls")
    print("**************************************************************************************")
    print("                                                                                      ")
    print("              ▂▃▄▅▆▇█▓▒░ SISTEMAS TICKET SHOW ░▒▓█▇▆▅▄▃▂                      ")
    print("                                                                                      ")
    print("                              PROCESO DE COMPRA                                       ")
    print("                                                                                      ")
    print("**************************************************************************************")
    print("                                                                                      ")
    print("  Por favor ingrese el numero de su tarjeta de credito / debito                       ")
    print("                                                                                      ")
    print("                                                                                      ")


def opciones_inicio_sesion(usuario):
    system("cls")
    print("**************************************************************************************")
    print("                                                                                      ")
    print("              ▂▃▄▅▆▇█▓▒░ SISTEMAS TICKET SHOW ░▒▓█▇▆▅▄▃▂                      ")
    print("                                                                                      ")
    print("                               MENU DE USUARIO                                        ")
    print("                                                                                      ")
    print("**************************************************************************************")
    print("                                                                                      ")
    print(f"  Bienvenido {usuario}:                                                               ")
    print("   Elija la opcion deseada                                                            ") 
    print("                                                                                      ")
    print("   1- Comprar entradas                                                                ")
    print("   2- Consultar comprobantes                                                          ")
    print("   3- Cancelar compra                                                                 ")
    print("   4- Salir                                                                           ")
    print("                                                                                      ") 

def consultar_comprobantes_screen(usuario):
    system("cls")
    print("**************************************************************************************")
    print("                                                                                      ")
    print("              ▂▃▄▅▆▇█▓▒░ SISTEMAS TICKET SHOW ░▒▓█▇▆▅▄▃▂                      ")
    print("                                                                                      ")
    print("                              MIS COMPROBANTES                                        ")
    print("                                                                                      ")
    print("**************************************************************************************")
    print("                                                                                      ")
    print(f"  Bienvenido {usuario}:                                                               ")
    print("                                                                                      ")
    print("   A continuacion se detallan las compras realizadas                                  ") 
    print("                                                                                      ")
    print("                                                                                      ")


def cancelaciones_screen(usuario):
    system("cls")
    print("**************************************************************************************")
    print("                                                                                      ")
    print("              ▂▃▄▅▆▇█▓▒░ SISTEMAS TICKET SHOW ░▒▓█▇▆▅▄▃▂                      ")
    print("                                                                                      ")
    print("                              CANCELACIONES                                           ")
    print("                                                                                      ")
    print("**************************************************************************************")
    print("                                                                                      ")
    print(f"  Bienvenido {usuario}:                                                               ")
    print("                                                                                      ") 
    print("                                                                                      ")   