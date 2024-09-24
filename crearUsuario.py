from re import match, search
from globales import *

##########################################################################################################################################
#  Funcion     : existeUsuario
#  Descripcion : recibe un usuario y verifica si ya existe 
#  Entrada     : usuario
#  Salida      : True (si usuario ya existe en la lista de usuarios)
#                False (si el usuario no existe)
#######################################################################################################AAA###################################

def existeUsuario (usuario): #Tiene como parametro el usuario que se creó en la función crearUsuario

    for dicUsuario in lista_usuarios: # Recorre la lista y se fija si el usuario está. 
                                      #Le asigna cada elemento de lista_usuarios a dicUsuarios.
                                      #lista_usuarios se encuentra el globales.
        if dicUsuario["user"] == usuario: #Si en la clave user de cada dicUsuario se encuentra el usuario que se pasó por parametro,
                                          #Entonces el usuario ya existe.
            print("Lo sentimos, el usuario ingresado ya existe.")
            return True #Existe le usuario
    
    return False #No existe el usuario 


##########################################################################################################################################
#  Funcion     : validarEmail
#  Descripcion : recibe un email y valida el formato. 
#  Entrada     : email
#  Salida      : none (no hay coincidencia en el patrón) u objeto coincidencia (hay match del email con el patrón)
#######################################################################################################AAA###################################

def validarEmail (email):  
    patron = "[0-9a-z]+@[a-z]+.com" #Se crea la variable patrón que guarda las validaciones del email.
                                    #Las validaciones se componen de:
                                    #+: uno o más caracteres [0-9a-z]   
                                    # @[a-z] -> arroba más uno o más caracteres a-z
                                    #.com -> el literal
    resultado = match(patron, email) #Compara el email con el patrón descripto
                                   
    return resultado   #Si hay match, devuelve un objeto considencia, sino devuelve None.


##########################################################################################################################################
#  Funcion     : validarPassword
#  Descripcion : recibe un password y valida el formato. 
#  Entrada     : password
#  Salida      : True: la clave es valida o False: la clave es invalida.
#######################################################################################################AAA###################################

def validarPassword(password):
    
    patron = "[A-Z][a-zA-Z0-9#&_!%]{,8}" #Que haya 8 caracteres máximos con esas combinaciones mencionadas. 
                                          #La primer letra deberá ser una mayúscula.
                                          #Luego se compone de elementos alfanúmericos y caracteres especiales ya definidos. 

    #Primera validación padrón y password.                                     
    resultado = match(patron, password) #Valida que el padrón matchee con la contraseña ingresada. Devuelve un objeto coincidencia si es así.
                                        #sino devuelve None.
    
    if resultado: #If resultado == True | Es decir, si el resultado no es None y sí es un objeto coincidencia, entonces: 
        caracteresEsp = "[#&_!%]" #Creo una variable para mis caracteres especiales.
        numeros = "[0-9]" #Creo una variable para los números.
        matchEspeciales = search(caracteresEsp, password) #Se busca si hay al menos algún caracter especial presente en la password.
        matchNumeros = search(numeros, password) #Se busca si hay al menos algún número presente en la password. 

        #---Tiene que verificarse que haya sí o sí exista al menos un caracter especial y un número, por lo tanto:--- 
        if matchNumeros and matchEspeciales: #Si el search devuelve un objeto, es porque encontró un caracter esp. o un número
            coincidencia = True #Entonces hay coincidencia. La clave es correcta porque tiene 8 caracteres y responde al patrón definido.
        else:   
            coincidencia = False #Sino, no hay coincidencia: no se encontró un caracter esp. o un número.

    else:  
        coincidencia = False #No hay coincidencias en la primera validación, ya que la pass no tiene 8 caracteres.

    return coincidencia  #Retorna True o False. 

   
 


##########################################################################################################################################
#  Funcion     : crearUsuario
#  Descripcion : solicita un usuario y contraseña, validando que ambos formatos sean correctos para casí crear el usuario
#  Entrada     : ()
#  Salida      : True = si se pudo crear el usuario y False = si no se pudo crear el usuario. 
##########################################################################################################################################


def crearUsuario():  
    
    #---VadaciónUsuario----

    usuarioInvalido = True #Se setea en True para que entre la primera vez al ciclo While.

    while usuarioInvalido == True: 
        usuario = input("Ingrese una dirección de correo: ").lower()  #Convertimos todo a minuscula para que no sea key sensitive.      
                                                                      
        #1era Validacion: Patrón - Email.
        valido = validarEmail(usuario)  #validarEmail -> valida el email (es decir, el usuario) ingresado con el patrón. 
                                        #Devuelve None o un objeto coincidencia. 
                                        #Lo guardamos en la varible valido. 

        #2da validación: Existencia Previa del Usuario.
        if valido: #If valido == True | Si validarEmail devolvió un objeto coincidencia, es porque el email es válido. 
                   #Entonces, habrá que validar también que no exista el usuario previamente en la base:

            usuarioInvalido = existeUsuario(usuario) #existeUsuario devuelve True o False y recibe un usuario. 
                                                     #Si usuario existe previamente, usuarioInvalido es True, ya que el usuario NO es valido. 
                                                     #Si es False, sale del ciclo porque el usuario no existe y por ende, SÍ es valido. 
        
        else:
            usuarioInvalido = True #El usuario es invalido por el formato (validación patrón-email), hay que ingresarlo nuevamente. 
                                   #Se setea la bandera en True para continuar el ciclo.
            print("El email ingresado no tiene un formato válido. Por favor, intente nuevamente. ")
    

    #---ValidaciónPassword----

    passwordInvalido = True #Se setea en True para que entre la primera vez

    while passwordInvalido == True: 
        password = input("Ingrese la contraseña: ") 
        valida = validarPassword(password) #validarPassword devuelve True o False.
        if valida: #Si password == True -> Es decir, validarPassword devolvió un objeto y por ende la password es válida. 
            passwordInvalido = False #Se cambia la bandera a False y se termina el ciclo.
        else:
           passwordInvalido = True #Sino, la password es Invalida. Se setea la bandera en True. Continúa el ciclo.
           print("La contraseña ingresada no cumple con los requisitos. Por favor, intente nuevamente. ")




    #Una vez validados corectamente usuario y contraseña:

        #Se grabarán en una variable diccionario y se agregará a mi lista de usuarios.
        #lista_usuarios está en globales. Sólo existe el usuario admin/admin harcodeado.
         
    usuario = {"user": usuario, "password": password}
    lista_usuarios.append(usuario)


