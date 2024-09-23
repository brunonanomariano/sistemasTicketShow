usuarios = []

def validar_usuario():
    valido = False 
    while valido == False:
        valido = True 
        usuario = input("Ingrese su nombre de usuario: ")

        for i in usuarios:
                if i["usuario"] == usuario :
                    print("Este usuario ya se encuentra")
                    valido = False

        if len(usuario) > 20:
            print("tiene que tener menos caracteres ")
            valido = False

        if len(usuario) < 5:
            print("tiene que tener mas caracteres ")
            valido = False

        caracteres_especiales = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "{", "}", "[", "]", "|", "\\", ":", ";", "'", "\"", "<", ">", ",", ".", "?", "/"]

        for i in usuario:
            if i in caracteres_especiales:
                print("no puede contener caracteres especiales el usuario ")
                valido = False

    return usuario





def probar_contraseña():
    caracteres_mayuscula = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    contador_mayusculas = 0
    valido = False
    while not valido:
        valido = True 

        contrasena = input("Ingrese su contraseña de usuario: ")

        for i in contrasena:
            if i in caracteres_mayuscula:
                contador_mayusculas += 1


        if contador_mayusculas < 1:
            print("La contraseña tiene que tener mas mayusculas")
            valido = False                

        if len(contrasena) < 5:
            print("La contraseña debe de tener más caracteres: ")
            valido = False

        if len(contrasena) > 15:
            print("Límite máximo de carácteres excedido, porfavor ingrese menos: ")
            valido = False

    return contrasena

def crear_usuario(usuarios):

    usuario = validar_usuario()
    
    contrasena = probar_contraseña()

    usuarios.append({"usuario": usuario, "contrasena": contrasena})
    print(usuarios)

crear_usuario(usuarios=usuarios)