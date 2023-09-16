from app import app
from flask import render_template
from flask import request, flash, redirect

@app.route('/')
@app.route('/index', defaults={"nome":"utilizador"})
@app.route('/index/<nome>')
def index(nome):
    dados = {"Apilido": "Silva", "Idade": "26", "Profissão": "Engenheiro"}
    return render_template("index.html", nome= nome, dados=dados)


@app.route('/contact')
def contacto():
    return render_template("contacto.html")

@app.route('/login')
def login():
    return render_template("login.html")

"""
#metodo GET

@app.route('/autenticar', methods=['GET'])
def autenticar():
    utilizador = request.args.get('utilizador')
    senha = request.args.get('senha')
    return f'Utilizador: {utilizador} Senha: {senha}'
"""
@app.route('/autenticar', methods=['POST'])
def autenticar():
    utilizador = request.form.get('utilizador')
    senha = request.form.get('senha')
    if utilizador == "admin" and senha == "senha1234":
        return f'Utilizador: {utilizador} Senha: {senha}'
    else:
        flash ('dados inválidos')
        return redirect ('login')

@app.route('/calcular', methods=['POST', 'GET'])
def calcular():
    result = 0
    if request.method =='POST' and 'número_1' in request.form and 'número_2' in request.form:
        num_1 = float(request.form.get('número_1'))
        num_2  = float(request.form.get('número_2'))
        operacao = str(request.form['opr'])
        
        if operacao == 'add':
            result = num_1 + num_2
        elif operacao == 'sub':
            result = num_1 - num_2
        elif operacao == 'mul':
            result = num_1 * num_2
        elif operacao == 'div':
            result = num_1 / num_2
        
        
    return render_template('calculador.html', result=result)