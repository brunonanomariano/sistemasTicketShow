from re import match, search
from globales import *

##########################################################################################################################################
#  Funcion     : existeUsuario
#  Descripcion : recibe un usuario y verifica si ya existe 
#  Entrada     : usuario
#  Salida      : True (si usuario ya existe en la lista de usuarios)
#                False (si el usuario no existe)
#######################################################################################################AAA###################################

def existeUsuario (usuario): 

    for dicUsuario in lista_usuarios: 
        if dicUsuario["user"] == usuario: 
            print("Lo sentimos, el usuario ingresado ya existe.")
            return True 
    
    return False 

##########################################################################################################################################
#  Funcion     : validarEmail
#  Descripcion : recibe un email y valida el formato. 
#  Entrada     : email
#  Salida      : none (no hay coincidencia en el patrón) u objeto coincidencia (hay match del email con el patrón)
#######################################################################################################AAA###################################

def validarEmail (email):  
    patron = "[0-9a-z_-]+@[a-z]+.com" 
    resultado = match(patron, email) 
                                   
    return resultado  


##########################################################################################################################################
#  Funcion     : validarPassword
#  Descripcion : recibe un password y valida el formato. 
#  Entrada     : password
#  Salida      : True: la clave es valida o False: la clave es invalida.
#######################################################################################################AAA###################################

def validarPassword(password):
    
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

   
 


##########################################################################################################################################
#  Funcion     : crearUsuario
#  Descripcion : solicita un usuario y contraseña, validando que ambos formatos sean correctos para casí crear el usuario
#  Entrada     : ()
#  Salida      : True = si se pudo crear el usuario y False = si no se pudo crear el usuario. 
##########################################################################################################################################


def crearUsuario():  
    

    usuarioInvalido = True 

    while usuarioInvalido == True: 
        usuario = input("Ingrese una dirección de correo: ").lower()       
                                                                      
        valido = validarEmail(usuario)  

        if valido:

            usuarioInvalido = existeUsuario(usuario)  
        
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



         
    usuario = {"user": usuario, "password": password}
    lista_usuarios.append(usuario)


