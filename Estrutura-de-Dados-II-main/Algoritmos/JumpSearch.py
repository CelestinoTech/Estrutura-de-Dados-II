import math

def jump_search(lista, alvo, tamanho):
    # Encontrando o tamanho do bloco que será pulado
    salto = math.sqrt(tamanho)
    # Variável para contar o número de pulos
    pulos = 0
    # Encontrando o bloco onde o elemento pode estar
    anterior = 0
    while lista[int(min(salto, tamanho)-1)] < alvo:
        anterior = salto
        salto += math.sqrt(tamanho)
        pulos += 1  # Contabiliza o pulo
        if anterior >= tamanho:
            return -1, pulos  # Retorna -1 se não encontrar o elemento
    
    # Busca linear dentro do bloco onde o elemento pode estar
    while lista[int(anterior)] < alvo:
        anterior += 1
        pulos += 1  # Contabiliza o pulo na busca linear
        
        # Se chegarmos ao próximo bloco ou ao fim da lista, o elemento não está na lista
        if anterior == min(salto, tamanho):
            return -1, pulos  # Retorna -1 se não encontrar o elemento

    # Se o elemento for encontrado
    if lista[int(anterior)] == alvo:
        return anterior, pulos  

    return -1, pulos  # Retorna -1 se não encontrar o elemento

# Lista de exemplo
lista = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
alvo = 55
# Conta a quantidade de pulos, definido pela raiz quadrada.
tamanho = len(lista)

indice, pulos = jump_search(lista, alvo, tamanho)

if indice != -1:
    print(f"Número {alvo} na posição {indice}. Total de pulos: {pulos}")
else:
    print(f"Número {alvo} não encontrado. Total de pulos: {pulos}")
