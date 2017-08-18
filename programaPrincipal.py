#coding:latin-1
import midestino as ec
import numpy as np
import destinoguayaquil as dg


#print("Lista de listas de sitios visitados")

listaResultados = ec.obtenerResultadosEncuestas()
listaUsuarios = ec.obtenerResultadosUsuarios()
listaRanking = ec.obtenerResultadosRanking()

#print(listaResultados)
#print(listaUsuarios)
#print(listaRanking)

dg.bienvenida()
dg.menu()

opcion = int(input("Ingrese la opción del menú: "))
while not(0< opcion < 8):
    opcion = int(input("Ingrese la opción del menú: "))

if opcion == 1:
    lol = ec.obtenerResultadosEncuestas()
    matriz = dg.opcion1(lol)
    print(matriz)
elif opcion == 2:
    lol = ec.obtenerResultadosEncuestas()
    matriz = dg.opcion1(lol)

    sitio = input("Ingrese el lugar turistico")

    numeroDeVeces = dg.opcion2(sitio, matriz)