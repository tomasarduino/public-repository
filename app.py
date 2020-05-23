from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/")  
def index():
	titulo = "Cauchos"  
	lista = ["Marca","Dimiensiones","Precio","Disponibilidad"]
	return render_template("index.html", titulo = titulo, lista = lista) 

@app.route("/youtube")
def go_to_youtube():
	return redirect("https://www.youtube.com/")

@app.route("/signup", methods=["GET","POST"])
def signup():
	if request.method == "POST":
		return redirect(url_for("/"))
	return render_template("signup.html")

if __name__ == "__main__":
	app.run(debug=True, port=3000)