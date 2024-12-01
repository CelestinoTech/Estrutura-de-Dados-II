def selection_sort(array):
    size = len(array)
    # Percorre todos os elementos da lista
    for i in range(size):
        # Assume que o primeiro elemento não ordenado é o mínimo
        min_idx = i
        # Encontra o menor elemento na lista não ordenada
        for j in range(i + 1, size):
            if array[j] < array[min_idx]:
                min_idx = j
        # Troca o elemento encontrado com o primeiro elemento não ordenado
        array[i], array[min_idx] = array[min_idx], array[i]
        
        # Acompanhamento da lista após cada iteração
        print(f"Iteração {i + 1}: {array}")
    
    return array
    
array_original = [64, 25, 12, 32, 11]
print("Array original:")
print(array_original)

print("\nProcesso de ordenação:")
sorted_array = selection_sort(array_original)

print("\nArray ordenado:")
print(sorted_array)
