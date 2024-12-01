def binary_search_recursive(lista, alvo, inicio, fim):
    """
    Busca binária recursiva para encontrar o índice do elemento alvo.
    """
    if inicio > fim:
        return -1  # Caso base: o intervalo é inválido

    meio = (inicio + fim) // 2  # Calcula o índice do meio

    if lista[meio] == alvo:  # Caso o elemento no meio seja o alvo
        return meio
    elif lista[meio] > alvo:  # Busca na metade esquerda
        return binary_search_recursive(lista, alvo, inicio, meio - 1)
    else:  # Busca na metade direita
        return binary_search_recursive(lista, alvo, meio + 1, fim)


def exponential_search(lista, alvo):
    """
    Implementação da Exponential Search.
    """
    if not lista:
        return -1  # Lista vazia, retorna -1

    if lista[0] == alvo:
        return 0  # Verifica o primeiro elemento

    # Determina o intervalo potencial onde o alvo pode estar
    indice = 1
    while indice < len(lista) and lista[indice] <= alvo:
        indice *= 2  # Dobra o índice a cada passo

    # Define os limites do intervalo para busca binária
    inicio = indice // 2
    fim = min(indice, len(lista) - 1)

    # Chama a busca binária no intervalo encontrado
    return binary_search_recursive(lista, alvo, inicio, fim)


# Exemplo de uso
if __name__ == "__main__":
    lista = [2, 3, 4, 10, 40, 50, 70, 100, 150]
    alvo = 4

    indice = exponential_search(lista, alvo)
    if indice != -1:
        print(f"Índice do elemento {alvo}: {indice}")
    else:
        print(f"Elemento {alvo} não encontrado.")
