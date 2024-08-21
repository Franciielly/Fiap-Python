print("------CONVERSOR DE MOEDAS--------")
moedas = input("Você gostaria de converter REAIS para DÓLAR, EURO ou LIBRA? ").upper()
if moedas == "DÓLAR" or moedas == "DOLAR":
    quantia = float(input("Qual a quantia desejada? R$"))
    total = quantia * 5.49
    print(f"US$ {total:.2f}")
elif moedas == "EURO":
     quantia = float(input("Qual a quantia desejada? R$"))
     total = quantia * 6.01
     print(f"{total:.2f} €")
elif moedas == "LIBRA":
    quantia = float(input("Qual a quantia desejada? R$"))
    total = quantia * 7.02
    print(f"{total:.2f} £")
else:
    print("Entrada inválida.")