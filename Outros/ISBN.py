def binary_search(lista, alvo):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        
        if lista[meio]['ISBN'] == alvo:
            return meio  
        elif alvo < lista[meio]['ISBN']:
            fim = meio - 1
        else:
            inicio = meio + 1
    return -1

if __name__ == "__main__":
    lista_livros = [
        {'ISBN': '0001', 'titulo': 'Introdução à Programação'},
        {'ISBN': '0002', 'titulo': 'Estruturas de Dados'},
        {'ISBN': '0003', 'titulo': 'Algoritmos Avançados'},
        {'ISBN': '0004', 'titulo': 'Redes de Computadores'},
        {'ISBN': '0005', 'titulo': 'Inteligência Artificial'}
    ]  
    isbn_alvo = '0005'
    resultado = binary_search(lista_livros, isbn_alvo)

    if resultado != -1:
        livro = lista_livros[resultado]
        print(f"Livro encontrado: '{livro['titulo']}' (ISBN: {livro['ISBN']})")
    else:
        print(f"Livro com ISBN {isbn_alvo} não encontrado.")
