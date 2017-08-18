#coding:utf-8

def limpiarArchivo():
    archivo = open('tweetsCity/Guayaquil.txt', 'r', encoding="utf-8")
    lineas = archivo.readlines()
    archivo.close()

    archivo2 = open('tweetsCity/Guayaquil2.txt', 'w', encoding="UTF-8")

    for linea in lineas:
        diccionario = eval(linea)
        if 'sex' not in diccionario['text'].lower():
            diccionario['text'] = diccionario['text'].encode('iso-8859-15', 'ignore').decode('iso-8859-15')
            #diccionario['user'] = diccionario['user'].encode('iso-8859-15', 'ignore').decode('iso-8859-15')
            #diccionario['text'] = diccionario['text'].encode('iso-8859-15', 'ignore').decode('iso-8859-15')
            archivo2.write(str(diccionario) + "\n")

    archivo2.close()

#limpiarArchivo()


#id
#lang, geo, source source[source.index(">")+1:source.index("</")].encode('iso-8859-15', 'ignore').decode('iso-8859-15')
#created_at, retweet_count, favorite_count, lang, text

#entities
#   hashtags -> list dict 'text'
#place
#   name, full_name

#user
#   screen_name,favourites_count, friends_count, followers_count, location, id, created_at





def leerArchivoNuevo():
    archivo = open('guayaquil/Guayaquil2.txt', 'r', encoding="utf-8")
    lineas = archivo.readlines()
    archivo.close()

    contador = dict()

    for linea in lineas:
        diccionario = eval(linea)

        id = diccionario['id']

        source = diccionario['source']
        source = source[source.index(">") + 1:source.index("</")].encode('iso-8859-15', 'ignore').decode('iso-8859-15')

        created_at = diccionario['created_at']

        retweet_count = diccionario['retweet_count']
        favorite_count = diccionario['favorite_count']

        lang = diccionario['lang']

        geo = diccionario['geo']

        lat, long = 0,0
        if geo != None:
            lat, long = geo['coordinates'][0], geo['coordinates'][1]

        print(id, created_at, lang, retweet_count, favorite_count,source, lat, long)

        text = diccionario['text']
        print("\t",id, text)


        hashtags = diccionario['entities']['hashtags']
        hashtags = '|'.join([hastag['text'] for hastag in hashtags ])
        print("\t", id, hashtags)

        keys = ['id','screen_name','favourites_count', 'friends_count', 'followers_count', 'location', 'created_at']
        valuesUser = ','.join([ str(diccionario['user'][key]) for key in keys])
        print("\t", id, valuesUser.encode('iso-8859-15', 'ignore').decode('iso-8859-15'))

    #     c = value
    #
    #     if c not in contador.keys():
    #         contador[c] = 1
    #     else:
    #         contador[c] += 1
    #
    # for c in contador.keys():
    #     print(c, contador[c])

leerArchivoNuevo()