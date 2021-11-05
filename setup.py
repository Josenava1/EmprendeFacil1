from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def template():
    return render_template("prueba.html")

@app.route('/form.html', methods=['GET'])
def formulario():
    return render_template("form.html")


@app.route('/calculosformulario', methods=['POST','GET'])
def calulosformulario():
    #recoleccion de datos
    nombre = request.args.get('nombre')
    unidadescompradas = request.args.get('unidadescompradas')

    return (render_template("resultadoform.html", nombre=nombre, unidadescompradas=unidadescompradas))

@app.route('/equipo.html')
def equipo():
    return render_template("equipo.html")

@app.route('/prueba.html')
def inicio():
    return render_template("prueba.html")

if __name__ =='__main__':
    #iniciar en modo debug
    app.run(debug=True)
