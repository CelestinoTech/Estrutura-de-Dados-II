def binary_search(lista, alvo, inicio=0, fim=None):
    # Define o limite inicial e final da busca.
    if fim is None:
        fim = len(lista) - 1
    if inicio <= fim:
        # Calcula o índice do meio.
        meio = (inicio + fim) // 2
        # Verifica se o elemento do meio é o alvo.
        if lista[meio] == alvo:
            return meio
        # Caso o alvo seja menor que o meio, busca na metade esquerda. (Recursividade)
        if alvo < lista[meio]:
            return binary_search(lista, alvo, inicio, meio - 1)
        # Caso contrário, busca na metade direita.
        return binary_search(lista, alvo, meio + 1, fim)
    # Se o alvo não estiver presente, retorna None.
    return None

# Exemplo de uso do algoritmo
if __name__ == "__main__":
    # Lista ordenada
    lista = [1, 1, 3, 6, 8, 12, 13, 80, 90]
    # Alvo a ser buscado
    alvo = 3
    # Chamada da função
    resultado = binary_search(lista, alvo)
    # Exibição do resultado
    if resultado is not None:
        print(f"Elemento {alvo} encontrado no índice: {resultado}")
    else:
        print(f"Elemento {alvo} não encontrado na lista.")
