def partition(array, low, high):
    """
    Função de partição para o Quick Sort.
    Coloca o elemento pivô na posição correta e organiza os elementos menores
    à esquerda e os maiores à direita do pivô.
    """
    pivot = array[high]  # Escolhe o último elemento como pivô
    i = low - 1  # Índice do menor elemento

    for j in range(low, high):
        if array[j] <= pivot:  # Se o elemento atual for menor ou igual ao pivô
            i += 1
            array[i], array[j] = array[j], array[i]  # Troca os elementos

    # Coloca o pivô na posição correta
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def quick_sort(array, low, high):
    """
    Implementação do Quick Sort usando recursão.
    """
    if low < high:
        # Particiona o array e retorna o índice do pivô
        pivot_index = partition(array, low, high)

        # Ordena os sub-arrays à esquerda e à direita do pivô
        quick_sort(array, low, pivot_index - 1)
        quick_sort(array, pivot_index + 1, high)


# Exemplo de uso
if __name__ == "__main__":
    array_original = [10, 7, 8, 9, 1, 5]
    print("Array original:", array_original)

    quick_sort(array_original, 0, len(array_original) - 1)
    print("Array ordenado:", array_original)
