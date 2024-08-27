def entrada_valida(item): 
    return item.replace(" ","").isalpha()
    
print("--------LISTA DE COMPRAS----------")
print("Digite seus itens e, quando desejar parar, pressione Enter em uma linha em branco")
itens = []
while True:
    item = input("item: ")
    if item == "":
        break
    if entrada_valida(item):
        if item in itens: 
            print("O item já está na lista.")
        else:
            itens.append(item)
    else:
        print("Por favor, digite apenas palavras (letras)")
        
print("----------Itens adicionados---------")
for indice in range(0,len(itens)):
    itens.sort()
    print(itens[indice])

resposta = input("Deseja excluir algum intem? S/N   ").upper()
if resposta == "S":
    ItemExcluido = input("Digite o nome do item que deseja excluir: ")
    for indice in itens: 
        if indice == ItemExcluido:
            itens.remove(indice)
            print("\n")
            print("----------Itens atualizados---------")
            for indice in range(0,len(itens)):
                itens.sort()
                print(itens[indice])
