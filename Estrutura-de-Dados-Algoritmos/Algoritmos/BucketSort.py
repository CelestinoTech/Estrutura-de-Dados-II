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

if __name__ == "__main__":
    lista = [0.78, 0.17, 0.39, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
    print("Lista original:", lista)

    lista_ordenada = bucket_sort(lista)
    print("Lista ordenada:", lista_ordenada)
