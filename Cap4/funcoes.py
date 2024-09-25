def perguntar():
    resposta = input(
        "<I> - Para Inserir um usuário\n" +
        "<P> - Para Pesquisar um usuário\n" + 
        "<E> - Para Excluir um usuário\n" +
        "<L> - Para Listar um usuário\n" +
        "O que deseja realizar?\n"
    ).upper()

    return resposta

def inserir(dicionario):
    login = input ("Digite seu ID de Funcionário: ").upper()
    dicionario[login]= [input("Digite seu nome: ").upper(),
                     input("Digite o nível de acesso: "),
                     input("Digite sua última data de acesso: "),
                     input("Digite a hora do último acesso: "),
                     input("Digite sua estação: "),
                     print("\n")]

def pesquisar(dicionario, login):
    lista=dicionario.get(login)
    if lista!=None:
        print("Nome...........: " + lista[0])
        print("Nível de acesso: " + lista[1])
        print("Último acesso..: " + lista[2] + " "+ lista[3])
        print("Última estação.: " + lista[4])
        print("\n")

def excluir(dicionario, login):
    if dicionario.get(login)!=None:
        del dicionario[login]
    print("ID eliminado")
    print("\n")

def listar(dicionario):
    for login, valor in dicionario.items():
        print("ID: ", login)
        print("Dados: ", valor) 
        print("\n")   

