
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
    
    nombre = request.args.get('nombre')
    nombredetuemprendimento = request.args.get('nombredetuemprendimento')
    tipo_industria = request.args.get('tipo_industria')
    ingresomensual = request.args.get('ingresomensual')
    capitaldisponible = request.args.get('capitaldisponible')
    activos = request.args.get('activos')
    pagosueldos = request.args.get('pagosueldos')
    inversionprod = request.args.get('inversionprod')
    gastopublicidad = request.args.get('gastopublicidad')
    gastosop = request.args.get('gastosop')
    otrosgastos = request.args.get('otrosgastos')
    canalesventas = request.args.get('canalesventas')
    unidadescompradas = request.args.get('unidadescompradas')
    unidadesvendidas = request.args.get('unidadesvendidas')
    porcentajeaumento = request.args.get('porcentajeaumento')

    #DEFINIR
    pagosueldos= int(pagosueldos)
    inversionprod= int(inversionprod)
    gastopublicidad= int(gastopublicidad)
    gastosop= int(gastosop)
    otrosgastos= int(otrosgastos)
    ingresomensual= int(ingresomensual)
    unidadescompradas= int(unidadescompradas)
    unidadesvendidas= int(unidadesvendidas)
    porcentajeaumento=int(porcentajeaumento)
    canalesventas=int(canalesventas)
    activos=int(activos)
    capitaldisponible=int(capitaldisponible)



    
    #CÁLCULOS

    #1 GASTOS TOTALES
    gastototalrespuesta = pagosueldos + inversionprod + gastopublicidad + gastosop + otrosgastos
    gastototalrespuesta = int(gastototalrespuesta)

    #2 CUANTO ESTAS GANANDO REALMENTE
    gananciarealrespuesta = (ingresomensual - gastototalrespuesta) * 0.81
    gananciarealrespuesta = int(gananciarealrespuesta)

    #3 CUANTO PAGAS EN IMPUESTOS
    impuestosrespuesta = (ingresomensual - gastototalrespuesta) * 0.19
    impuestosrespuesta = int(impuestosrespuesta)

    #4 CAPACIDAD DE AHORRO pensando en un ahorro recomendado del 30% del ingreso
    capacidadahorrorespuesta = gananciarealrespuesta * 0.3
    capacidadahorrorespuesta = int(capacidadahorrorespuesta)

    #5 INVERION POR UNIDAD COMPRADA
    inversionporunidadrespuesta = inversionprod/unidadescompradas
    inversionporunidadrespuesta = int(inversionporunidadrespuesta)

    #6 GANANCIA REAl POR ARTICULO VENDIDO
    gananciaporunidadrespuesta = gananciarealrespuesta/unidadesvendidas
    gananciaporunidadrespuesta = int(gananciaporunidadrespuesta)

    #7 CALCULAR CUANTAS UNIDADES SE DEBEN VENDER PARA ALCANZAR EL OBJETIVO
    cuantasunidadesparaobjetivorespuesta =  (((ingresomensual *(1+(porcentajeaumento/100)))/gananciaporunidadrespuesta)-unidadesvendidas)
    cuantasunidadesparaobjetivorespuesta = int(cuantasunidadesparaobjetivorespuesta)

    #8 CUANTO HABRIA QUE INVERTIR EN INVENTARIO PARA ALCANZAR EL OBJETIVO
    invertirparaobjrespuesta = cuantasunidadesparaobjetivorespuesta * inversionporunidadrespuesta
    invertirparaobjrespuesta = int(invertirparaobjrespuesta)


    #9 CUANTO SE PUEDE INVERTIR POR CANAL DE VENTA
    inversionporcanalrespuesta = gananciarealrespuesta / canalesventas
    inversionporcanalrespuesta = int(inversionporcanalrespuesta)

    #10 CUANTAS UNIDADES QUEDAN EN INVENTARIO
    unidadesstockrespuesta = unidadescompradas - unidadesvendidas
    unidadesstockrespuesta = int(unidadesstockrespuesta)

    #11 SI SIGUES ASI POR 12 MESES, TU INVENTARIO AUMENTARÁ EN ___ EXISTENCIAS
    unidadesstockrespuestapor12meses = unidadesstockrespuesta * 12
    unidadesstockrespuestapor12meses = int(unidadesstockrespuestapor12meses)

    #12 INVERSIONES PORCENTUALES
    inversionporcentualensueldos = (pagosueldos/gastototalrespuesta)*100
    inversionporcentualensueldos= int(inversionporcentualensueldos)

    inversionporcentualenoperaciones = (gastosop/gastototalrespuesta)*100
    inversionporcentualenoperaciones= int(inversionporcentualenoperaciones)

    inversionporcentualenpublicidad = (gastopublicidad/gastototalrespuesta)*100
    inversionporcentualenpublicidad= int(inversionporcentualenpublicidad)

    inversionporcentualeninventario = (inversionprod/gastototalrespuesta)*100
    inversionporcentualeninventario= int(inversionporcentualeninventario)






    return (render_template("resultadoform.html", nombre=nombre, tipo_industria=tipo_industria, 
    ingresomensual=ingresomensual, capitaldisponible=capitaldisponible, activos=activos, pagosueldos=pagosueldos, 
    inversionprod=inversionprod, gastopublicidad=gastopublicidad, gastosop=gastosop, otrosgastos=otrosgastos, 
    canalesventas=canalesventas, unidadescompradas=unidadescompradas, unidadesvendidas=unidadesvendidas, porcentajeaumento=porcentajeaumento, 
    gastototalrespuesta=gastototalrespuesta, gananciarealrespuesta=gananciarealrespuesta, impuestosrespuesta=impuestosrespuesta, 
    capacidadahorrorespuesta=capacidadahorrorespuesta, gananciaporunidadrespuesta=gananciaporunidadrespuesta, cuantasunidadesparaobjetivorespuesta=cuantasunidadesparaobjetivorespuesta, 
    inversionporunidadrespuesta=inversionporunidadrespuesta, invertirparaobjrespuesta=invertirparaobjrespuesta, inversionporcanalrespuesta=inversionporcanalrespuesta,
    unidadesstockrespuesta=unidadesstockrespuesta, unidadesstockrespuestapor12meses=unidadesstockrespuestapor12meses, inversionporcentualensueldos=inversionporcentualensueldos,
    inversionporcentualenoperaciones=inversionporcentualenoperaciones, inversionporcentualenpublicidad=inversionporcentualenpublicidad, inversionporcentualeninventario=inversionporcentualeninventario ))

@app.route('/equipo.html')
def equipo():
    return render_template("equipo.html")

@app.route('/prueba.html')
def inicio():
    return render_template("prueba.html")

if __name__ =='__main__':
    #iniciar en modo debug
    app.run(debug=True)
