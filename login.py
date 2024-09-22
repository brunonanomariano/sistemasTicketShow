# función     : loguear_usuario
#descripción : recibe un usuario y contraseña. Valida si ese usuario está registrado
#en el diccionario y si la contraseña ingresada coincide con la almacenada para ese usuario.
# entrada     : usuario(correo) y contraseña con la que el usuario se quiere loguear.
# salida      : True: Si el usuario está registrado y la contraseña coincide. 
# False: Si el usuario no está registrado o la contraseña no es correcta.
usuarios_registrados = {}

def logear_usuario(usuario, password):
    # se valida si el usuario existe en el diccionario
    if usuario in usuarios_registrados:
        # verificar si la contraseña coincide
        if usuarios_registrados[usuario] == password:
            return True 
        else:
            return False  # Contraseña incorrecta
    else:
        return False  # Usuario no encontrado
    
    