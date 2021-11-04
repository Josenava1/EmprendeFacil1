
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def template():
    return render_template("prueba.html")

@app.route('/informacion.html')
def informacion():
    return render_template("informacion.html")


@app.route('/form.html', methods=['GET'])
def formulario():
    return render_template("form.html")


@app.route('/calculosformulario', methods=['POST','GET'])
def calulosformulario():

    #recoleccion de datos
    
    nombre = request.form.get('nombre')
    nombredetuemprendimento = request.form.get('nombredetuemprendimento')
    country = request.form.get('country')
    ingresomensual = request.form.get('ingresomensual')
    capitaldisponible = request.form.get('capitaldisponible')
    activos = request.form.get('activos')
    pagosueldos = request.form.get('pagosueldos')
    inversionprod = request.form.get('inversionprod')
    gastopublicidad = request.form.get('gastopublicidad')
    gastosop = request.form.get('gastosop')
    otrosgastos = request.form.get('otrosgastos')
    canalesventas = request.form.get('canalesventas')
    unidadescompradas = request.form.get('unidadescompradas')
    unidadesvendidas = request.form.get('unidadesvendidas')
    porcentajeaumento = request.form.get('porcentajeaumento')

    return render_template("resultadoform.html")

@app.route('/equipo.html')
def equipo():
    return render_template("equipo.html")

@app.route('/prueba.html')
def inicio():
    return render_template("prueba.html")

if __name__ =='__main__':
    #iniciar en modo debug
    app.run(debug=True)
