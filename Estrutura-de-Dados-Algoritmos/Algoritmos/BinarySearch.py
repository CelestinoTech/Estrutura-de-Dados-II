def binary_search(lista, alvo, inicio=0, fim=None):
    # Define o limite inicial e final da busca da lista.
    if fim is None:
        fim = len(lista) - 1
    if inicio <= fim:
        # Começa a dividir a lista ao meio
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            return meio
        # Caso o alvo seja menor que o meio, busca na metade esquerda. (Recursividade)
        if alvo < lista[meio]:
            return binary_search(lista, alvo, inicio, meio - 1)
        # Caso contrário, busca na metade direita. E elimina o outro lado
        return binary_search(lista, alvo, meio + 1, fim)
    return None

if __name__ == "__main__":
    lista = [1, 1, 3, 6, 8, 12, 13, 80, 90]
    alvo = 3
    resultado = binary_search(lista, alvo)
    if resultado is not None:
        print(f"Elemento {alvo} encontrado no índice: {resultado}")
    else:
        print(f"Elemento {alvo} não encontrado na lista.")
