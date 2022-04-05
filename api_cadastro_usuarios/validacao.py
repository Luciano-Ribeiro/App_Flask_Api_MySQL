import jwt

def encode_jwt(dicionario):
    dados_codificados = jwt.encode(dicionario, key="minha-palavra-chave", algorithm='HS256')
    return dados_codificados

def decode_jwt(dicionario):
    dados_decodificados = jwt.decode(dicionario, key="minha-palavra-chave", algorithms='HS256')
    return dados_decodificados

