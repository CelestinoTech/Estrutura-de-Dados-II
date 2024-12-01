def bucket_sort(lista):
    """
    Implementação do Bucket Sort.
    Ordena uma lista de números reais no intervalo [0, 1) ou escala os valores para este intervalo.
    """
    if not lista:
        return []  # Retorna lista vazia se a entrada for vazia

    # 1. Determinar o número de buckets
    num_buckets = len(lista)
    buckets = [[] for _ in range(num_buckets)]  # Criar buckets vazios

    # 2. Distribuir os elementos nos buckets
    for numero in lista:
        indice = int(numero * num_buckets)  # Mapear o número para o bucket correto
        buckets[indice].append(numero)

    # 3. Ordenar individualmente os elementos em cada bucket
    for bucket in buckets:
        bucket.sort()

    # 4. Concatenar os buckets ordenados
    lista_ordenada = []
    for bucket in buckets:
        lista_ordenada.extend(bucket)

    return lista_ordenada


# Exemplo de uso
if __name__ == "__main__":
    lista = [0.78, 0.17, 0.39, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
    print("Lista original:", lista)

    lista_ordenada = bucket_sort(lista)
    print("Lista ordenada:", lista_ordenada)
