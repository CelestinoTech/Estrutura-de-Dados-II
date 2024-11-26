# JumpSearch
# Esse algoritmo de busca funciona da seguinte maneira: ao receber uma lista já ordenada,
# ele realiza um cálculo (sqrt(16) = 4), onde o resultado será a quantidade de "saltos" 
# que ele deverá fazer. Após realizar esses saltos, ele faz uma busca linear dentro do bloco
# para encontrar o elemento, retornando a posição do item caso o encontre.
# A complexidade do Jump Search é O(√n), onde "n" é o número de elementos na lista. 
# Comparado ao Binary Search, que tem complexidade O(log n), o Jump Search tende a ser eficiente
# para listas de tamanho moderado, mas em listas muito grandes, o Binary Search pode ser mais eficiente.

import math

def jumpSearch(arr, x, n):
    # Encontrando o tamanho do bloco que será pulado
    step = math.sqrt(n)
    # Variável para contar o número de pulos
    jumps = 0
    # Encontrando o bloco onde o elemento pode estar
    prev = 0
    while arr[int(min(step, n)-1)] < x:
        prev = step
        step += math.sqrt(n)
        jumps += 1  # Contabiliza o pulo
        if prev >= n:
            return -1, jumps  # Retorna -1 se não encontrar o elemento
    
    # Busca linear dentro do bloco onde o elemento pode estar
    while arr[int(prev)] < x:
        prev += 1
        jumps += 1  # Contabiliza o pulo na busca linear
        
        # Se chegarmos ao próximo bloco ou ao fim da lista, o elemento não está na lista
        if prev == min(step, n):
            return -1, jumps  # Retorna -1 se não encontrar o elemento

    # Se o elemento for encontrado
    if arr[int(prev)] == x:
        return prev, jumps  

    return -1, jumps  # Retorna -1 se não encontrar o elemento

arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21,
    34, 55, 89, 144, 233, 377, 610 ]
x = 55
# Conta a quantidade de pulos, definido pela raiz quadrada.
n = len(arr)

index, jumps = jumpSearch(arr, x, n)

if index != -1:
    print(f"Numero {x} na posicao {index}. Total de pulos: {jumps}")
else:
    print(f"Numero {x} nao encontrado. Total de pulos: {jumps}")
