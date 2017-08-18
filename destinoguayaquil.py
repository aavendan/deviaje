#coding:latin-1
import numpy as np

def bienvenida():
    print("Bienvenid@s a @DeViaje593")

def menu():
    print("""
        Opción 1: Sitios Turísticos de Guayaquil.
        Opción 2: Número de veces visitado.
        Opción 3: Visitantes.
        Opción 4: MAAC.
        Opción 5: Visita a lugares.
        Opción 6: Sitios emblemáticos.
        Opción 7: Isla Santay.
    """)

def opcion1(lol):
    matriz = np.array(lol, dtype=str)
    return matriz

def opcion2(sitio, matriz):
    #aquí debe filtrar la matriz de acuerdo al sitio enviado
    #debe devolver el número de veces que aparece el sitio