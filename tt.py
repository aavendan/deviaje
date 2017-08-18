archivo = open('practica/metadata-tweetero.txt','r')

usuarios = dict()

for linea in archivo:
    datos = linea.split("$")

    if datos[2] not in usuarios.keys():
        usuarios[datos[2]] = 1
    else:
        usuarios[datos[2]] += 1

archivo.close()

for clave, valor in usuarios.items():
    if(valor >= 10):
        print(clave, valor)