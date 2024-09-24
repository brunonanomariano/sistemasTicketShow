from salas import *

sala_abel = crear_sala(20,9)
disp_abel = calcular_disponibilidad(sala_abel)

sala_tanBionica = crear_sala(15,9)
disp_tanBionica = calcular_disponibilidad(sala_tanBionica)

sala_luisMiguel = crear_sala(20,10)
disp_luisMiguel = calcular_disponibilidad(sala_luisMiguel)

sala_sole = crear_sala(10,15)
disp_sole = calcular_disponibilidad(sala_sole)

sala_rolling = crear_sala(15,15)
disp_rolling = calcular_disponibilidad(sala_rolling)



#Lista de usuarios creados
lista_usuarios = []


lista_conciertos = [
    {"nombreArtista": "Abel Pintos", "fecha": "09/01/2025", "sala": sala_abel, "disponibilidadAsientos": disp_abel},
    {"nombreArtista": "Tan Bionica", "dia": "30/11/2024", "sala": sala_tanBionica, "disponibilidadAsientos": disp_tanBionica},
    {"nombreArtista": "Luis Miguel", "dia": "22/12/2024", "sala": sala_luisMiguel, "disponibilidadAsientos": disp_luisMiguel},
    {"nombreArtista": "Soledad Pastorutti", "dia": "12/10/2024", "sala": sala_sole, "disponibilidadAsientos": disp_sole},
    {"nombreArtista": "The Rolling Stones", "dia": "30/10/2024", "sala": sala_rolling, "disponibilidadAsientos": disp_rolling}
]


print(lista_conciertos)