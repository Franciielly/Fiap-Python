
eq = input("Digite o nome do equipamento que será depreciado: ")
for indice in range (0,len(equipamento)): 
    if equi == equipamento[indice]:
        novoPreco = valor[indice] - (0.10 * valor[indice]) 
        valor = novoPreco
        print("O novo valor do " + equipamento + "é de R$" + str(valor[indice]))

SerialDescartado = input("Digite o número serial do equipamento descartado: ")
for indice in range (0,len(equipamento)):
    if numeroSerial[indice] == SerialDescartado:
        del equipamento[indice]
        del valor[indice]
        del numeroSerial[indice]
        del departamento[indice]
        break