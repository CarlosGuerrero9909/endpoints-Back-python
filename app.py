from flask import Flask,request
import random

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def hello():
    if request.method == "GET":
        numero = random.randint(1, 10000)
        return "Hola mundo: {}".format(numero)
    if request.method == "POST":
        nombre = request.form['nombre']
        return "Hola {}".format(nombre)

if __name__ == "__main__":
    app.run(debug=True)