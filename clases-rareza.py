#En este ejercicio vamos a consultar el nombre de las cartas de nuestra API. Para ello le mostraremos al usuario una serie de parametros
#que puede rellenar o no, dependiendo de lo que rellene se le mostraran unas cartas u otras.

import requests
import os
key=os.environ["clave_propia"]
#payload = {"locale=es_ES":"es_ES"}
headers={"Authorization":"bearer "+key}
URL_BASE_CARTAS = "https://us.api.blizzard.com/"
URL_BASE_PARAMETROS = "https://us.api.blizzard.com/hearthstone/metadata/"