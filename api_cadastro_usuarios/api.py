from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import json
from validacao import encode_jwt, decode_jwt
import requests


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456789@localhost/banco_teste'

db = SQLAlchemy(app)

dados_dict={}

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    pais = db.Column(db.String(50))
    estado = db.Column(db.String(50))
    municipio = db.Column(db.String(50))
    cep = db.Column(db.String(100))
    rua = db.Column(db.String(100))
    numero = db.Column(db.String(10))
    complemento = db.Column(db.String(50))
    cpf = db.Column(db.String(25))
    pis = db.Column(db.String(25))
    senha = db.Column(db.String(200))

# db.create_all() para criar a tabela no terminal


@app.route('/login', methods=['POST', 'GET'])
def login():
    dados = request.get_json(force=True)
    print(dados)
    print(decode_jwt(dados))
    dados = decode_jwt(dados)
    usuarios = Usuario.query.filter_by(email=dados['email']).first()
    print(usuarios)
    if usuarios != None:
        dados_dict = {}
        dados_dict['nome'] = usuarios.nome
        dados_dict['email'] = usuarios.email
        dados_dict['pais'] = usuarios.pais
        dados_dict['estado'] = usuarios.estado
        dados_dict['municipio'] = usuarios.municipio
        dados_dict['rua'] = usuarios.rua
        dados_dict['cep'] = usuarios.cep
        dados_dict['numero'] = usuarios.numero
        dados_dict['complemento'] = usuarios.complemento
        dados_dict['cpf'] = usuarios.cpf
        dados_dict['pis'] = usuarios.pis
        dados_dict['senha'] = usuarios.senha

        post_cadastro_web(dados_dict)
        if dados["tipo"] == "consulta":
            post_cadastro_web(dados_dict, link='http://127.0.0.1:3000/editar')
    else:
        usuarios_dict = {"nome":"None"}
        post_cadastro_web(usuarios_dict)

    return "200"


@app.route('/cadastro', methods=['POST'])
def recebe_cadastro():
    dados = request.get_json(force=True)
    print(dados)
    print(decode_jwt(dados))
    dados = decode_jwt(dados)
    print('decodificação ok')
    add_dados_cadastro = Usuario(nome=dados['nome'], email=dados['email'], pais=dados['pais'],estado=dados['estado'],
                                 municipio=dados['municipio'],cep=dados['cep'], rua=dados['rua'], numero=dados['numero'],
                                 complemento=dados['complemento'],cpf=dados['cpf'], pis=dados['pis'], senha=dados['senha'])
    db.session.add(add_dados_cadastro)
    db.session.commit()
    print('dados salvos')
    return f'dados salvos'

@app.route('/editar', methods=['POST',"GET"])
def editar():
    dados = request.get_json(force=True)
    print(f'dados para editar {dados}')
    print(decode_jwt(dados))
    dados = decode_jwt(dados)
    usuarios = Usuario.query.filter_by(email=dados['email']).first()
    add_dados_editados = Usuario(nome=dados['nome'], email=usuarios.email, pais=dados['pais'],estado=dados['estado'],
                                 municipio=dados['municipio'],cep=dados['cep'], rua=dados['rua'], numero=dados['numero'],
                                 complemento=dados['complemento'],cpf=dados['cpf'], pis=dados['pis'], senha=usuarios.senha)
    db.session.add(add_dados_editados)
    db.session.commit()
    print('dados editados')
    return f'dados editados'

@app.route('/')
def home():
    return 'a api ok'


def post_cadastro_web(dados, link='http://127.0.0.1:3000/api'):

    dados = encode_jwt(dados)
    print(f'os dados foram mudados {dados}')
    requisicao = requests.post(link, json=dados)
    print(f'Essa é a requisição para a web{requisicao}')

@app.route('/excluir', methods=['POST'])
def excluir_usuario():

    delete = request.get_json(force=True)
    print(delete)
    print(decode_jwt(delete))
    delete = decode_jwt(delete)
    usuarios = Usuario.query.filter_by(email=delete['email']).first()
    db.session.delete(usuarios)
    db.session.commit()
    return "200"




if __name__ == "__main__":
    app.run(debug=True)


