#from salas import *;
import json;

archivo_usuarios = "usuarios.json"
archivo_salas="salas.json"

#FILAS_SALA=13
#ASIENTOS_SALA=10
#
#sala_abel = crear_sala(FILAS_SALA,ASIENTOS_SALA)
#disp_abel = calcular_disponibilidad(sala_abel)
#
#sala_tanBionica = crear_sala(FILAS_SALA,ASIENTOS_SALA)
#disp_tanBionica = calcular_disponibilidad(sala_tanBionica)
#
#sala_twenty_one_pilots = crear_sala(FILAS_SALA,ASIENTOS_SALA)
#disp_twenty_one_pilots = calcular_disponibilidad(sala_twenty_one_pilots)
#
#sala_sole = crear_sala(FILAS_SALA,ASIENTOS_SALA)
#disp_sole = calcular_disponibilidad(sala_sole)
#
#sala_redhot = crear_sala(FILAS_SALA,ASIENTOS_SALA)
#disp_redhot = calcular_disponibilidad(sala_redhot)
#
#
#lista_conciertos = [
#    {"nombreArtista": "Abel Pintos", "fecha": "09/01/2025", "sala": sala_abel, "disponibilidadAsientos": disp_abel, "precioBase": 18000},
#    {"nombreArtista": "Tan Bionica", "fecha": "30/11/2024", "sala": sala_tanBionica, "disponibilidadAsientos": disp_tanBionica, "precioBase": 15000},
#    {"nombreArtista": "Twenty One Pilots", "fecha": "22/12/2024", "sala": sala_twenty_one_pilots, "disponibilidadAsientos": disp_twenty_one_pilots, "precioBase": 25000},
#    {"nombreArtista": "Soledad Pastorutti", "fecha": "12/10/2024", "sala": sala_sole, "disponibilidadAsientos": 0, "precioBase": 10000},
#    {"nombreArtista": "Red Hot Chili Peppers", "fecha": "30/10/2024", "sala": sala_redhot, "disponibilidadAsientos": disp_redhot, "precioBase": 30000}
#]

cupones_validos = {
    'DESC10': 0.10,
    'DESC20': 0.20,
    'DESC30': 0.30
}

#def grabar_salas():
#    with open(archivo_salas, "w") as archivo:
#        json.dump(lista_conciertos, archivo, indent=4)
