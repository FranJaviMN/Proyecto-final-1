#En este ejercicio vamos a obtener todos los herores disponibles en la api que usamos, para ello el ussuario debe de introducir que clase
#quiere consultar, si solo quiere verr tdoos los heroes no debera introducir nada.


import requests
import os
key=os.environ["clave_propia"]
#payload = {"locale=es_ES":"es_ES"}
headers={"Authorization":"bearer "+key}
URL_BASE_CARTAS = "https://us.api.blizzard.com/"
URL_BASE_PARAMETROS = "https://us.api.blizzard.com/hearthstone/metadata/"


