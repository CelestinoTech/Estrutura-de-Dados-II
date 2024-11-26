# Algoritmo de Busca Binária
def binary_search(array, item, start=0, end=None):
    # Define o limite inicial e final da busca.
    if end is None:
        end = len(array) - 1

    # Enquanto os limites forem válidos (start <= end).
    if start <= end:
        # Calcula o índice do meio.
        m = (start + end) // 2

        # Verifica se o elemento do meio é o alvo.
        if array[m] == item:
            return m
        
        # Caso o item seja menor que o meio, busca na metade esquerda.
        if item < array[m]:
            return binary_search(array, item, start, m - 1)
        
        # Caso contrário, busca na metade direita.
        return binary_search(array, item, m + 1, end)
    
    # Se o item não estiver presente, retorna None.
    return None


# Exemplo de uso do algoritmo
if __name__ == "__main__":
    # Lista ordenada
    array = [1, 1, 3, 6, 8, 12, 13, 80, 90]

    # Item a ser buscado
    target = 3

    # Chamada da função
    resultado = binary_search(array, target)

    # Exibição do resultado
    if resultado is not None:
        print(f"Elemento {target} encontrado no índice: {resultado}")
    else:
        print(f"Elemento {target} não encontrado na lista.")

# Observação:
# A lista deve ser ordenada, pois a lógica da busca binária depende disso.
# Se a lista não estiver ordenada, o algoritmo não funcionará corretamente.
