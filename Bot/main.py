#git subtree push --prefix Bot heroku master

from flask import Flask, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def hello():

    return """Funciona :D"""


@app.route('/telegram', methods=['POST'])
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

    form = {'chat_id': b["message"]["chat"]["id"], 'text': text}
    header = {'content-Type': 'application/json'}  # el header define el tipo de contenido
    r = requests.post('https://api.telegram.org/bot402191911:AAFH1X4HxsZny4eVvp3_vLxiSzQe2McsIdU/sendMessage',
                      headers=header, data=json.dumps(form))

    return "Cualquier Cosa"


if __name__ == '__main__':
    app.run()
