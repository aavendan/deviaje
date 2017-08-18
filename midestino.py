#coding:latin-1
import random
from faker import Faker

#Devuelve una lista de listas, con los lugares m�s visitados en Guayaquil
#par�metros opcionales: topSitios = 5, numeroResultados = 9

def obtenerResultadosEncuestas(topSitios = 5, numeroResultados = 9):
    resultados = []
    lugares = ["Parque Centenario", "Malec�n 2000", "Malec�n del Salado", "Isla Santay", "MAAC", "Catedral",
               "Parque Seminario",
               "Hemiciclo Rotonda",
               "Parque Lago", "Parque Forestal", "Museo Municipal", "La Perla", "El Pantanal", "Museo Nahim Isa�as",
               "Museo Miniatura",
               "Safari Park", "Museo Presley Norton", "Museo Luis A. Noboa Naranjo",
               "Bosque Seco Protector Cerro Paraiso",
               "Museo de M�sica Popular", "Parque Pdte. Clemente Yerovi Indaburu", "Parque ESPOL",
               "Museo De Los Equipos Del Astillero - Barcelona & Emelec", "Museo Del Bombero", "Parque Hist�rico",
               "Plaza Rodolfo Baquerizo Moreno", "El Museo Del Cacao", "Parque Japon�s"]

    for i in range(numeroResultados):
        random.shuffle(lugares)
        resultados.append(lugares[:topSitios])

    return resultados

#Devuelve una lista de usuarios de Twitter que participaron en las encuentas
#par�metro opcional: numeroPersonas = 9

def obtenerResultadosUsuarios(numeroPersonas = 9):
    usuarios = []
    fake = Faker()
    for i in range(numeroPersonas):
        usuarios.append("@"+fake.user_name())

    return usuarios

#Devuelve una lista de listas con los resultados asignados por cada usuario a un sitio tur�stico
#par�metros opcionales: topSitios = 5, numeroResultados = 9

def obtenerResultadosRanking(topSitios = 5, numeroResultados = 9):
    resultados = []
    for i in range(numeroResultados):
        puntos = []
        for j in range(topSitios):
            puntos.append(random.randrange(1,10,1))
        resultados.append(puntos)
    return resultados