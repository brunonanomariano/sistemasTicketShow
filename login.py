from globales import *;
from crearUsuario import *;

def verificar_datos (usuario, password, archivo_user): 
    """"
      Funcion     : verificar_datos
      Descripcion : controla que el usuario y la pass sean correctos 
      Entrada     : usuario, password, archivo de usuarios
      Salida      : True (si usuario ya existe en el archivo)
                    False (si el usuario no existe en el archivo)
    """

    existencia_usuario = False
    usuarios = []

    if existe_archivo(archivo_user):
        try:
            with open(archivo_user, "r") as archivo:
                usuarios = json.load(archivo)
        except json.JSONDecodeError:
            existencia_usuario = False

        for usuarioCargado in usuarios:
            if usuarioCargado["user"] == usuario and usuarioCargado["password"] == password:
                existencia_usuario = True      

    return existencia_usuario
 
def logear_usuario():
    """
        Funcion     : loguear_usuario
        Descripcion : solicita usuario y contraseña, verifica si existe en la lista de usuarios creados y si no existe vuelve a pedirlo
        Entrada     : -
        Salida      : False (si no pudo logearse dentro de los primeros 3 intentos)
                      True  (si lo encontro antes de los primeros 3 intentos)
    """
    intentos = 0
    encontrado = False
   
    while intentos < 3 and not encontrado:
       
        usuario = input("Ingresa el usuario: ")
        contrasenia = input("Ingresa la contraseña: ")
       
        if verificar_datos(usuario, contrasenia, archivo_usuarios):
            encontrado = True
            print("Usuario logueado correctamente")
            input("Presione ENTER para continuar")
        else:
            print("Usuario o contraseña incorrectos, intenta nuevamente")
            intentos += 1
 
    if intentos < 3:
        return True
    else:
        return False