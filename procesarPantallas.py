def verificar_opcion(opcion, lista_opciones):
    if opcion in lista_opciones:
        return True
    else:
        print("La opcion ingresada no esta disponible")
        return False
    



    
def procesar_bienvenida():
    opcionCorrecta = False

    while not opcionCorrecta:
        opcion = int(input("Por favor ingrese una opcion para continuar ----> "))
        opcionCorrecta = verificar_opcion(opcion, [1,2,3])

    return opcion
    

