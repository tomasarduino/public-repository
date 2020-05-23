from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")   ##direccion de la ruta final##
def index():
	titulo = "HOME"  ##Definiendo variable##
	lista = ["Marca","Dimiensiones","Precio","Disponibilidad"] ##Definiendo una lista
	return render_template("index.html", titulo = titulo, lista = lista) ##Mostrando variable "titulo" en conjunto con indexx.html##

if __name__ == "__main__":
	app.run(debug=True, port=3000)