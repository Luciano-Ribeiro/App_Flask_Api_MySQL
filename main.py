from typing import Dict, Any, Union

from flask import Flask, render_template, request, redirect, session
import time
from validacao import modifica_senha, check_password_hash
from acessa_api import post_api
from acessa_api import decode_jwt, encode_jwt

app = Flask(__name__, template_folder=('templates'))

app.secret_key = modifica_senha('minha senha')

nome = ""
list = []
dados_cadastro = {}
dados_editados = {}
login_usuario = {}
email = ''
dados_usuario = {}
session = {'nome': 'None'}


@app.route("/")
def home():
    return render_template("home.html")


@app.route('/', methods=['POST'])
def form_login():
    login_usuario["email"] = request.form['email']
    login_usuario["password"] = request.form['password']
    print(f'esse é o login {login_usuario}')
    login = {'email':login_usuario['email'], "tipo":"login"}
    post_api(login, link='http://127.0.0.1:5000/login')
    time.sleep(1)
    return redirect('/login')


@app.route('/api', methods=['POST', 'GET'])
def get_usuario_api():
    dados_api = request.get_json(force=True)
    print(f' Esses foram os dados recebidos no /api {dados_api}')
    print(decode_jwt(dados_api))
    dados_api = decode_jwt(dados_api)
    autentica_senha = check_password_hash(dados_api['senha'], login_usuario['password'])
    if dados_api['nome'] == "None":
        return render_template("home.html")
    if login_usuario['email'] == dados_api['email'] and autentica_senha:
        session['nome'] = dados_api['nome']
        session['email'] = dados_api['email']
        session['senha'] = dados_api['senha']
        print(session)
        return redirect('/login'), dados_api
    return redirect('/')


@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")


@app.route("/cadastro", methods=['POST'])
def form_cadastro():
    dados_cadastro['nome'] = request.form['nome']
    dados_cadastro['email'] = request.form['email_cadastro']
    dados_cadastro['pais'] = request.form['pais']
    dados_cadastro['estado'] = request.form['estado']
    dados_cadastro['municipio'] = request.form['municipio']
    dados_cadastro['cep'] = request.form['cep']
    dados_cadastro['rua'] = request.form['rua']
    dados_cadastro['numero'] = request.form['numero']
    dados_cadastro['complemento'] = request.form['complemento']
    cpf = request.form['cpf']
    dados_cadastro['cpf'] = request.form['cpf']
    dados_cadastro['pis'] = request.form['pis']
    senha_form = request.form['senha']
    dados_cadastro['senha'] = modifica_senha(senha_form)
    print(senha_form)
    print(dados_cadastro)
    post_api(dados_cadastro)

    return redirect("/", cadastrado="O usuario foi cadastrado")


@app.route("/editar", methods=['POST', 'GET'])
def editar():
    return render_template("editar.html")


@app.route("/editar", methods=['POST'])
def form_editar():
    dados_editados = {}
    dados_editados['nome'] = request.form['nome']
    dados_editados['email'] = session['email']
    dados_editados['pais'] = request.form['pais']
    dados_editados['estado'] = request.form['estado']
    dados_editados['municipio'] = request.form['municipio']
    dados_editados['cep'] = request.form['cep']
    dados_editados['rua'] = request.form['rua']
    dados_editados['numero'] = request.form['numero']
    dados_editados['complemento'] = request.form['complemento']
    dados_editados['cpf'] = request.form['cpf']
    dados_editados['pis'] = request.form['pis']
    dados_editados['senha'] = session['senha']
    print(dados_editados)
    post_api(dados_editados, link='http://127.0.0.1:5000/editar')
    return redirect("/login")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if session['nome'] != "None":
        return render_template('usuario.html', session=session['nome'])
    else:
        return "<h1> Você não esta logado, faça o login para obter acesso</h1>"


@app.route('/logout', methods=['GET'])
def logout():
    session['nome'] = 'None'
    return redirect('/')


@app.route('/excluir', methods=['GET'])
def excluir_usuario():
    print(session)
    post_api(session, link='http://127.0.0.1:5000/excluir')
    session['nome'] = 'None'
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True, port=3000)
