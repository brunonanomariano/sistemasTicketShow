from re import match, search
from globales import *

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
    
    patron = "[A-Z][a-zA-Z0-9#&-_!%]{,8}" #Que haya 8 caracteres máximos de esas combinaciones
    resultado = match(patron, password) #que el padrón matchee con la contraseña ingresada. Devuelve un objeto si es así.
    
    if resultado: #si el resultado no es None y sí es un objeto, entonces: 
        caracteresEsp = "[#&-_!%]" #creo una variable para mis caracteres esp.
        numeros = "[0-9]" #creo una variable para los números 
        matchEspeciales = search(caracteresEsp, password) #se encuentra si hay algún caracter especial en la password
        matchNumeros = search(numeros, password) # se encuentra si hay algún número en la password
        #Tiene que verificarse que haya sí o sí un caracter especial y un número, por lo tanto: 
        if matchNumeros and matchEspeciales: #si el search devuelve un objeto, es porque encontró un caracter esp. o un número
            coincidencia = True
        else:   
            coincidencia = False #No encontró un caracter esp. o un número
    else:  
        coincidencia = False #No hay coincidencias, ya que la pass no tiene 8 caracteres

    return coincidencia 

   
 


##########################################################################################################################################
#  Funcion     : crearUsuario
#  Descripcion : solicita un usuario y contraseña, validando que ambos formatos sean correctos
#  Entrada     : ()
#  Salida      : True = si se pudo crear el usuario y False = si no se pudo crear el usuario. 
##########################################################################################################################################


def crearUsuario():  
    
    usuarioInvalido = True #Se setea en true para que entre la primera vez

    while usuarioInvalido == True: 
        usuario = input("Ingrese una dirección de correo: ").lower()  #Convertimos todo a minuscula para que no sea key sensitive 
        valido = validarEmail(usuario) #Devuelve None o un objeto
        if valido: #Si la dirección de correo hizo match, entonces salimos del ciclo y termina la ejecución.
            usuarioInvalido = False 
        else:
            usuarioInvalido = True #El usuario es invalido, hay que ingresarlo nuevamente. Se setea la bandera en true para continuar el ciclo.
            print("El email ingresado no tiene un formato válido. Intente nuevamente. ")
    

    passwordInvalido = True #Se setea en true para que entre la primera vez

    while passwordInvalido == True:
        password = input("Ingrese la contraseña: ")
        valida = validarPassword(password)
        if valida:
            passwordInvalido = False
        else:
           passwordInvalido = True
           print("La contraseña ingresada no cumple con los requisitos. ")

    #Una vez ingresados corectamente usuario y contraseña la grabo en una variable diccionario y la agrega a mi lista de usuarios
    usuario = {"user": usuario, "pass": password}
    usuarios.append(usuario)


