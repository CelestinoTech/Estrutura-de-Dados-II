def bucket_sort(lista):
    if not lista:
        return [] 
    num_buckets = len(lista)
    buckets = [[] for _ in range(num_buckets)] 
    for numero in lista:
        indice = int(numero * num_buckets)  
        buckets[indice].append(numero)

    for bucket in buckets:
        bucket.sort()

    lista_ordenada = []
    for bucket in buckets:
        lista_ordenada.extend(bucket)

    return lista_ordenada

def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1
    
    while low <= high and target >= arr[low] and target <= arr[high]:
        # Estimando a posição do elemento
        pos = low + int(((high - low) / (arr[high] - arr[low])) * (target - arr[low]))
        
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
            
    return -1 

if __name__ == "__main__":
    lista = [0.78, 0.17, 0.39, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
    print("Lista original:", lista)

    lista_ordenada = bucket_sort(lista)
    print("Lista ordenada:", lista_ordenada)
    
    nota_procurada = 0.72
    posicao = interpolation_search(lista_ordenada, nota_procurada)
    
    if posicao != -1:
        print(f"A nota {nota_procurada} foi encontrada na posição {posicao}.")
    else:
        print(f"A nota {nota_procurada} não foi encontrada.")
