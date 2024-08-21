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







#nivelDeAcesso = input ("Digite seu nível de acesso: ").upper()
#genero = input("Digite seu gênero: ").upper()

#if nivelDeAcesso == "ADM" and genero == "MASCULINO":
    #print("Olá administrador!")
#elif nivelDeAcesso =="ADM" and genero == "FEMININO":
    #print("Olá administradora!")
#elif nivelDeAcesso == "USR" and genero == "MASCULINO":
    #print("Olá usuário!")
#elif nivelDeAcesso == "USR" and genero == "FEMININO":
    #print("Olá usuária!")
#elif nivelDeAcesso == "GUEST":
    #print("Olá visitante!")
#elif nivelDeAcesso != "ADM" or "USR" or "GUEST":
    #print("Olá desconhecido(a)")

