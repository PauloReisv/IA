"""
A lista é uma estrutura mutável, ou seja, ela pode ser modificada. S seguir estão algumas 
funções utilizadas para manipular listas:
a) len: retorna o tamanho da lista. 
Exemplo: L = [1, 2, 3, 4] e len(L) retorna 4
b) min: retorna o menor valor da lista. 
Exemplo: L = [10, 40, 30, 20] e min(L) retorna 10
c) max: retorna o maior valor da lista. 
Exemplo: L = [10, 40, 30, 20] e max(L) retorna 40
d) sum: retorna soma dos elementos da lista. 
Exemplo: L = [10, 20, 30] e sum(L) retorna 60
e) append: adiciona um novo valor na no final da lista.
Exemplo: L = [1, 2, 3] e L.append(100) gera L [1, 2, 3, 100]
f) extend: insere uma lista no final de outra lista.
Exemplo: L = [0, 1, 2] e L.extend([3, 4, 5]) gera L [0, 1, 2, 3, 4, 5]
g) del: remove um elemento da lista, dado seu índice.
Exemplo: L = [1,2,3,4] e del L[1] gera L [1, 3, 4]
h) in: verifica se um valor pertence à lista. 
Exemplo: L = [1, 2 , 3, 4] e 3 in L retorna True
i) sort( ): ordena em ordem crescente
Exemplo: L = [3, 5, 2, 4, 1, 0] e L.sort( ) gera L [0, 1, 2, 3, 4, 5]
j) reverse( ): inverte os elementos de uma lista.
Exemplo: L = [0, 1, 2, 3, 4, 5] e L.reverse( ) gera L [5, 4, 3, 2, 1, 0]
Execute o código abaixo para entender melhor:
"""
xs = [3, 1, 2, 'texto'] 
# Cria a lista

print(xs, xs[2]) 
# Mostra "[3, 1, 2] 2"

print(xs[-1]) 
# Indices negativos contam a partir do fim da lista e mostra "2"

xs[2] = 'texto' 
# Listas podem ter elementos de tipos diferentes

print(xs) 
# Mostra "[3, 1, 'texto']"

xs.append('outro') 
# Coloca um novo elemento no fim da lista

print(xs) 
# Mostra "[3, 1, 'texto', 'outro']"

x = xs.pop() 
# Remove e retorna o ultimo elemento da lista

print(x, xs) 
# Mostra "bar [3, 1, 'texto']"

animais = ['gato', 'cachorro', 'macaco']
# A seguir um Loop com a lista animais

for animal in animais:
 print(animal)
# O recurso de Loop (repetição) acima conheceremos na próxima aula

"""
É possível também fazermos operações com diversas listas:
a) Concatenação ( + ): coloca a 2a lista após a1a. lista formando uma com todos elementos
Exemplo: se tivermos a = [0,1,2] e b = [3,4,5], então c = a + b gera c=[0, 1, 2, 3, 4, 5]
b) Repetição ( * ): cria uma lista com n vezes os elementos da original
Exemplo: se tivermos L = [1,2] então R = L * 4 gera R= [1, 2, 1, 2, 1, 2, 1, 2]
c) Fatiamento: O fatiamento de listas é semelhante ao fatiamento de strings.
Exemplo: se tivermos L = [3 , 'abacate' , 9.7 , [5 , 6 , 3] , "Python" , (3 , 'j')] então
L[1:4] seleciona os elementos das posições 1,2,3 e gera ['abacate', 9.7, [5, 6, 3]]
L[2:] seleciona os elementos a partir da posição 2 e gera [9.7, [5, 6, 3], 'Python', (3, 'j')]
L[:4] seleciona os elementos até a posição 3 e gera [3, 'abacate', 9.7, [5, 6, 3]]
Por fim, é possível criar listas com range ( ). A função range() define um intervalo de valores 
inteiros. Associada a list(), cria uma lista com os valores do intervalo. A função range() pode ter 
de 1 a 3 parâmetros (compreenderemos melhor funções na próxima aula):
- range(n) gera um intervalo de 0 a n-1
- range(i , n) gera um intervalo de i a n-1
- range(i , n, p) gera um intervalo de i a n-1 com intervalo p entre os números
Exemplos:
L1 = list(range(5)) gera [0, 1, 2, 3, 4]
L2 = list(range(3,8)) gera [3, 4, 5, 6, 7]
L3 = list(range(2,11,3)) gera [2, 5, 8]
Execute o código abaixo para entender melhor:
"""

l1 = list(range(5))
print(l1)
l2 = list(range(3,8))
print(l2)
l3 = list(range(2,11,3))
print(l3)
l4 = l1 + l2
print(l4)
l5 = l3 * 4
print(l5)
l6 = [9 , 'texto' , 5.7 , [16, 11 , 18] , "Python" , [7 , 8]]
print(l6)
l7 = l6[1:4]
print(l7)
l8 = l6[2:]
print(l8)
l9 = l6[:4]
print(l9)
