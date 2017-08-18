#coding:latin-1

def ubicacionGuayaquil():
    ubicacion = (-2.1709979, -79.92235920000002)
    return  ubicacion

#ciudad, tiempo en carro, tiempo en avión, latitud, longitud
def ciudadesDesdeGuayaquil():
    listaCiudades = [
        ("Salinas",2,6, -2.2233633, -80.958462),
        ("Machalilla",2.44,12,-1.4760749, -80.7643952),
        ("Daule",0.56,2,-1.86218, -79.97766899999999 ),
        ("Ingapirca",2.17, 12,-2.548985, -78.8714679),
        ("Durán",0.19,2,-2.173333, -79.83111099999996),
        ("Nobol",0.34, 2, -1.916671, -80.01153899999997),
        ("Gualaceo",3.46,12,-2.9, -78.78333299999997 ),
        ("Canoa", 4.10, 18, -0.463631, -80.45365),
        ("Riobamba",3.02, 12, -1.6734849, -78.647992),
        ("Quito",5.03, 18,-0.223151, -78.512677),
        ("Ambato",3.39,12,-1.2416667, -78.6197222),
        ("Montañita",3.30,12,-0.866667, -80.266667),
        ("Santa Elena",2.50,6,-2.1934804, -80.543845),
        ("Loja",5.04,18,-3.990138, -79.20446 ),
        ("Bahía de Caráquez",3.52,12,-0.608935, -80.431023)

    ]

    return listaCiudades


#ciudad, número de hoteles, ranking/5, cercano al mar, etiquetas
def datosCiudades():
    listaCiudades = [
        ("Salinas", "300", 3.4, True, "#vacaciones #playa #mojitos #atardecer"),
        ("Machalilla", "260", 3.0, True, "#nomevuelvoaenamorar #vacaciones #mojitos #playa"),
        ("Daule", "24", 2.7, False, "#obras #friends #salud"),
        ("Ingapirca", "5", 4.2, False, "#ruinas #incas #sol #achachay"),
        ("Durán", "120", 3.2, False, "#tren #fritada #malecón #puente"),
        ("Nobol", "82", 3.0, False, "#maduroconqueso #narcisita #campo #calor"),
        ("Gualaceo", "92", 2.9, False, "#termas #achachay #cuenquita #cuy"),
        ("Canoa", "12", 3.1, True, "#mar #atardecer #corviche #manabí"),
        ("Riobamba", "130", 3.5, False,"#achachay #hornado #cafecito"),
        ("Quito", "310", 3.6, False, "#achachay #mitaddelmundo #laronda #frío"),
        ("Ambato", "130", 2.9, False, "#pan #ferialibre #achachay #frío" ),
        ("Montañita", "250", 3.1, True, "#cocteles #nolehagoaeso #hastaabajo #mojitos #nomevuelvoaenamorar #playa"),
        ("Loja", "180", 3.0, False, "#cantaclaro #frío #achachay #bonito"),
        ("Bahía de Caráquez", "190", 3.1, True, "#playa #atardecer #ballenas #snorkel" )
    ]

    return listaCiudades
