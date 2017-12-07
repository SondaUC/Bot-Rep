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

        if b["message"]["text"][0:5] == "Start":
            text = """Hola!

Soy SondaBot, en que te puedo ayudar?"""
            print("cambia el texto")

        if b["message"]["text"][0:48]  == "Tengo un error en mi proceso de calculo de cuota":
            text = "Su problema se ha registrado, para completar el proceso ingrese su usuario"

        if b["message"]["text"][0:21] == "Paola Cabezas Pizarro":
            text = """Posiblemente, su problema sea de un registro duplicado. De todas maneras,
la orden de servicio ya se ha presentado a nuestro equipo, y estamos trabajando en ella ahora mismo"""

    form = {'chat_id': b["message"]["chat"]["id"], 'text': text}
    header = {'content-Type': 'application/json'}  # el header define el tipo de contenido
    r = requests.post('https://api.telegram.org/bot495424347:AAGM7XlCXne39odbh-aS95MyuBlkFpWBkuI/sendMessage',
                      headers=header, data=json.dumps(form))

    return "Cualquier Cosa"


if __name__ == '__main__':
    app.run()
