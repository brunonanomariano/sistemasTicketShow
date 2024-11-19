from re import match;
from globales import *;
from crearUsuario import *;
import json;


def separar_fila_asiento(coordenadas):
    """
        Funcion      : separar_fila_asiento
        Descripcion  : recibe una coordenada, y separa la fila y el asiento para devolverlos
        Entrada      : coordenadas
        Salida       : fila y asiento
    """
    fila = coordenadas[0:1].upper() 
    asiento = int(coordenadas[1:])-1

    return fila, asiento


def verificar_coordenadas(filas, asientos, coordenadas):
    """
        Funcion      : verificar_coordenadas
        Descripcion  : recibe un lista de filas y de asientos, y verifica que las coordenadas ingresadas sean validas
        Entrada      : filas, coordenadas
        Salida       : invalidez (True si las coordanadas no son validas, false si las coordenadas son validas)
    """
    patron = "^[a-zA-Z][0-9]{1,2}$"
    coincide = match(patron,coordenadas)

    if coincide:
        fila, asiento = separar_fila_asiento(coordenadas)

        if not(fila in filas) or not(asiento in asientos):
            print("Las coordenadas ingresadas no se encuentran en pantalla")
            invalidez = True
        else:
            invalidez = False
    else: 
        print("Las coordenadas ingresadas no poseen un formato valido")
        invalidez = True

    return invalidez


def elegir_lugares(filas,asientos,cant_tickets, show):
    """
        Funcion     : elegir_lugares
        Descripcion : se elige y valida una ubicacion ingresada por el usuario para que la misma se encuentre
                        dentro de las opciones disponibles
        Entrada     : filas(lista de filas validas), asientos (lista de asientos validos)
        Salida      : asiento_elegido, fila_elegida (ambos en valores enteros)
    """

    lista_fila=[]
    esta_compra=[]
    i=0

    while cant_tickets > 0:
        i=i+1

        coordenada_incorrecta = True

        while coordenada_incorrecta:
            try:
                coordenadas = input(f"Ingrese las coordenadas de su ticket nro {i}, indicando primero la fila y luego el asiento:\n")
                coordenada_incorrecta = verificar_coordenadas(filas, asientos, coordenadas)

                if not(coordenada_incorrecta):
                    
                    fila_elegida, asiento_elegido = separar_fila_asiento(coordenadas)
                    fila_elegida_numerica = ord(fila_elegida) - 65 #paso la fila de letra a numero para transformala a un indice

                    #Verifico que la ubicacion este disponible dentro de la sala
                    if show["sala"][fila_elegida_numerica][asiento_elegido] == 0:
                        print("La ubicacion seleccionada esta ocupada, por favor ingese una ubicacion libre")
                        coordenada_incorrecta = True
                    else:
                        if not(coordenadas in esta_compra):
                            esta_compra.append(coordenadas) #Guardo las coordenadas para validar duplicidad durante la compra
                            #Guardo una lista de filas que me servira para calcular el total de la compra
                            #ya que el precio de un asiento depende de su fila
                            lista_fila.append(fila_elegida_numerica)
                        else:
                            print("Las cordenadas ya fueron elegidas en esta compra, por favor ingrese otra ubicacion disponible \n")
                            coordenada_incorrecta = True
            except:
                print("El formato de las ubicaciones no es correcto, reintente nuevamente")
                coordenada_incorrecta = True
                
        cant_tickets -=1

    return lista_fila, esta_compra

def marcar_asientos_ocupados(lista_compras, indice_sala):
    """
        Funcion     : marcar_asientos_ocupados
        Descripcion : marca los asientos ocupados de acuerdo de las compras realizadas dentro de una sala
        Entrada     : listado de ubicaciones comprados, indice de sala a modificar
        Salida      : True (si la operacion fue exitosa), False (caso contrario)
    """
    
    estado_operacion = True

    #Por cada ubicacion comprada la marco como ocupada y la grabo en el archivo
    for ubicacion in lista_compras:
        fila_elegida, asiento_elegido = separar_fila_asiento(ubicacion)
        fila_elegida_numerica = ord(fila_elegida.upper()) - 65

        if existe_archivo(archivo_salas):
            with open(archivo_salas, "r") as archivo:
                try:
                    lista_shows = json.load(archivo)
                    lista_shows[indice_sala]["sala"][fila_elegida_numerica][asiento_elegido] = 0
                    lista_shows[indice_sala]["disponibilidadAsientos"] -= 1
                except json.JSONDecodeError:
                    print("Error al acceder al archivo de salas")
        else:
            print("Error al acceder al archivo de salas")

        try:
            with open(archivo_salas, "w") as archivo:
                json.dump(lista_shows, archivo, indent=4)
        except Exception as e:
            estado_operacion = False
        
    return estado_operacion
            
