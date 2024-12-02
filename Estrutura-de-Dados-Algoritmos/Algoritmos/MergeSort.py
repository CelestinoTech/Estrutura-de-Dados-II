def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    lista_esquerda = merge_sort(lista[:meio])  
    lista_direita = merge_sort(lista[meio:])  
    
    return merge(lista_esquerda, lista_direita)

def merge(lista_esquerda, lista_direita):
    
    resultado = []
    i = j = 0

    while i < len(lista_esquerda) and j < len(lista_direita):
        if lista_esquerda[i] <= lista_direita[j]:
            resultado.append(lista_esquerda[i])
            i += 1
        else:
            resultado.append(lista_direita[j])
            j += 1

    resultado.extend(lista_esquerda[i:])
    resultado.extend(lista_direita[j:])

    return resultado
    
lista_original = [38, 27, 43, 3, 9, 82, 10]
print("Lista original:")
print(lista_original)

lista_ordenada = merge_sort(lista_original)
print("Lista ordenada:")
print(lista_ordenada)
