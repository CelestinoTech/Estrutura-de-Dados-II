# Interpolation Search
# Semelhante ao Binary Search, mas em vez de dividir a lista ao meio, o algoritmo utiliza uma estimativa para encontrar o índice do elemento desejado. Ele começa a busca mais próximo do valor a ser encontrado, tornando-o eficiente em grandes conjuntos de dados ordenados e uniformemente distribuídos.
# Mais eficiente em grandes conjuntos de dados, com listas ordenadas uniformes [10,20,30,40,50,60]

def interpolationSearch(arr, lo, hi, x):
    # Verifica se os dados são válidos, e se o valor procurado está dentro do intervalo dos valores.
    if (lo <= hi and x >= arr[lo] and x <= arr[hi]):
        # Calcula a posição estimada do valor desejado, com base na distribuição uniforme dos elementos.
        pos = lo + ((hi - lo) // (arr[hi] - arr[lo]) * (x - arr[lo]))
        # Verifica se o valor estimado corresponde ao valor procurado
        if arr[pos] == x:
            return pos
        # Se o valor é maior que o estimado, busca na metade direita da lista (Recursividade)
        if arr[pos] < x:
            return interpolationSearch(arr, pos + 1, hi, x)
        # Se o valor é menor que o estimado, busca na metade esquerda da lista
        if arr[pos] > x:
            return interpolationSearch(arr, lo, pos - 1, x)
    # Caso o valor não esteja presente, retorna -1.
    return -1

#Lista ordenada com intervalos uniformes
arr_uniforme = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
n_uniforme = len(arr_uniforme)

# Elemento a ser procurado (Retorna a posição)
x_uniforme = 18
index_uniforme = interpolationSearch(arr_uniforme, 0, n_uniforme - 1, x_uniforme)

if index_uniforme != -1:
    print("Elemento Encontrado na lista uniforme:", index_uniforme)
else:
    print("Elemento Não Encontrado na lista uniforme")

#Uniforme
arr_nao_uniforme = [1, 2, 5, 9, 15, 18, 21, 26, 35, 40, 55, 60, 65]
n_nao_uniforme = len(arr_nao_uniforme)

#Não Uniforme
x_nao_uniforme = 18
index_nao_uniforme = interpolationSearch(arr_nao_uniforme, 0, n_nao_uniforme - 1, x_nao_uniforme)

if index_nao_uniforme != -1:
    print("Elemento Encontrado na lista não uniforme:", index_nao_uniforme)
else:
    print("Elemento Não Encontrado na lista não uniforme")
