import math
def jump_search(lista, alvo, tamanho):
    salto = math.sqrt(tamanho)
    pulos = 0
    anterior = 0
    while lista[int(min(salto, tamanho)-1)] < alvo:
        anterior = salto
        salto += math.sqrt(tamanho)
        pulos += 1  
        if anterior >= tamanho:
            return -1, pulos  
    

    while lista[int(anterior)] < alvo:
        anterior += 1
        pulos += 1  
        
        if anterior == min(salto, tamanho):
            return -1, pulos  

    if lista[int(anterior)] == alvo:
        return anterior, pulos  

    return -1, pulos

lista = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
alvo = 55
tamanho = len(lista)

indice, pulos = jump_search(lista, alvo, tamanho)

if indice != -1:
    print(f"Número {alvo} na posição {indice}. Total de pulos: {pulos}")
else:
    print(f"Número {alvo} não encontrado. Total de pulos: {pulos}")
