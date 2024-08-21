resposta = "SIM"
while resposta == "SIM":
    parOuImpar = input("Digite se você gostaria de ver os números pares ou ímpares: ").upper()
    numero = int(input("Digite o número máximo: "))
    contador = 0
    if parOuImpar == "PARES":
        while contador <= numero:
            if contador % 2 == 0:
                print(contador)
            contador+=1
    elif parOuImpar == "ÍMPARES":
        while contador <= numero:
            if contador % 2 != 0:
                print(contador)
            contador+=1
    else:
        print ("Responda as perguntas corretamente")
    resposta = input("Se gostaria de continuar digite SIM:  ").upper()
   