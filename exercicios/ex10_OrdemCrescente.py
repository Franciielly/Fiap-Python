print("-------Crescente ou Decrescente-------")
print ("Digite vários números positivos e quando desejar parar aperte Enter.")
numeros = []
while True:
    numero = input("Número: ")
    if numero == "":
        break
    if numero.replace('.', '', 1).isdigit():
        numero = float(numero)
        if numero > 0:
            numeros.append(numero)
        else:
            print("Digite números positivos.")
    else: 
        print("Por favor, digite apenas números positivos.")

while True: 
    ordem = input("Você prefere que os números sejam ordenados em ordem crescente ou decrescente? ").upper()
    if ordem == "CRESCENTE":
        numeros.sort() 
        print("Números positivos digitados em ordem crescente: ", numeros)
        break
    elif ordem == "DECRESCENTE":
        numeros.sort(reverse=True)
        print("Números positivos digitados em ordem decrescente: ", numeros)
        break
    else: 
        print("Opção inválida. Por favor, digite \"crescente\" ou \"decrescente\"")
print("Programa encerrado.")


