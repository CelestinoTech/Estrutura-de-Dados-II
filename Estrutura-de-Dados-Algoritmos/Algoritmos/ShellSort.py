import math

def shell_sort(array):
    size = len(array)
    # Calcula o maior gap (h) como (3^k - 1) / 2
    k = math.log(size + 1, 3)  # Base 3
    k = math.floor(k + 0.5)
    gap = (3 ** int(k) - 1) // 2

    while gap > 0:
        for i in range(gap, size):  
            current = array[i]      
            j = i
            while j >= gap and array[j - gap] > current:
                array[j] = array[j - gap]
                j -= gap
            array[j] = current          
        gap = (gap - 1) // 3            


array = [1, 9, 6, 35, 2, 99, 8, 7]

print("Array original:")
print(array)

shell_sort(array)

print("Array ordenado:")
print(array)
