equipamento = []
valor = []
numeroSerial = []
departamento = []
resposta = "S"
while resposta == "S":
    equipamento.append(input("Equipamento: "))
    valor.append(float(input("Digite o valor: ")))
    numeroSerial.append(int(input("Digite o número serial: ")))
    departamento.append(input("Digite o departamento: "))
    resposta = input("Digite \"S\" para digitar outros equipamentos: ").upper()

for indice in range(0,len(equipamento)): 
        print("Equipamentos..: ", (indice + 1))
        print ("Nome........: ", equipamento[indice])
        print("Valor........: ", valor [indice])
        print("Serial.......: ", numeroSerial[indice])
        print("Departamento.: ", departamento[indice])
        print("\n")

busca = input ("Digite o nome do equipamento que deseja buscar: ")
for indice in range(0,len(equipamento)):
    if busca == equipamento[indice]:
        print("Valor...: ", valor[indice])
        print("Serial..: ", numeroSerial[indice])

depreciacao = input("Digite o nome do equipamento que será depreciado: ")
for indice in range (0,len(equipamento)): 
    if depreciacao == equipamento[indice]:
        print("Valor antigo: ", valor[indice])
        novoPreco = valor[indice] - (0.10 * valor[indice])
        valor[indice] = novoPreco
        print("Novo valor: ", valor[indice])

SerialDescartado = input("Digite o número serial do equipamento descartado: ")
for indice in range (0,len(equipamento)):
    if numeroSerial[indice] == SerialDescartado:
        del equipamento[indice]
        del valor[indice]
        del numeroSerial[indice]
        del departamento[indice]
        break

for indice in range(0,len(equipamento)): 
        print("Equipamentos..: ", (indice + 1))
        print ("Nome........: ", equipamento[indice])
        print("Valor........: ", valor[indice])
        print("Serial.......: ", numeroSerial[indice])
        print("Departamento.: ", departamento[indice])
        print("\n")
