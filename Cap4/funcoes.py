def perguntar():
    resposta = input(
        "O que deseja realizar?\n" + 
        "<I> - Para Inserir um usuário\n" +
        "<P> - Para Pesquisar um usuário\n" + 
        "<E> - Para Excluir um usuário\n" +
        "<L> - Para Listar um usuário\n"
    ).upper()

    return resposta

def inserir(dicionario):
    login = input ("Digite seu login: ").upper()
    dicionario[login]= [input("Digite seu nome: ").upper(),
                     input("Digite sua última data de acesso: "),
                     input("Digite sua estação: ")]

def pesquisar(dicionario, chave):
    lista=dicionario.get(chave)
    if lista!=None:
        print("Nome...........: " + lista[0])
        print("Último acesso..: " + lista[1])
        print("Última estação.: " + lista[2])

def excluir(dicionario, chave):
    if dicionario.get(chave)!=None:
        del dicionario[chave]
    print("Objeto Eliminado")

def listar(dicionario):
    for chave, valor in dicionario.items():
        print("Objeto......")
        print("Login: ", chave)
        print("Dados: ", valor)    


"""
def pesquisar(dicionario):
    login = input("Digite o login que gostaria de pesquisar: ").upper()
    print("Dados: ", dicionario.get(login))

def excluir (dicionario):
    login = input("Digite o login que deseja excluir: ").upper()
    print("Excluindo: ", dicionario.get(login))
    dicionario.pop(login)

def listar(dicionario):
    print("Dados: ", dicionario)
"""   
