resposta = "SIM"
while resposta == "SIM": 
    nome = input("Digite o nome do aluno: ")
    ra = input("Digite o RA do aluno: ")
    anoLetivo = input ("Digite o ano letivo: ")
    materia = input ("Digite o nome da matéria: ")
    serie = input ("Digite a série do aluno: ")
    notas = int(input("Quantas notas serão digitadas: "))
    totalNotas = 0
    contador = 1
    while contador <= notas:
        nota = float(input("Digite a " + str(contador) + "º nota: "))
        totalNotas += nota
        contador += 1
    print("Média do aluno(a) " + nome + ": " + str((totalNotas / notas)))
    reposta = input ("Gostaria de digitar mais notas? ")

    