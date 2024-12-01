def merge_sort(lista):
    # Caso base: lista com 0 ou 1 elemento já está ordenada
    if len(lista) <= 1:
        return lista

    # Dividir a lista em duas metades
    meio = len(lista) // 2
    lista_esquerda = merge_sort(lista[:meio])  # Recursão para a metade esquerda
    lista_direita = merge_sort(lista[meio:])  # Recursão para a metade direita
    # Combinar as listas
    return merge(lista_esquerda, lista_direita)

def merge(lista_esquerda, lista_direita):
    # Lista final combinada
    resultado = []
    i = j = 0

    # Combina elementos das duas listas em ordem crescente
    while i < len(lista_esquerda) and j < len(lista_direita):
        if lista_esquerda[i] <= lista_direita[j]:
            resultado.append(lista_esquerda[i])
            i += 1
        else:
            resultado.append(lista_direita[j])
            j += 1

    # Adiciona os elementos restantes (se tiver) das listas
    resultado.extend(lista_esquerda[i:])
    resultado.extend(lista_direita[j:])

    return resultado
    
lista_original = [38, 27, 43, 3, 9, 82, 10]
print("Lista original:")
print(lista_original)

lista_ordenada = merge_sort(lista_original)
print("Lista ordenada:")
print(lista_ordenada)
