#En este ejercicio vamos a consultar el nombre de las cartas de nuestra API. Para ello le mostraremos al usuario una serie de parametros
#que puede rellenar o no, dependiendo de lo que rellene se le mostraran unas cartas u otras.

import requests
import os
key=os.environ["clave_propia"]
#payload = {"locale=es_ES":"es_ES"}
headers={"Authorization":"bearer "+key}
URL_BASE_CARTAS = "https://us.api.blizzard.com/"
URL_BASE_PARAMETROS = "https://us.api.blizzard.com/hearthstone/metadata/"


#EN esta parte realizamos una peticion a la api donde se encuentran todos los parametros que podemos usar para filtrar las cartas, en mi caso
#solo voy a usar dos de ellos que en este caso seran las clases disponibles y la rareza de las cartas de dicha clase.

#Primero realizamos la peticion para obtener las clases.

peticion_classes=requests.get(URL_BASE_PARAMETROS+"classes?locale=es_ES",headers=headers)

if peticion_classes.status_code == 200:
    print("Las clases disponibles son las siguientes: ")
    lista_clases=[]
    doc_classes = peticion_classes.json()
    for clas in doc_classes:
        print(clas["slug"])
        lista_clases.append(clas["slug"])


    lista_clases.append("")

    elec_class=str(input("Dime la clase que quieres consultar(Si quieres consultar todas las clases dejar vacio): "))
    print()

    while elec_class not in lista_clases:
        print("Clases disponibles")
        for clas in lista_clases:
            print(clas)
        elec_class=str(input("Introduzca una de las clases disponibles, si quieres consultarlas todas dejar en blanco: "))
else:
    print("Fallo al obtener las clases, saltando campo...")
    elec_class=""

#Segundo una peticion para que nos muestre las rarezas disponibles

peticion_rareza=requests.get(URL_BASE_PARAMETROS+"rarities?locale=es_ES",headers=headers)

if peticion_rareza.status_code == 200:
    lista_rarezas=[]
    print("Las rarezas de cartas disponibles son las siguientes: ")
    doc_rarezas=peticion_rareza.json()
    for rareza in doc_rarezas:
        print(rareza["slug"])
        lista_rarezas.append(rareza["slug"])
    lista_rarezas.append("")

    elec_rareza=str(input("Dime que tipo de rareza de cartas quieres consultar, si quieres consultar todas dejar en blanco: "))

    while elec_rareza not in lista_rarezas:
        print("Rarezas disponibles")
        for rareza in lista_rarezas:
            print(rareza)
        elec_rareza=str(input("Dime que tipo de rareza de cartas quieres consultar, si quieres consultar todas dejar en blanco: "))
else:
    print("Fallo al obtener las rarezas, saltando campo...")
    elec_rareza=""

#En esta parte de nuestro ejercicio vemos que tenemos 4 posibles casos dependiendo de las elecciones que hayamos hecho en las preguntas
#anteriores. Asi se procedera a mostrar todos los nombres de las cartas que coincidan con lo que hayamos elegido.

print("Las cartas que coinciden con las busqueda son las siguientes: ")
    
if elec_rareza == "" and elec_class == "":
    peticion_todas_cartas=requests.get(URL_BASE_CARTAS+"hearthstone/cards?locale=es_ES&page=1",headers=headers)
    doc_cartas=peticion_todas_cartas.json()
    for cartas in doc_cartas["cards"]:
        print(cartas["name"])
    print("Pagina", doc_cartas["page"], "de", doc_cartas["pageCount"])
    print()

#Al haber en muchos de los casos varias paginas de cartas, el usuario vera solo la primera pagina, luego se le preguntara si 
#Quiere ver la siguiente pagina, en caso contrario el programa terminara.

    eleccion=str(input("¿Quiere continua a la siguiente pagina? Si/No: "))
    pagina=2
    while eleccion == "Si" and pagina < doc_cartas["pageCount"]:
        peticion_todas_cartas=requests.get(URL_BASE_CARTAS+"hearthstone/cards?locale=es_ES&page="+str(pagina),headers=headers)
        doc_cartas=peticion_todas_cartas.json()
        for cartas in doc_cartas["cards"]:
            print(cartas["name"])
        print("Pagina", pagina, "de", doc_cartas["pageCount"])
        eleccion=str(input("¿Quiere continua a la siguiente pagina? Si/No: "))
        pagina=pagina+1
        
