#coding:latin-1
import numpy as np

def bienvenida():
    print("Bienvenid@s a @DeViaje593")

def menu():
    print("""
        Opci�n 1: Sitios Tur�sticos de Guayaquil.
        Opci�n 2: N�mero de veces visitado.
        Opci�n 3: Visitantes.
        Opci�n 4: MAAC.
        Opci�n 5: Visita a lugares.
        Opci�n 6: Sitios emblem�ticos.
        Opci�n 7: Isla Santay.
    """)

def opcion1(lol):
    matriz = np.array(lol, dtype=str)
    return matriz

def opcion2(sitio, matriz):
    #aqu� debe filtrar la matriz de acuerdo al sitio enviado
    #debe devolver el n�mero de veces que aparece el sitio