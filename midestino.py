#coding:latin-1
import random
from faker import Faker

#Devuelve una lista de listas, con los lugares más visitados en Guayaquil
#parámetros opcionales: topSitios = 5, numeroResultados = 9

def obtenerResultadosEncuestas(topSitios = 5, numeroResultados = 9):
    resultados = []
    lugares = ["Parque Centenario", "Malecón 2000", "Malecón del Salado", "Isla Santay", "MAAC", "Catedral",
               "Parque Seminario",
               "Hemiciclo Rotonda",
               "Parque Lago", "Parque Forestal", "Museo Municipal", "La Perla", "El Pantanal", "Museo Nahim Isaías",
               "Museo Miniatura",
               "Safari Park", "Museo Presley Norton", "Museo Luis A. Noboa Naranjo",
               "Bosque Seco Protector Cerro Paraiso",
               "Museo de Música Popular", "Parque Pdte. Clemente Yerovi Indaburu", "Parque ESPOL",
               "Museo De Los Equipos Del Astillero - Barcelona & Emelec", "Museo Del Bombero", "Parque Histórico",
               "Plaza Rodolfo Baquerizo Moreno", "El Museo Del Cacao", "Parque Japonés"]

    for i in range(numeroResultados):
        random.shuffle(lugares)
        resultados.append(lugares[:topSitios])

    return resultados

#Devuelve una lista de usuarios de Twitter que participaron en las encuentas
#parámetro opcional: numeroPersonas = 9

def obtenerResultadosUsuarios(numeroPersonas = 9):
    usuarios = []
    fake = Faker()
    for i in range(numeroPersonas):
        usuarios.append("@"+fake.user_name())

    return usuarios

#Devuelve una lista de listas con los resultados asignados por cada usuario a un sitio turístico
#parámetros opcionales: topSitios = 5, numeroResultados = 9

def obtenerResultadosRanking(topSitios = 5, numeroResultados = 9):
    resultados = []
    for i in range(numeroResultados):
        puntos = []
        for j in range(topSitios):
            puntos.append(random.randrange(1,10,1))
        resultados.append(puntos)
    return resultados