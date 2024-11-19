from globales import *;
from crearUsuario import *; 
import json;



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
        print(
            f" ---------- COMPROBANTE DE COMPRA ---------\n"
            f" --- GRACIAS POR USAR SIST. TICKET SHOW ---\n"
            f"                                           \n"
            f"     Usuario: {comprobante['usuario']}     \n"  
            f"     ID de compra: {comprobante['idcompra']}\n"
            f"     Cantidad de entradas: {comprobante['cantentradas']}\n"
            f"     Ubicación: {comprobante['ubicacion']}\n"
            f"     {comprobante['descuento']}\n"
            f"     Precio total: ${comprobante['preciotot']:.2f}\n"
            f"                                            \n"
            f"--------------------------------------------"
        )



def filtrar_comprobantes(usuario, lista_comprobantes):
 
    """
    Funcion     : filtrar_comprobantes
    Descripcion : Filtra los comprobantes de compra de un usuario específico de una lista de comprobantes.
    Entrada     : El nombre del usuario cuyos comprobantes se quieren obtener.
                  Una lista de diccionarios donde cada diccionario representa un comprobante de compra.
    Salida      :  Una lista de diccionarios con los comprobantes que corresponden al usuario especificado.
    """

    comprobantes_filtrados = filter(lambda comprobante: comprobante["usuario"] == usuario, lista_comprobantes)
    
    return list(comprobantes_filtrados)


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
                comprobantes_usuario = filtrar_comprobantes(usuario, lista_comprobantes)
                imprimir_comprobantes(comprobantes_usuario)
            except json.JSONDecodeError:
                print("Se genero un problema al obtener los comprobantes.")
                operacion_exitosa = False
    else:
        print("No se encontró archivo de comprobantes.")
        operacion_exitosa = False


obtener_comprobantes("admin")