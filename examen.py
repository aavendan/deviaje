#coding:latin-1

def cargarDatos(nombreArchivo):

    archivo = open(nombreArchivo, "r")
    lineas = archivo.readlines()
    archivo.close()

    diccionarioGrande = dict()

    for linea in lineas: #linea -> Azogues| Pedernales,555|...|Babahoyo,125
        lista = linea.split("|") # [Azogues, "Pedernales,555", "Babahoyo,125"]

        clave = lista[0]

        listaParaDiccionario = lista[1:]
        diccionarioPequeño = dict()

        for elemento in listaParaDiccionario: #elemento -> "Pedernales,555"
            listaPequeña = elemento.split(",")

            clavePequeña = listaPequeña[0]
            valorPequeño = listaPequeña[1]

            diccionarioPequeño[clavePequeña] = int(valorPequeño)

        diccionarioGrande[clave] = diccionarioPequeño

    return diccionarioGrande


def ciudadesCercanas(distancias, km):

    lista = []

    for ciudadOrigen in distancias.keys():

        diccionarioPequeño = distancias[ciudadOrigen]

        for ciudadDestino in diccionarioPequeño.keys():

            valor = diccionarioPequeño[ciudadDestino]

            if valor <= km:

                tupla = (ciudadOrigen, ciudadDestino, valor)

                lista.append(tupla)

    return lista

def ciudadesCercanas(distancias, km):

    lista = []

    for ciudadOrigen, diccionarioPequeño in distancias.items():

        for ciudadDestino, valor in diccionarioPequeño.items():

            if distancias[ciudadOrigen][ciudadDestino] <= km:

                lista.append( (ciudadOrigen, ciudadDestino, valor) )

    return lista

def guardarCiudadesCercanas(distancias, listaKms):

    for km in listaKms:

        listaTuplas = ciudadesCercanas(km=km, distancias=distancias)

        nombreArchivo = "ciudades"+str(km)+".txt"

        archivo = open(nombreArchivo, "w")

        for tupla in listaTuplas: #tupla -> ('Azogues','Babahoyo',125)

            ciudadOrigen, ciudadDestino, valor = tupla

            linea = ciudadOrigen+","+ciudadDestino+","+str(valor)+"\n"

            archivo.write(linea)

        archivo.close()


#distancias = cargarDatos('Ecuador_Distancias.txt')
#guardarCiudadesCercanas(distancias, [150, 225, 320, 555])


def buscar(listaAnidada, valor):

    existe = False

    for lista in listaAnidada:

        if valor in lista:

            existe = True

    return existe

lista = [
    [1,2,3],
    [6,4,5],
    [7,8,9]
]

print( buscar(listaAnidada=lista, valor=5) )


L = [[3, 2, 5], [1], [7, 9]]
X = int(input('Ingrese valor por teclado'))
#su código aquí

if buscar(listaAnidada=L, valor=X):
    print('Valor si existe')
else:
    print('Valor no existe')