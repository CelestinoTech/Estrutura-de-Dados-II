def counting_sort_for_radix(array, place):
    """
    Counting Sort modificado para ser usado no Radix Sort.
    Ordena os números com base no dígito representado pelo parâmetro `place`.
    """
    size = len(array)
    output = [0] * size
    count = [0] * 10  # Base decimal (0-9)

    # Contar as ocorrências dos dígitos na posição atual
    for num in array:
        index = (num // place) % 10
        count[index] += 1

    # Atualizar o array de contagem para posições acumuladas
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Construir o array de saída ordenado
    for i in range(size - 1, -1, -1):
        index = (array[i] // place) % 10
        output[count[index] - 1] = array[i]
        count[index] -= 1

    # Copiar os valores ordenados de volta ao array original
    for i in range(size):
        array[i] = output[i]


def radix_sort(array):
    """
    Implementação do Radix Sort.
    Ordena números inteiros não-negativos.
    """
    if not array:
        return []

    # Encontra o maior número para determinar o número de dígitos
    max_number = max(array)
    place = 1

    # Realiza Counting Sort para cada posição decimal
    while max_number // place > 0:
        counting_sort_for_radix(array, place)
        place *= 10

    return array


# Exemplo de uso
if __name__ == "__main__":
    array_original = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Array original:", array_original)

    sorted_array = radix_sort(array_original)
    print("Array ordenado:", sorted_array)
a