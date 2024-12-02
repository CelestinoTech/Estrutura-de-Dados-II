# Busca Ternária
def ternary_search(numeros, esquerda, direita, alvo):
    # Verifica se o limite esquerdo é menor ou igual ao limite direito
    if esquerda <= direita:
        # Calcula dois pontos médios dividindo o subarray atual em três partes iguais
        meio1 = esquerda + (direita - esquerda) // 3
        meio2 = direita - (direita - esquerda) // 3

        # Verifica se o alvo é igual a algum dos dois pontos médios
        if numeros[meio1] == alvo:
            return meio1
        if numeros[meio2] == alvo:
            return meio2

        # Se o alvo for menor que o elemento em meio1, busca no terço esquerdo do subarray
        if alvo < numeros[meio1]:
            return ternary_search(numeros, esquerda, meio1 - 1, alvo)
        # Se o alvo for maior que o elemento em meio2, busca no terço direito do subarray
        elif alvo > numeros[meio2]:
            return ternary_search(numeros, meio2 + 1, direita, alvo)
        # Se o alvo estiver entre meio1 e meio2, busca no terço do meio do subarray
        else:
            return ternary_search(numeros, meio1 + 1, meio2 - 1, alvo)

    # Elemento não encontrado, retorna -1
    return -1


# Função principal
if __name__ == "__main__":
    # O array deve estar ordenado
    numeros = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    alvo = 19

    # Chama a função de busca ternária para encontrar o elemento alvo
    resultado = ternary_search(numeros, 0, len(numeros) - 1, alvo)

    # Verifica se o resultado não é -1 (elemento encontrado) e imprime o índice
    if resultado != -1:
        print(f"Elemento {alvo} encontrado no índice {resultado}")
    # Se o resultado for -1, o elemento não foi encontrado no array
    else:
        print(f"Elemento {alvo} não encontrado no array")
