# Algoritmos de Busca e Ordenação - Respostas Teóricas

---

## 1. **Binary Search (Busca Binária)**

### Por que a lista deve estar ordenada?

A **Busca Binária** funciona dividindo repetidamente a lista ao meio para localizar um valor, mas ela só opera corretamente se a lista estiver ordenada. Caso contrário, o algoritmo pode se confundir ao tentar "dividir" a lista de forma incorreta, resultando em erros.

### Exemplo:
Imagine a lista `[1, 3, 5, 7, 9, 11, 13]` e o número `7` como alvo:

- Primeiro, o algoritmo verifica o elemento do meio: `5`. Como `7 > 5`, sabe que o número está na metade direita.
- Em seguida, encontra `9` e continua até chegar a `7`.

---

## 2. **Interpolation Search (Busca por Interpolação)**

### Quando o Interpolation Search é mais eficiente que o Binary Search?

O **Interpolation Search** é mais eficiente que o **Binary Search** quando os dados são distribuídos uniformemente. Ele "adivinha" a localização do valor com base na distribuição dos dados, enquanto o Binary Search sempre divide a lista ao meio.

---

## 3. **Jump Search**

### Comparação com Binary Search em listas de diferentes tamanhos:

O **Jump Search** pula um número fixo de elementos (geralmente a raiz quadrada do tamanho da lista) e realiza uma busca linear no bloco encontrado.

- Em listas pequenas, o **Binary Search** é geralmente mais rápido devido à complexidade `O(log n)`.
- Em listas grandes, o **Jump Search** pode ser vantajoso, pois realiza menos verificações preliminares.

---

## 4. **Exponential Search**

### Desempenho em listas grandes e pequenas:

- Em **listas pequenas**, o Exponential Search pode ser mais lento devido à sobrecarga inicial.
- Em **listas grandes**, é eficiente, pois encontra rapidamente o intervalo de pesquisa antes de usar a busca binária.

---

## 5. **Shell Sort**

### Como a escolha da sequência de intervalos afeta a eficiência?

O **Shell Sort** utiliza diferentes "gaps" para comparar elementos distantes. A escolha dos intervalos impacta diretamente a eficiência do algoritmo. Intervalos mal escolhidos podem resultar em maior número de comparações.

---

## 6. **Selection Sort**

### Análise de desempenho em listas pequenas, médias e grandes:

O **Selection Sort** seleciona o menor elemento e o coloca na posição correta em cada iteração. Com complexidade `O(n²)`, é adequado apenas para listas pequenas, sendo ineficiente em médias e grandes.

---

## 7. **Radix Sort**

### Como lida com diferentes bases (ex.: base 10 e base 2)?

O **Radix Sort** ordena números com base em seus dígitos, da menor posição para a maior. Em base 10, utiliza os dígitos de 0 a 9, enquanto em base 2, trabalha com os valores binários 0 e 1.

---

## 8. **Quick Sort**

### Desempenho em listas quase ordenadas e completamente desordenadas:

- **Listas quase ordenadas**: Muito eficiente, com complexidade `O(n log n)`.
- **Listas desordenadas**: A escolha inadequada do pivô pode levar ao pior caso, com complexidade `O(n²)`.

---

## 9. **Ternary Search (Busca Ternária)**

### Quando o Ternary Search seria mais eficiente que o Binary Search?

O **Ternary Search**, que divide a lista em três partes, pode ser mais eficiente em listas grandes e com dados distribuídos de forma não uniforme.
