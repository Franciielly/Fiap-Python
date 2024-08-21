resposta = "SIM"
while resposta == "SIM":
    op = input("Digite a operação: ").upper()
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    if op == "SOMA" or op == "+":
        soma = numero1 + numero2
        print(str (numero1) + " + " + str (numero2) + " = "+ str (soma))
    elif op == "SUBTRAÇÃO" or op == "-":
        sub = numero1 - numero2
        print(str (numero1) + " - " + str(numero2) + " = " + str(sub))
    elif op == "MULTIPLICAÇÃO" or op == "x":
        mult = numero1 * numero2
        print(str(numero1) + " X " + str(numero2) + " = " + str(mult))
    elif op == "DIVISÃO" or op == "/":
        if numero2 != 0:
            div = numero1 / numero2
            print(str(numero1) + " ÷ " + str(numero2) + " = " + str(div))
        else:
            print("Divisão por 0 não é permitida.")
    else:
        print("Entrada inválida.")
    while True: 
        resposta = input("Continuar? SIM/NÃO ").upper()
        if resposta == "SIM" or resposta == "NÃO":
            break
        else: 
            print ("Digite apenas SIM ou NÃO.")
print("Programa encerrado.")
