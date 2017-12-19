#git subtree push --prefix Bot heroku master

from flask import Flask, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def hello():

    return """Funciona :D"""


@app.route('/tele', methods=['POST'])
def telegram():
    print("Entra desde telegram")
    a = request.data
    b = json.loads(a)
    print("Cargo el mensaje")
    print(b)
    mensaje = b["message"]["text"]
    text = ""

    print("Entra a ver si hay un problema")
    if b["message"]["text"][0:17] == "Tengo un problema":
        text = "El programa recibio que tiene un problema"
        print("cambia el texto")

    if b["message"]["text"][0:5] == "Hola!":
        text = """Hola!

Soy SondaBot, Me indica su nombre porfavor?"""
        print("cambia el texto")

    if b["message"]["text"][0:10]  == "Juan Perez":
        text = "Me indica su nombre de contrato porfavor?"

    if b["message"]["text"][0:20] == "DSF_SISTEMAS TRADING":
        text = "Cual es su consulta?"

    if b["message"]["text"][0:40] == "No me actualizan mis datos en el sistema":
        text = "Me puede enviar una captura de pantalla al corredo OS@Sonda.cl, e ingresar enviado cuando se haya logrado"

    if b["message"]["text"][0:7] == "enviado":
        text = """Confirmo recepción

Me da un numero de contacto?"""

    if b["message"]["text"][0:12] == "+56991827364":
        text = """para seguimiento, su numero de OS creada es 45627, lo solucionaremos a la brevedad.

Muchas Gracias"""

    if b["message"]["text"][0:48]  == "Tengo un error en mi proceso de calculo de cuota":
        text = "Su problema se ha registrado, para completar el proceso ingrese su usuario:"

    if b["message"]["text"][0:21] == "Paola Cabezas Pizarro":
        text = """Posiblemente, su problema sea de un registro duplicado. De todas maneras, la orden de servicio ya se ha presentado a nuestro equipo, y estamos trabajando en ella ahora mismo"""

    form = {'chat_id': b["message"]["chat"]["id"], 'text': text}
    header = {'content-Type': 'application/json'}  # el header define el tipo de contenido
    r = requests.post('https://api.telegram.org/bot495424347:AAGM7XlCXne39odbh-aS95MyuBlkFpWBkuI/sendMessage',
                      headers=header, data=json.dumps(form))

    return "Cualquier Cosa"


if __name__ == '__main__':
    app.run()
