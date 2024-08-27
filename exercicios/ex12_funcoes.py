#Função que soma números digitados
def somarNumeros(lista):
    soma = 0
    while True:
        numero = input("Digite um número: ")
        if numero == "":
            break
        if numero.replace('.', '', 1).isdigit():
            numero = float (numero)
            lista.append(numero)
        else: 
            print("Digite apenas números.")
    for numero in lista:
        soma+= numero
    return soma

#Função que encontra maior e menor número digitado
def maiornumero(lista):
    while True:
        numeroM = input ("Gostaria de ver o menor ou maior número digitado? ").upper()
        if numeroM == "MAIOR": 
            return max(lista)
        elif numeroM == "MENOR":
            return min(lista)
        else:
            print("Opção inválida. Por favor, digite \"Maior\" ou \"Menor\".")
    
minhaLista = []
resultado = somarNumeros(minhaLista)
print("A soma dos números: ", resultado)

resultadoMaiorMenor = maiornumero(minhaLista)
print("O número escolhido é: ", resultadoMaiorMenor)
