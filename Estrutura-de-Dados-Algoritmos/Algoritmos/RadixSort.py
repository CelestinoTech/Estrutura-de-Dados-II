def counting_sort_for_radix(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10  

    
    for num in array:
        index = (num // place) % 10
        count[index] += 1


    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(size - 1, -1, -1):
        index = (array[i] // place) % 10
        output[count[index] - 1] = array[i]
        count[index] -= 1

    for i in range(size):
        array[i] = output[i]


def radix_sort(array):
    if not array:
        return []

    max_number = max(array)
    place = 1

    while max_number // place > 0:
        counting_sort_for_radix(array, place)
        place *= 10

    return array

if __name__ == "__main__":
    array_original = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Array original:", array_original)

    sorted_array = radix_sort(array_original)
    print("Array ordenado:", sorted_array)
