inventario = []
resposta = "S"
while resposta == "S":
    inventario.append(input("Equipamento: "))
    inventario.append(float(input("Valor: ")))
    inventario.append(int(input("Número Serial: ")))
    inventario.append(input("Apartamento: "))
    resposta = input ("Digite "S" para continuar: ").upper()
for elemento in inventario:
    print (elemento)