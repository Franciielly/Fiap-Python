lista = []
resposta = "SIM"
while resposta == "SIM":
    lista.append(input("Digite um número: "))
    resposta = input("Digite \"SIM\" se desejar digitar mais algum número? ").upper()
for elemento in lista:
    print (elemento)