resposta = "SIM"
while resposta == "SIM":
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    doenca_infectocontagiosa = "aaaa"
    while doenca_infectocontagiosa != "SIM" and doenca_infectocontagiosa != "NÃO":
        print("Digite SIM ou NÃO")
        doenca_infectocontagiosa = input("Suspeita de doença infecto-contagiosa? ").upper()
    if idade >=65: 
        print("Paciente COM prioridade")
        if doenca_infectocontagiosa=="SIM":
            print("Encaminhe o paciente para sala AMARELA")
        elif doenca_infectocontagiosa=="NÃO":
            print("Encaminhe o paciente para sala BRANCA")
        else: 
            print("Responda a suspeita de doença  infecto-contagiosa com SIM ou NÃO")
    else: 
        print("Paciente SEM prioridade")
        if doenca_infectocontagiosa == "SIM":
            print("Encaminhe o paciente para sala AMARELA")
        elif doenca_infectocontagiosa == "NÃO":
            print("Encaminhe o paciente para sala BRANCA")
    resposta=input("\nGostaria de cadastrar outro paciente? ").upper()

    
