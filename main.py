from flask import Flask, render_template, request
from flask.templating import render_template

app = Flask(__name__)

@app.route("/")
def mainPage():
    return render_template('index.html')

@app.route("/equipo")
def teamPage():
    return render_template('equipo.html')

@app.route("/precios")
def preciosPage():
    return render_template('precios.html')

@app.route("/ubicacion")
def mapPage():
    return render_template('ubicacion.html')

@app.route("/ubicacion_variable", methods=['POST'])
def mapPage_variable():
    linkmapas=["?pb=!1m18!1m12!1m3!1d3957.047007198271!2d-70.70399097013896!3d-33.4892343256583!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x9662c4b06a0a9777%3A0xb3321d1fb943bcbe!2sPiloto%20Lazo%20120%2C%20Cerrillos%2C%20Regi%C3%B3n%20Metropolitana!5e0!3m2!1ses-419!2scl!4v1636048356562!5m2!1ses-419!2scl", "?pb=!1m14!1m8!1m3!1d13318.228969046637!2d-70.7285094!3d-33.4347858!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x3f8db00dcdfd1518!2sFarmacia%20Popular%20Cerro%20Navia!5e0!3m2!1ses-419!2scl!4v1636048411922!5m2!1ses-419!2scl"]
    comuna=int(request.form['comuna'])
    print(comuna)
    return render_template("ubicacion.html", mapcomuna=linkmapas[comuna])

if __name__ == "__main__":
    app.run(debug=True)