elif elec_class != "" and elec_rareza != "":
    peticion_todas_cartas=requests.get(URL_BASE_CARTAS+"hearthstone/cards?locale=es_ES&class="+elec_class.lower()+"&rarity="+elec_rareza.lower(),headers=headers)
    doc_cartas=peticion_todas_cartas.json()
    for cartas in doc_cartas["cards"]:
        print(cartas["name"])
    print("Pagina", doc_cartas["page"], "de", doc_cartas["pageCount"])
    print()
    eleccion=str(input("¿Quiere continua a la siguiente pagina? Si/No: "))
    pagina=2
    while eleccion == "Si" and pagina < doc_cartas["pageCount"]:
        peticion_todas_cartas=requests.get(URL_BASE_CARTAS+"hearthstone/cards?locale=es_ES&page="+str(pagina)+"class="+elec_class.lower()+"&rarity="+elec_rareza.lower(),headers=headers)
        doc_cartas=peticion_todas_cartas.json()
        for cartas in doc_cartas["cards"]:
            print(cartas["name"])
        print("Pagina", pagina, "de", doc_cartas["pageCount"])
        eleccion=str(input("¿Quiere continua a la siguiente pagina? Si/No: "))
        pagina=pagina+1

elif elec_class == "" and elec_rareza != "":
    peticion_todas_cartas=requests.get(URL_BASE_CARTAS+"hearthstone/cards?locale=es_ES&class="+elec_class.lower()+"&rarity="+elec_rareza.lower(),headers=headers)
    doc_cartas=peticion_todas_cartas.json()
    for cartas in doc_cartas["cards"]:
        print(cartas["name"])
    print("Pagina", doc_cartas["page"], "de", doc_cartas["pageCount"])
    print()
    eleccion=str(input("¿Quiere continua a la siguiente pagina? Si/No: "))
    pagina=2
    while eleccion == "Si" and pagina <= doc_cartas["pageCount"]:
        peticion_todas_cartas=requests.get(URL_BASE_CARTAS+"hearthstone/cards?locale=es_ES&page="+str(pagina)+"class="+elec_class.lower()+"&rarity="+elec_rareza.lower(),headers=headers)
        doc_cartas=peticion_todas_cartas.json()
        for cartas in doc_cartas["cards"]:
            print(cartas["name"])
        print("Pagina", pagina, "de", doc_cartas["pageCount"])
        eleccion=str(input("¿Quiere continua a la siguiente pagina? Si/No: "))
        pagina=pagina+1

        
else:
    peticion_todas_cartas=requests.get(URL_BASE_CARTAS+"hearthstone/cards?locale=es_ES&class="+elec_class.lower()+"&rarity="+elec_rareza.lower(),headers=headers)
    doc_cartas=peticion_todas_cartas.json()
    for cartas in doc_cartas["cards"]:
        print(cartas["name"])
    print("Pagina", doc_cartas["page"], "de", doc_cartas["pageCount"])
    print()
    eleccion=str(input("¿Quiere continua a la siguiente pagina? Si/No: "))
    pagina=2
    while eleccion == "Si" and pagina <= doc_cartas["pageCount"]:
        peticion_todas_cartas=requests.get(URL_BASE_CARTAS+"hearthstone/cards?locale=es_ES&page="+str(pagina)+"class="+elec_class.lower()+"&rarity="+elec_rareza.lower(),headers=headers)
        doc_cartas=peticion_todas_cartas.json()
        for cartas in doc_cartas["cards"]:
            print(cartas["name"])
        print("Pagina", pagina, "de", doc_cartas["pageCount"])
        eleccion=str(input("¿Quiere continua a la siguiente pagina? Si/No: "))
        pagina=pagina+1
