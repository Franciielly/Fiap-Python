nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
prioridade = "NÃO"
if idade >= 65: 
    prioridade = "SIM"
print("O paciente " + nome + "possui atendimento prioritário? " + prioridade)