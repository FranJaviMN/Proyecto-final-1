#En este ejercicio vamos a realizar una consulta a nuestra api donde el usuario pondra por teclado un personaje, palabra, o comienzo de una cadena
#para buscar en la api que personajes coinciden para asi, mostrar por pantalla las cartas junto a sus imagenes.

import requests
import os
key=os.environ["clave_propia"]
#payload = {"locale=es_ES":"es_ES"}
headers={"Authorization":"bearer "+key}
URL_BASE_CARTAS = "https://us.api.blizzard.com/"
