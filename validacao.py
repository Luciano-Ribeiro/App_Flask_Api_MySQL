
from werkzeug.security import generate_password_hash, check_password_hash

cpf = "111.111.111-11"


def valida_cpf(cpf):
    #verifica se cpf é um numero
  
    if "." or "-":
        cpf_tratado = cpf.replace('.',"").replace("-","")
    tamanho = len(cpf_tratado)
    cpf = int(cpf_tratado)
    if tamanho != 11:
        return print("Favor escrever um cpf válido")


        


valida_cpf(cpf)


def modifica_senha(senha_cadastro):
    senha_hash = generate_password_hash(senha_cadastro, salt_length=6)
    return senha_hash

def check_senha_modificada(senha_hash, senha_login):

    flag = check_password_hash(senha_hash, senha_login)
    print(flag)
    return flag
