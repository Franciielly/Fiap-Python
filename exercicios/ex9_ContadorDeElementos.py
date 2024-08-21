def entrada_valida(palavra):
    return palavra.isalpha()
cont = 0

print("-------- CONTADOR DE ELEMENTOS --------")
print("Insira várias palavras aleatórias. Você pode repetir palavras quantas vezes quiser, pois esse é o objetivo.")
print ("\n")

print("Digite uma palavra (ou pressione ENTER para parar)")

palavras = []

while True: 
    palavra = input("Digite uma palavra: ")
    if palavra == "":
        break
    if entrada_valida(palavra):
        palavras.append(palavra)
    else: 
        print("Entrada inválida. Por favor, digite apenas palavras (letras).")

palavraBuscada = input("Digite a palavra que você gostaria de saber quantas vezes foi digitada: ")
for palavra in palavras:
    if palavraBuscada == palavra:
        cont += 1

print(f"A palavra {palavraBuscada} foi digitada {cont} vezes")



