print("---------Calcula IMC----------")
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
if altura > 0 and peso > 0:
    imc =  peso / (altura**2)
    print(f"Seu IMC é: {imc:.2f}" )
    if imc < 18.5:
        print ("Sua classificação é: ABAIXO DO PESO")
    elif 18.5 <= imc <= 24.9:
        print("Sua classificação é: SAUDÁVEL")
    elif 25<= imc <= 29.9:
        print("Sua classificação é considerada: ACIMA DO PESO")
    elif 30 <= imc <= 34.9:
        print("Sua classificação é considerada: OBESIDADE ")
    elif 35 <= imc <= 39.9:
        print("Sua classificação é considerada: OBESIDADE SEVERA")
    else: 
        print("Sua classificação é considerada: OBESIDADE MÓRBIDA")
else:
    print("Digite números positivos.")
