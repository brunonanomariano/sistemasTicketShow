# función     : loguear_usuario
#descripción : recibe un usuario y contraseña. Valida si ese usuario está registrado
#en el diccionario y si la contraseña ingresada coincide con la almacenada para ese usuario.
# entrada     : usuario(correo) y contraseña con la que el usuario se quiere loguear.
# salida      : True: Si el usuario está registrado y la contraseña coincide. 
# False: Si el usuario no está registrado o la contraseña no es correcta.

from globales import usuarios  

def verificar_usuario(usuario, contraseña):

    usuario = input("Ingresa el usuario: ")
    contraseña = input("Ingresa la contraseña: ")

    encontrado = False
    for i in usuarios:
        if i[usuario] == contraseña:
            encontrado = True

    return encontrado


def logear_usuario():
    autenticado = False
    
    while not autenticado:
        
        usuario = input("Ingresa el usuario: ")
        contraseña = input("Ingresa la contraseña: ")

        
        if verificar_usuario(usuario, contraseña):
            print("Usuario logueado correctamente")
            autenticado = True  
        else:
            print("Usuario o contraseña incorrectos, intenta de nuevo.")

logear_usuario()
