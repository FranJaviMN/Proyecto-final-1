#En este ejercicio vamos a obtener todos los herores disponibles en la api que usamos, para ello el ussuario debe de introducir que clase
#quiere consultar, si solo quiere verr tdoos los heroes no debera introducir nada.


import requests
import os
key=os.environ["clave_propia"]
#payload = {"locale=es_ES":"es_ES"}
headers={"Authorization":"bearer "+key}
URL_BASE_CARTAS = "https://us.api.blizzard.com/"
URL_BASE_PARAMETROS = "https://us.api.blizzard.com/hearthstone/metadata/"

#Aqui vamos a hacer la peticion de clases disponibles, si se hace bien se seguira el proceso, sino, saldra del programa

peticion_classes=requests.get(URL_BASE_PARAMETROS+"classes?locale=es_ES",headers=headers)

if peticion_classes.status_code == 200:
    print("Las clases disponibles son las siguientes: ")
    lista_clases=[]
    doc_classes = peticion_classes.json()
    for clas in doc_classes:
        lista_clases.append(clas["slug"])
        print(clas['slug'])
    lista_clases.append("")
    eleccion=str(input('Dime que clase quieres consultar(pulsar enter para ver todo): '))
    print()
    while eleccion not in lista_clases:
        print('Clase no encontrada')
        for clas in lista_clases:
            print(clas)
        eleccion=str(input('Dime que clase quieres usar(dejar en blanco si quieres ver todas): '))
        
#Aqui vamos a hacer la consulta sobre la clase que hayamos elegido, al haber dos posibilidades debemos de dividir en dos, la primera
#cuando queremos ver todos los heroes y la segunda cuando hemos introducido una clase.
    if eleccion == "":
        peticion_heroes=requests.get(URL_BASE_CARTAS+"hearthstone/cards?locale=es_ES&type=hero", headers=headers)
        if peticion_heroes.status_code == 200:
            print('Estos son todos los heroes: ')
            doc_heores = peticion_heroes.json()
            for heroes in doc_heores['cards']:
                print(heroes['name']+' Enlace para ver la imagen de la carta: '+heroes['image'])
    else:
        peticion_heroes=requests.get(URL_BASE_CARTAS+"hearthstone/cards?locale=es_ES&type=hero&class="+eleccion, headers=headers)
        if peticion_heroes.status_code == 200:
            print('Estos son todos los heroes: ')
            doc_heores = peticion_heroes.json()
            for heroes in doc_heores['cards']:
                print(heroes['name']+' Enlace para ver la imagen de la carta: '+heroes['image'])
            
else:
    print('ERROR AL OBTENER INFORMACION, INTENTE DE NUEVO')

