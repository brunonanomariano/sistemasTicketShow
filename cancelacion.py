from globales import *;
from crearUsuario import *; 
import json;
from pantallas import *
from compras import *
from globales import *

def recuperar_comprobante(usuario, id):
    """
      Funcion     : recuperar_comprobante
      Descripcion : recupera un comprobante del archivo de comprobantes
      Entrada     : id comprobante
      Salida      : datos del comprobante 
    """
    compra_a_cancelar = {}

    if existe_archivo(archivo_comprobantes):
        with open(archivo_comprobantes, "r") as archivo:
            try:
                lista_comprobantes = json.load(archivo)
                comprobantes_usuario = filter(lambda comprobante: comprobante["usuario"] == usuario, lista_comprobantes)
                
                for comprobante in comprobantes_usuario:
                    if id == comprobante["idcompra"]:
                        compra_a_cancelar = comprobante

            except json.JSONDecodeError:
                print("Se genero un problema al obtener los comprobantes.")
                operacion_exitosa = False
    else:
        print("No se encontró archivo de comprobantes.")
        operacion_exitosa = False

    return compra_a_cancelar

def imprimir_cancelacion(usuario, comprobante_recuperado):
    """
      Funcion     : imprimir_cancelacion
      Descripcion : imprimi datos de cancelacion
      Entrada     : usuario, datos de cancelacion
      Salida      : - 
    """
    cancelaciones_screen(usuario)
    print(" Esta a punto de cancelar la siguiente compra: ")
    print()
    print (
    f"  -ID de compra: {comprobante_recuperado["idcompra"]} \n"   
    f"  -Artista: {comprobante_recuperado["artista"]}       \n" 
    f"  -Fecha: {comprobante_recuperado["fecha"]}           \n" 
    f"  -Ubicaciones: {comprobante_recuperado["ubicacion"]} \n"
    f"  -Precio total: ${comprobante_recuperado["preciotot"]:.2f} \n")    

def actualizar_comprobantes(usuario, id):
    """
      Funcion     : actualizar_comprobantes
      Descripcion : actualiza el estado de un comprobante segun el usuario y el id de compra
      Entrada     : usuario, id
      Salida      : - 
    """
    actualizar = False

    if existe_archivo(archivo_comprobantes):
        with open(archivo_comprobantes, "r") as archivo:
            try:
                lista_comprobantes = json.load(archivo)
                for comprobante in lista_comprobantes:
                        if comprobante["usuario"] == usuario and comprobante["idcompra"] == id:
                            comprobante["estado"] = "CANCELADO"
                            actualizar = True
            except json.JSONDecodeError:
                print("Error al acceder al archivo de comprobantes")
    else:
        print("Error al acceder al archivo de salas")

    try:
        if actualizar == True:
            with open(archivo_comprobantes, "w") as archivo:
                json.dump(lista_comprobantes, archivo, indent=4)
    except Exception as e:
        print(f" Error {e} al actualizar el archivo de comprobantes")
    
def procesar_cancelacion(usuario):
    """
      Funcion     : procesar_cancelacion
      Descripcion : cancelacion una compra perteneciente al usuario siempre que exista
      Entrada     : usuario
      Salida      : True (si la pudo cancelar), False (si no pudo cancelarla) 
    """
    cancelar = False

    cancelaciones_screen(usuario)
    id = input(" Por favor ingrese el ID de la compra para poder continuar: ")
    comprobante_recuperado = recuperar_comprobante(usuario, id)
    if comprobante_recuperado and comprobante_recuperado["estado"] == "APROBADO": 
        imprimir_cancelacion(usuario, comprobante_recuperado)
        
        respuesta=""
        while respuesta != "S" and respuesta != "N":
            imprimir_cancelacion(usuario, comprobante_recuperado)
            respuesta=input("Desea continuar con la cancelacion? (S/N): ").upper()

        if respuesta == "S":
            asientos = comprobante_recuperado["ubicacion"]
            sala = comprobante_recuperado["indiceSala"]
            marcar_asientos(asientos, sala, LIBRE)
            actualizar_comprobantes(usuario, id)
            print()
            print(f"La compra con el id {id} se ha cancelada exitosamente!")
            cancelar = True

    elif comprobante_recuperado and comprobante_recuperado["estado"] == "CANCELADO":
        print(f" La compra con id '{id}' ya se encuentra cancelada")
        print()
        cancelar = False
    else:
        print(f" No se encontro compra para el id: '{id}'")
        print()
        cancelar = False

    return cancelar
