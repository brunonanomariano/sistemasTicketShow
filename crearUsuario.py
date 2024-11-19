from re import match, search
from globales import *
import json
import os

def existe_archivo(archivo):
    """"
      Funcion     : verificar_existencia_archivo
      Descripcion : informa si un archivo existe o no
      Entrada     : archivo
      Salida      : True (si el archivo existe)
                    False (si el archivo no existe)
    """
    if os.path.exists(archivo):
        return True
    else:
        return False
    
def guardar_usuario(usuario, password, archivo_usr):
    """"
      Funcion     : guardar_usuario
      Descripcion : graba un usuario en el archivo recibido como parametro 
      Entrada     : usuario, password, archivo de usuarios
      Salida      : True (si la grabacion fue exitosa)
                    False (si la grabacion no pudo ser realizada)
    """

    nuevo_usuario = {"user": usuario, "password": password}
    
    # Obtengo los datos del archivo si existe o trabajo desde cero
    if existe_archivo(archivo_usr):
        with open(archivo_usr, "r") as archivo:
            try:
                usuarios = json.load(archivo)
            except json.JSONDecodeError:
                usuarios = []
    else:
        usuarios = []
    
    # Agrego el nuevo usuario
    usuarios.append(nuevo_usuario)

    estado_operacion = True

    # Intento guardar los datos actualizados en el archivo
    try:
        with open(archivo_usr, "w") as archivo:
            json.dump(usuarios, archivo, indent=4)
    except Exception as e:
        estado_operacion = False
    
    return estado_operacion



def existeUsuario (usuario, archivo_user): 
    """"
      Funcion     : existeUsuario
      Descripcion : verifica si un usuario existe en el archivo de usuarios 
      Entrada     : usuario, archivo de usuarios
      Salida      : True (si usuario ya existe en el archivo)
                    False (si el usuario no existe en el archivo)
    """

    if existe_archivo(archivo_user):
        try:
            with open(archivo_user, "r") as archivo:
                usuarios = json.load(archivo)
        except json.JSONDecodeError:
            return False

        # Buscar el usuario en la lista
        for usuarioCargado in usuarios:
            if usuarioCargado["user"] == usuario:
                return True
            else:
                return False
    else:
        return False



def validarEmail (email):  
    """
      Funcion     : validarEmail
      Descripcion : recibe un email y valida el formato. 
      Entrada     : email
      Salida      : none (no hay coincidencia en el patrón) u objeto coincidencia (hay match del email con el patrón)
    """

    patron = "[0-9a-z_-]+@[a-z]+.com" 
    resultado = match(patron, email) 
                                   
    return resultado  



def validarPassword(password):
    """
      Funcion     : validarPassword
      Descripcion : recibe un password y valida el formato. 
      Entrada     : password
      Salida      : True: la clave es valida o False: la clave es invalida.
    """   
    patron = "[A-Z][a-zA-Z0-9#&_!%]{7}"  
                                    
    resultado = match(patron, password) 
    
    if resultado: 
        caracteresEsp = "[#&_!%]" 
        numeros = "[0-9]" 
        matchEspeciales = search(caracteresEsp, password) 
        matchNumeros = search(numeros, password) 

        
        if matchNumeros and matchEspeciales: 
            coincidencia = True 
        else:   
            coincidencia = False 

    else:  
        coincidencia = False 

    return coincidencia  

   
 


def crearUsuario():  
    """
      Funcion     : crearUsuario
      Descripcion : solicita un usuario y contraseña, validando que ambos formatos sean correctos para casí crear el usuario
      Entrada     : ()
      Salida      : True = si se pudo crear el usuario y False = si no se pudo crear el usuario. 
    """

    usuarioInvalido = True 

    while usuarioInvalido == True: 
        usuario = input("Ingrese una dirección de correo: ").lower()       
                                                                      
        valido = validarEmail(usuario)  

        if valido:
            usuarioInvalido = existeUsuario(usuario,archivo_usuarios)
            if usuarioInvalido == True:
                print("El usuario ya existe. Por favor intente nuevamente...")
        else:
            usuarioInvalido = True 
            print("El email ingresado no tiene un formato válido. Por favor, intente nuevamente. ")
    


    passwordInvalido = True 

    while passwordInvalido == True: 
        password = input("Ingrese la contraseña: ") 
        valida = validarPassword(password) 
        if valida: 
            passwordInvalido = False 
        else:
           passwordInvalido = True 
           print("La contraseña ingresada no cumple con los requisitos. Por favor, intente nuevamente. ")



         
    if guardar_usuario(usuario,password,archivo_usuarios):
        print("Usuario creado exitosamente!")
        input("Presione ENTER para volver al menu principal")
    else:
        print("No se pudo crear el usuario")
        input("Presione ENTER para volver al menu principal")