notas = []
soma = 0
nome = input("Digite o nome do aluno: ")

while True:
    nota = input("Digite a nota (ou pressione Enter para parar): ")
    # Sai do loop se o usuário não digitar nada
    if nota == "":
        break
    # Verifica se a entrada é um número válido
    if nota.replace('.', '', 1).isdigit():
        nota = float(nota)
        notas.append(nota)
        soma += nota
    else:
        print("Por favor, insira um valor numérico válido.")
# Calcula média das notas
numeroNotas = len(notas)
media = soma / numeroNotas if numeroNotas > 0 else 0

print(f"As notas do aluno {nome} são: {notas}")
print(f"A média final do aluno {nome} é: {media:.2f}")
