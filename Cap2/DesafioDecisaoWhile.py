resposta = "SIM"
while resposta == "SIM":
    nivel = input("Digite seu nível de acesso: ").upper()
    if nivel == "ADM" or nivel == "USR":
        genero = input("Digite seu gênero: ").upper()
        if genero == "MASCULINO":
            if nivel == "ADM":
                print("Olá, administrador.")
            else:
                print("Olá, usuário.")
        elif genero == "FEMININO":
            if nivel == "ADM":
                print("Olá, administradora.")
            else:
                print("Olá,usuária.")
        else:
            print("Digite o genêro corretamente!")
    elif nivel == "GUEST":
        print("Olá, visitante.")
    else:
        print("Olá, desconhecido(a).")
    resposta = input("Digite SIM para continuar: ").upper()
