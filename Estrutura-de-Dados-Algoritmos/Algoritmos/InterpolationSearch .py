def interpolation_search(lista, inicio, fim, alvo):
    if (inicio <= fim and alvo >= lista[inicio] and alvo <= lista[fim]):
        posicao = inicio + ((fim - inicio) // (lista[fim] - lista[inicio]) * (alvo - lista[inicio]))
        if lista[posicao] == alvo:
            return posicao
        if lista[posicao] < alvo:
            return interpolation_search(lista, posicao + 1, fim, alvo)
        if lista[posicao] > alvo:
            return interpolation_search(lista, inicio, posicao - 1, alvo)
    return -1

lista_uniforme = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
n_uniforme = len(lista_uniforme)


alvo_uniforme = 18
indice_uniforme = interpolation_search(lista_uniforme, 0, n_uniforme - 1, alvo_uniforme)

if indice_uniforme != -1:
    print("Elemento encontrado na lista uniforme:", indice_uniforme)
else:
    print("Elemento não encontrado na lista uniforme")


lista_nao_uniforme = [1, 2, 5, 9, 15, 18, 21, 26, 35, 40, 55, 60, 65]
n_nao_uniforme = len(lista_nao_uniforme)


alvo_nao_uniforme = 18
indice_nao_uniforme = interpolation_search(lista_nao_uniforme, 0, n_nao_uniforme - 1, alvo_nao_uniforme)

if indice_nao_uniforme != -1:
    print("Elemento encontrado na lista não uniforme:", indice_nao_uniforme)
else:
    print("Elemento não encontrado na lista não uniforme")
