from ex13_funcoes2 import *  # Importa função de um módulo externo 

lista = [] # Cria lista vazia para armazenar números digitados

# Loop para coletar números digitados pelo usuário
while True:  
    numero = input("Digite um número: ") 
    if numero == "":  # Se a entrada for vazia sai do loop
        break
    # Verifica se a entrada é válida
    if numero.replace('.', '', 1).isdigit():
        numero = float(numero) # Converte para float
        lista.append(numero) 
    else: 
        print("Por favor, digite apenas números.") # mensagem para entrada inválida

# Menu de opção para usuário
menu = """
escolha uma opção: 
1 - Crescente 
2 - Decrescente
3 - Maior número
4 - Menor Número
5 - Soma dos números
6 - Números pares 
7 - Números Ímpares
"""

# Loop para exibir menu e processar escolha do usuário
while True: 
    escolha = int(input(menu + "\nDigite o número de sua escolha: "))

    if escolha == 1:
        resultado = crescente(lista)
        print("Números digitados em ordem crescente:\n", resultado)

    elif escolha == 2:
        resultado = decrescente(lista)
        print("Números em ordem decrescente:\n", resultado)

    elif escolha == 3:
        resultado = maiornumero(lista)
        print("O maior número é: ", resultado)

    elif escolha == 4:
        resultado = menornumero(lista)
        print("O menor número é: ", resultado)

    elif escolha == 5:
        resultado = somaNumero(lista)
        print("A soma dos números é: ", resultado)

    elif escolha == 6:
        resultado = numerosPares(lista)
        print("Os números pares digitados são:\n", resultado)

    elif escolha == 7:
        resultado = numerosImpares(lista)
        print("Os números ímpares digitados são:\n", resultado)
    
    else:
        print("Opcão inválida. Por favor, digite uma opção válida.")
    
    # Loop que verifica se o usúario quer tentar outra opção
    while True: 
        res = input("Gostaria de tentar outra opção (S/N):  ").upper()
        if res == "S":
            break # Sai do loop e volta ao menu
        elif res == "N":
            print("Programa encerrado.")
            exit() # Encerra o programa
        else: 
            print("Opção inválida.Por favor, digite S ou N.")
