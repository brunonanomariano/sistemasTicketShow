from re import match

##########################################################################################################################################
#  Funcion     : validarEmail
#  Descripcion : recibe un email y valida el formato. 
#  Entrada     : email
#  Salida      : none (no hay coincidencia en el patrón) o objeto (hay coincidencia en el patrón)
#######################################################################################################AAA###################################

def validarEmail (email):
    patron = "[0-9a-z]+@[a-z]+.[com]"
    resultado = match(patron, email) 
    return resultado


##########################################################################################################################################
#  Funcion     : validarPassword
#  Descripcion : recibe un password y valida el formato. 
#  Entrada     : password
#  Salida      : 
#######################################################################################################AAA###################################


def validarPassword(password):
    patron = "[]"
    return



##########################################################################################################################################
#  Funcion     : crearUsuario
#  Descripcion : solicita un usuario y contraseña, validando que ambos formatos sean correctos
#  Entrada     : ()
#  Salida      : True = si se pudo crear el usuario y False = si no se pudo crear el usuario. 
##########################################################################################################################################


def crearUsuario ():  
    
    usuarioInvalido = True #Se setea en true para que entre la primera vez

    while usuarioInvalido == True: 
        usuario = input("Ingrese una dirección de correo: ").lower()  #Convertimos todo a minuscula para que no sea key sensitive 
        valido = validarEmail(usuario) #None - un objeto
        if valido: #Si la dirección de correo hizo match, entonces salimos del ciclo y termina la ejecución.
            usuarioInvalido = False 
        else:
            usuarioInvalido = True #El usuario es invalido, hay que ingresarlo nuevamente. Se setea la bandera en true para continuar el ciclo.
            print("El email ingresado no tiene un formato válido. Intente nuevamente. ")
    


crearUsuario()
