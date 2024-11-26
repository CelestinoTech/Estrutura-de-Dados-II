# Algoritmo de Busca Binária
# O algoritmo de busca binária tem como objetivo encontrar um elemento em uma lista **ordenada**.
# Ele funciona dividindo a lista pela metade a cada iteração, reduzindo o espaço de busca.
# A cada divisão, verifica-se se o elemento procurado (alvo) está no meio da lista:
#   - Se sim, o índice do elemento é retornado.
#   - Se o elemento for menor que o do meio, descarta-se a metade direita.
#   - Se for maior, descarta-se a metade esquerda.
# O processo é repetido de forma recursiva ou iterativa até encontrar o elemento ou até que a lista se esgote.

# Nota: A lista deve estar **obrigatoriamente ordenada**. Caso contrário, a lógica do algoritmo não funcionará,
# podendo gerar resultados incorretos e pior desempenho no tempo de execução.


def binary_search(array, item, start=0, end=None):
    # Define o limite inicial e final da busca.
    if end is None:
        end = len(array) - 1
    if start <= end:
        # Calcula o índice do meio.
        m = (start + end) // 2
        # Verifica se o elemento do meio é o alvo.
        if array[m] == item:
            return m
        # Caso o item seja menor que o meio, busca na metade esquerda.(Recursividade) 
        if item < array[m]:
            return binary_search(array, item, start, m - 1)
        # Caso contrário, busca na metade direita.
        return binary_search(array, item, m + 1, end)
    # Se o item não estiver presente, retorna None.
    return None
# Exemplo de uso do algoritmo
if __name__ == "__main__":
    # Lista ordenada
    array = [1, 1, 3, 6, 8, 12, 13, 80, 90]
    # Item a ser buscado
    target = 3
    # Chamada da função
    resultado = binary_search(array, target)
    # Exibição do resultado
    if resultado is not None:
        print(f"Elemento {target} encontrado no índice: {resultado}")
    else:
        print(f"Elemento {target} não encontrado na lista.")
