from flask import Flask, request
from genero import main as getGenero

app = Flask("MetalZap")

@app.route("/genero", methods=["POST"])
def genero():
    banda = request.get_json()["banda"]
    genero = getGenero(banda)
    return genero

app.run()