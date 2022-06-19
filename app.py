#Importamos la libreria Flask
from flask import Flask,  request, jsonify
import random

#Creación de una nueva instancia del servidor
app = Flask(__name__)

#Definimos el primer Path de la API: ruta y metodos del endpoint
#Decorador @, hace algo antes de una ejecución
@app.route("/", methods = ["GET", "POST"])
#Metodo que se llamara cuando el cliente haga el request a dicha ruta
#flask devolverá "Hello World, esto podría ser un string HTML o un string JSON.
def hello():
    if request.method == "GET":
        numero = random.randint(1, 10000)
        return "<h1>Hola mundo: {}</h1>".format(numero)
    if request.method == "POST":
        nombre = request.form['nombre']
        return "<h1>Hola {}</h1>".format(nombre)

@app.route("/endpoint2", methods = ["GET", "POST"])
def endpoint2():
    if request.method == "GET":
        return "<h2>Este es el <i>Segundo</i> endpoint con Flask</h2>"
    if request.method == "POST":
        apellido = request.form['apellido']
        return "<h2>Tu apellido es <i>{}</i>, verdad?</h2>".format(apellido)

@app.route("/endpoint3", methods = ["GET", "POST"])
def endpoint3():
    if request.method == "GET":
        return "<h2>Este es el <i>Tercer</i> endpoint con Flask</h2>"
    if request.method == "POST":
        edad = request.form['edad']
        return "<h2>Tambien se que tienes <i>{}</i> años</h2>".format(edad)

@app.route("/endpoint4", methods = ["GET", "POST"])
def endpoint4():
    if request.method == "GET":
        return "<h2>Este es el <i>Cuarto</i> endpoint con Flask</h2>"
    if request.method == "POST":
        telefono = request.json['telefono']
        #jsonify() es un método auxiliar proporcionado por Flask para devolver correctamente los datos JSON
        return jsonify({
            'response': "tu numero es " + telefono
        })
    

@app.route("/endpoint5", methods = ["GET", "POST"])
def endpoint5():
    if request.method == "GET":
        return "<h2>Este es el <i>Quinto</i> endpoint con Flask</h2>"
    if request.method == "POST":
        nombre = request.json['nombre']
        apellido = request.json['apellido']
        edad = request.json['edad']
        telefono = request.json['telefono']
        return jsonify({
            "nombre" : nombre,
            "apellido" : apellido,
            "edad" : edad,
            "telefono" : telefono
            
        })
        
#Metodo main donde finalmente iniciamos el servidor en el localhost.
if __name__ == "__main__":
    app.run(debug=True)