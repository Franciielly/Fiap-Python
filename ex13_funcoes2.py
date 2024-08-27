# Função para deixar números em ordem crescente
def crescente(lista):
    lista.sort()
    return lista

# Função para deixar números em ordem decrescente
def decrescente(lista):
    lista.sort(reverse=True)
    return lista

# Função que retorna maior número
def maiornumero(lista):
    if not lista:
        return None
    return max(lista)

# Função que retorna menor número
def menornumero(lista):
    if not lista:
        return None
    return min(lista)

# Função que retorna a soma dos números
def somaNumero(lista):
    if not lista:
        return None
    return sum(lista)

# Função que retorna números pares digitados
def numerosPares(lista):
    pares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
    return pares

# Função que retona números ímpares digitados
def numerosImpares(lista):
    impares = []
    for numero in lista:
        if numero % 2 != 0:
            impares.append(numero)
    return impares
        