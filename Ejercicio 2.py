#En este ejercicio vamos a realizar una consulta a nuestra api donde el usuario pondra por teclado un personaje, palabra, o comienzo de una cadena
#para buscar en la api que personajes coinciden para asi, mostrar por pantalla las cartas junto a sus imagenes.

import requests
import os
key=os.environ["clave_propia"]
#payload = {"locale=es_ES":"es_ES"}
headers={"Authorization":"bearer "+key}
URL_BASE_CARTAS = "https://us.api.blizzard.com/"

#En esta parte le vamos a pedir al usuario que nos de que palabra o personaje quiere buscar en la api.

palabra_clave=str(input('Dime que palabra o personaje quieres buscar: '))

peticion_cartas=requests.get(URL_BASE_CARTAS+"hearthstone/cards?locale=es_ES&textFilter="+palabra_clave,headers=headers)

if peticion_cartas.status_code == 200:
    lista_coincidencias=[]
    doc_cartas=peticion_cartas.json()
    while doc_cartas['cardCount'] == 0:
        print('No hay coincidencias, intentela de nuevo')
        palabra_clave=str(input('Dime que palabra o personaje quieres buscar: '))
        peticion_cartas=requests.get(URL_BASE_CARTAS+"hearthstone/cards?locale=es_ES&textFilter="+palabra_clave,headers=headers)
        doc_cartas=peticion_cartas.json()
    for cartas in doc_cartas['cards']:
        print(cartas['name']+' Imagen: '+cartas['image'])
else:
    print('Error, no se ha podido obtener la informacion')