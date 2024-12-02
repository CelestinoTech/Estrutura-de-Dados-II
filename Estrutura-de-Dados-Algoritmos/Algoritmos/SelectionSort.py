def selection_sort(array):
    size = len(array)

    for i in range(size):
        min_idx = i
        for j in range(i + 1, size):
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
        print(f"Iteração {i + 1}: {array}")
    
    return array
    
array_original = [64, 25, 12, 32, 11]
print("Array original:")
print(array_original)

print("\nProcesso de ordenação:")
sorted_array = selection_sort(array_original)

print("\nArray ordenado:")
print(sorted_array)
