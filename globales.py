from salas import *;
#Lista de usuarios creados
lista_usuarios = [
    {"user": "admin", "password": "admin"}
    ]

#Creo las salas y calculo su disponibilidad
sala_abel = crear_sala(11,9)
disp_abel = calcular_disponibilidad(sala_abel)

sala_tanBionica = crear_sala(10,9)
disp_tanBionica = calcular_disponibilidad(sala_tanBionica)

sala_twenty_one_pilots = crear_sala(11,10)
disp_twenty_one_pilots = calcular_disponibilidad(sala_twenty_one_pilots)

sala_sole = crear_sala(8,15)
disp_sole = calcular_disponibilidad(sala_sole)

sala_redhot = crear_sala(13,15)
disp_redhot = calcular_disponibilidad(sala_redhot)

#Armo la lista de shows disponibles
lista_conciertos = [
    {"nombreArtista": "Abel Pintos", "fecha": "09/01/2025", "sala": sala_abel, "disponibilidadAsientos": disp_abel, "precioBase": 18000},
    {"nombreArtista": "Tan Bionica", "fecha": "30/11/2024", "sala": sala_tanBionica, "disponibilidadAsientos": disp_tanBionica, "precioBase": 15000},
    {"nombreArtista": "Twenty One Pilots", "fecha": "22/12/2024", "sala": sala_twenty_one_pilots, "disponibilidadAsientos": disp_twenty_one_pilots, "precioBase": 25000},
    {"nombreArtista": "Soledad Pastorutti", "fecha": "12/10/2024", "sala": sala_sole, "disponibilidadAsientos": 0, "precioBase": 10000},
    #{"nombreArtista": "Soledad Pastorutti", "fecha": "12/10/2024", "sala": sala_sole, "disponibilidadAsientos": disp_sole, "precioBase": 10000},
    {"nombreArtista": "Red Hot Chili Peppers", "fecha": "30/10/2024", "sala": sala_redhot, "disponibilidadAsientos": disp_redhot, "precioBase": 30000}
]