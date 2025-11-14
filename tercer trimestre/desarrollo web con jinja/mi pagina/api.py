from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def menu():
    return render_template("menu.html", titulo="menu de la pagina")

@app.route("/prueba")
def prueba():
    return render_template("prueba.html", titulo="prueba")

@app.route("/a")
def a():
    return render_template("a.html", titulo="a")

@app.route("/b")
def b():
    return render_template("b.html", titulo="b")

@app.route("/formulario")
def formulario():
    return render_template("formulario.html", titulo="formulario")

if __name__ == "__main__":
    # host="0.0.0.0"
    # port=5080
    app.run(host="0.0.0.0", port=5080, debug=True)
