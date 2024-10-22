from globales import lista_usuarios  
 
##########################################################################################################################################
#  Funcion     : verificar_usuario
#  Descripcion : recibe un usuario y contraseña. Valida si ese usuario está registrado en la lista de usuarios
#  Entrada     : usuario, contraseña
#  Salida      : True (si lo encontro)
#                False (si no lo encontro)
#######################################################################################################AAA###################################
 
def verificar_usuario(usuario, contrasena):
 
    encontrado = False
    for dicUsuario in lista_usuarios:
       
        if dicUsuario["user"] == usuario: 
            if dicUsuario["password"] == contrasena: 
                encontrado = True
                return encontrado
            else: 
                encontrado = False
                return encontrado
 
    return encontrado
 
 
##########################################################################################################################################
#  Funcion     : loguear_usuario
#  Descripcion : solicita usuario y contraseña, verifica si existe en la lista de usuarios creados y si no existe vuelve a pedirlo
#  Entrada     : -
#  Salida      : False (si no pudo logearse dentro de los primeros 3 intentos)
#                True  (si lo encontro antes de los primeros 3 intentos)
#######################################################################################################AAA###################################
 
def logear_usuario():
    intentos = 0
    encontrado = False
   
    while intentos < 3 and not encontrado:
       
        usuario = input("Ingresa el usuario: ")
        contraseña = input("Ingresa la contraseña: ")
       
        if verificar_usuario(usuario, contraseña):
            encontrado = True
            print("Usuario logueado correctamente")  
        else:
            print("Usuario o contraseña incorrectos, intenta de nuevo.")
            intentos += 1
 
    if intentos < 3:
        return True
    else:
        return False
