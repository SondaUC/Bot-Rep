from flask import Flask, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def hello():

    return """Ganzos y patos han tenido guerras interminables las cuales
solo han tenido como resultado el caos y la destruccion.

La comida escasea, y las familias de ambos lados sufren, amor y traicion existe entre los ganzos y patos,
y solo el poder de los asados determinara quien de los 2 partidos sera el vencedor
(Es porque el que cacha como hacer asados se puede hacer el tremendo festin con el otro)
(Pd: equis de xD)"""


if __name__ == '__main__':
    app.run()
