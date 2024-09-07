usuario = {}
opcoes = """
1 - Inserir
2 - Pesquisar
3 - Excluir 
4 - Listar 
5 - Sair 
"""

res = "S"
while res == "S":
    opcao = input(opcoes + "Digite uma opção: ")
    if opcao == "1":
        print("------------------------")
        chave = input("Digite o login de usuário: ").upper()
        usuario[chave] = [input("Digite seu nome: ").upper(),
                          input("Digite a última data de acesso: "),
                          input("Qual a última estação acessada: ") ]
        print("------------------------")

    elif opcao == "2":
        print("------------------------")
        pesquisar = input("Digite o login: ").upper()
        print("Dados: ", usuario.get(pesquisar))
        print("------------------------")

    elif opcao == "3":
        print("------------------------")
        excluir = input("Digite o login: ").upper()
        print("Excluindo.....")
        usuario.pop(excluir)
        print("Dados: ", usuario)

    elif opcao == "4":
        print("------------------------")
        print("Dados: ", usuario)
        print("------------------------")

    elif opcao == "5":
        print("------------------------")
        print("Saindo........")
        print("------------------------")
        break
    
    else:
        print("Digite uma opção válida.")

    res = input("Deseja tentar outra opção: ").upper()

print("Programa encerrado.")




        

        
