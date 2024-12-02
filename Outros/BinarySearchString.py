def binary_search(lista, alvo, inicio=0, fim=None):    
    if fim is None:
        fim = len(lista) - 1
    if inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            return meio
        if alvo < lista[meio]:
            return binary_search(lista, alvo, inicio, meio - 1)
        return binary_search(lista, alvo, meio + 1, fim)
    return None


if __name__ == "__main__":
    lista_palavras = ["abacaxi", "banana", "cabelos", "laranja", "maçã"]
    palavra = "laranja"
    resultado = binary_search(lista_palavras, palavra)
    if resultado is not None:
        print(f"Palavra '{palavra}' encontrada no índice: {resultado}")
    else:
        print(f"Palavra '{palavra}' não encontrada na lista.")
