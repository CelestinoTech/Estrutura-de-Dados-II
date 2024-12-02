def binary_search_recursive(lista, alvo, inicio, fim):
    if inicio > fim:
        return -1  

    meio = (inicio + fim) // 2  

    if lista[meio] == alvo:  
        return meio
    elif lista[meio] > alvo:  
        return binary_search_recursive(lista, alvo, inicio, meio - 1)
    else:  
        return binary_search_recursive(lista, alvo, meio + 1, fim)


def exponential_search(lista, alvo):
    if not lista:
        return -1  

    if lista[0] == alvo:
        return 0  

    indice = 1
    while indice < len(lista) and lista[indice] <= alvo:
        indice *= 2  

    inicio = indice // 2
    fim = min(indice, len(lista) - 1)
    return binary_search_recursive(lista, alvo, inicio, fim)


if __name__ == "__main__":
    lista = [2, 3, 4, 10, 40, 50, 70, 100, 150]
    alvo = 4

    indice = exponential_search(lista, alvo)
    if indice != -1:
        print(f"Índice do elemento {alvo}: {indice}")
    else:
        print(f"Elemento {alvo} não encontrado.")
