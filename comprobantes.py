from globales import *;
from crearUsuario import *; 
import json;
from colorama import init, Fore, Back, Style

init(autoreset=True)


def imprimir_comprobantes(lista_comprobantes):
    """
    Funcion     : imprimir_comprobantes
    Descripcion : Imprime los detalles de los comprobantes de compra de una lista de comprobantes.
    Entrada     : Una lista de diccionarios donde cada diccionario representa un comprobante de compra.
    Salida      : None
    Notas        : 
        - Si la lista de comprobantes está vacía, no se imprime nada.
        - La función imprime el formato de un comprobante con información del usuario, la compra y el precio.
    """
       
    for comprobante in lista_comprobantes:

        print("")
        print("")
        if comprobante["estado"] == "APROBADO":
            print(
                f" {Fore.LIGHTCYAN_EX}---------- COMPROBANTE DE COMPRA ---------\n"
                f" --- GRACIAS POR USAR SIST. TICKET SHOW ---{Style.RESET_ALL}\n"
                f"                                           \n"
                f"     {Fore.BLUE}Usuario:{Style.RESET_ALL} {Style.BRIGHT}{comprobante['usuario']}{Style.RESET_ALL}     \n"  
                f"     {Fore.BLUE}Artista:{Style.RESET_ALL} {Style.BRIGHT}{comprobante['artista']}{Style.RESET_ALL} \n"
                f"     {Fore.BLUE}Fecha:{Style.RESET_ALL} {Style.BRIGHT}{comprobante['fecha']}{Style.RESET_ALL}           \n"
                f"     {Fore.BLUE}ID de compra:{Style.RESET_ALL} {Fore.MAGENTA}{comprobante['idcompra']}\n"
                f"     {Fore.BLUE}Cantidad de entradas:{Style.RESET_ALL} {comprobante['cantentradas']}\n"
                f"     {Fore.BLUE}Ubicación:{Style.RESET_ALL} {comprobante['ubicacion']}\n"
                f"     {comprobante['descuento']}\n"
                f"     {Fore.BLUE}Precio total:{Style.RESET_ALL} {Style.BRIGHT}${comprobante['preciotot']:.2f}{Style.RESET_ALL}\n"
                f"     {Fore.BLUE}Estado:{Style.RESET_ALL} {Fore.GREEN}{comprobante['estado']}{Style.RESET_ALL}       \n"
                f"                                            \n"
                f"{Fore.LIGHTCYAN_EX}--------------------------------------------{Style.RESET_ALL}"
            )
        else:
            print(
                f" {Fore.LIGHTCYAN_EX}---------- COMPROBANTE DE COMPRA ---------\n"
                f" --- GRACIAS POR USAR SIST. TICKET SHOW ---{Style.RESET_ALL}\n"
                f"                                           \n"
                f"     {Fore.BLUE}Usuario:{Style.RESET_ALL} {comprobante['usuario']}     \n"  
                f"     {Fore.BLUE}Artista:{Style.RESET_ALL} {comprobante['artista']} \n"
                f"     {Fore.BLUE}Fecha:{Style.RESET_ALL} {comprobante['fecha']}           \n"
                f"     {Fore.BLUE}ID de compra:{Style.RESET_ALL} {Fore.MAGENTA}{comprobante['idcompra']}\n"
                f"     {Fore.BLUE}Cantidad de entradas:{Style.RESET_ALL} {comprobante['cantentradas']}\n"
                f"     {Fore.BLUE}Ubicación:{Style.RESET_ALL} {comprobante['ubicacion']}\n"
                f"     {comprobante['descuento']}\n"
                f"     {Fore.BLUE}Precio total:{Style.RESET_ALL} - \n"
                f"     {Fore.BLUE}Estado:{Style.RESET_ALL} {Fore.RED}{comprobante['estado']}{Style.RESET_ALL}       \n"
                f"                                            \n"
                f"{Fore.LIGHTCYAN_EX}--------------------------------------------{Style.RESET_ALL}"
            )




def obtener_comprobantes(usuario):

    """
    Funcion     : obtener_comprobantes
    Descripcion : Obtiene los comprobantes de un usuario desde un archivo JSON y los imprime.
    Entrada     : El nombre del usuario cuyos comprobantes se desean obtener.
    Salida      : None
    Notas        : Si el archivo de comprobantes no existe o no se puede leer, se imprime un mensaje de error.
                   En caso de un error en el formato del archivo JSON, también se imprime un mensaje de error.
    """
        
    if existe_archivo(archivo_comprobantes):
        with open(archivo_comprobantes, "r") as archivo:
            try:
                lista_comprobantes = json.load(archivo)
                comprobantes_usuario = filter(lambda comprobante: comprobante["usuario"] == usuario, lista_comprobantes)
                imprimir_comprobantes(comprobantes_usuario)
            except json.JSONDecodeError:
                print(f"{Fore.RED}Se genero un problema al obtener los comprobantes.")
                operacion_exitosa = False
    else:
        print(f"{Fore.RED}No se encontró archivo de comprobantes.")
        operacion_exitosa = False