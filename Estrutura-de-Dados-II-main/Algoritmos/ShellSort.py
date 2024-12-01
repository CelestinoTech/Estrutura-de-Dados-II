import math

def shell_sort(array):
    size = len(array)
    # Calcula o maior gap (h) como (3^k - 1) / 2
    k = math.log(size + 1, 3)  # Base 3
    k = math.floor(k + 0.5)
    gap = (3 ** int(k) - 1) // 2

    # Enquanto o gap for maior que zero
    while gap > 0:
        for i in range(gap, size):  # Percorre a lista a partir do gap
            current = array[i]          # Elemento atual a ser posicionado
            j = i
            # Move os elementos maiores para frente, respeitando o gap
            while j >= gap and array[j - gap] > current:
                array[j] = array[j - gap]
                j -= gap
            array[j] = current          # Insere o elemento na posição correta
        gap = (gap - 1) // 3            # Atualiza o gap para o próximo valor

# Lista de exemplo
array = [1, 9, 6, 35, 2, 99, 8, 7]

print("Array original:")
print(array)

shell_sort(array)

print("Array ordenado:")
print(array)
