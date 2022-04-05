from flask import request
import requests
import jwt


def encode_jwt(dicionario):
    dados_codificados = jwt.encode(
        dicionario, key="minha-palavra-chave", algorithm='HS256')
    return dados_codificados


def decode_jwt(dicionario):
    dados_decodificados = jwt.decode(
        dicionario, key="minha-palavra-chave", algorithms='HS256')
    return dados_decodificados


def post_api(dados, link='http://127.0.0.1:5000/cadastro'):

    dados = encode_jwt(dados)
    requisicao = requests.post(link, json=dados)
    print(requisicao)




#if __name__ == "__main__":
    #post_api(dicionario)
