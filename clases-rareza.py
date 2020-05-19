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