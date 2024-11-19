from globales import *;
from crearUsuario import *;



def verificar_opcion(opcion, lista_opciones):
    """
      Funcion     : verificar_opcion
      Descripcion : recibe una opcion y una lista de posibles opciones e informa si la opcione es correcta o no
      Entrada     : opcion
                   lista_opciones
      Salida      : False (si la opcion no esta en la lista de opciones)
                    True  (si la opcion esta en la lista de opciones)
    """

    if opcion in lista_opciones:
        return True
    else:
        print("La opcion ingresada no esta disponible")
        return False
    


def procesar_bienvenida():
    """
      Funcion     : procesar_bienvenida
      Descripcion : procesa la primera pantalla espreando recibir una opcion correcta y devolviendo la opcion elegida en ese caso
      Entrada     : -
      Salida      : opcion (una opcion validad elegida por el usuario)
    """

    opcionCorrecta = False

    while opcionCorrecta == False:
        try:
            opcion = int(input("Por favor ingrese una opcion para continuar ----> "))
            opcionCorrecta = verificar_opcion(opcion, [1,2,3])
        except ValueError:
            print("La opcion ingresada no es numero, por favor ingrese una opcion en pantalla")
            opcionCorrecta = False
        
    return opcion



def procesar_seleccion_shows():
    """
      Funcion     : procesar_seleccion_shows
      Descripcion : procesa la pantalla de seleccion de shows
      Entrada     : -
      Salida      : opcion (una opcion validad elegida por el usuario)
                    cant_tickets (cantidad valida de tickets para ese show)
    """

    lista_shows=[]
    opcion = 0
    cant_tickets = 0

    if existe_archivo(archivo_salas):
        try:
            with open(archivo_salas, "r") as archivo:
                lista_shows = json.load(archivo)
                cantidad_conciertos = len(lista_shows)
    
                lista_opciones = list(range(1,cantidad_conciertos+1))

                opcionCorrecta = False
                while opcionCorrecta == False:
                    try:
                        opcion = int(input("Ingrese el show al cual desea asistir ----> "))
                        opcionCorrecta = verificar_opcion(opcion, lista_opciones)
                        if opcionCorrecta:
                            opcion -= 1 #Le resto 1 a la opcion para coincidir con los indices
                            if lista_shows[opcion]["disponibilidadAsientos"] == 0: 
                                opcionCorrecta = False
                                print("El show al cual desea asistir se encuentra agotado, por favor seleccione otra fecha")
                            else: #Verifico disponibilidad de tickets
                                supera_ubicacicones = True
                                try:
                                    cant_tickets = int(input("Ingrese la cantidad de tickets que desea comprar: "))
                                    while supera_ubicacicones == True:
                                        if cant_tickets > lista_shows[opcion]["disponibilidadAsientos"]:
                                            cant_tickets=int(input("La cantidad solicitada supera la disponible. Ingrese una nueva cantidad: "))
                                            supera_ubicacicones = True
                                        else:
                                            supera_ubicacicones = False
                                except:
                                    print("La cantidad ingresada debe ser un numero, por favor reintente nuevamente")
                                    opcionCorrecta = False
                    except:
                        print("La opcion ingresada debe ser un numero, por favor reintente nuevamente")
                        opcionCorrecta = False

                sala_elegida = lista_shows[opcion]

        except Exception as e:
            print(f"Ocurrió un error al abrir el archivo: {e}")
    else:
        print("No existen show disponibles en este momento")

    return sala_elegida, cant_tickets, opcion


    

