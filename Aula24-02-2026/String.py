nome = 'Jose da Silva'
print(nome)
n = 'Joao'
sn = 'Souza'
nc = n + ' ' + sn
print(nc)

"""
Existem uma série de funções para manipulações de strings Segue uma relação delas:
a) len(): Retorna o tamanho da string. 
Exemplo: Em teste = “Apostila de Python” o uso len(teste) retorna 18 
b) capitalize(): Retorna a string com a primeira letra maiúscula.
Exemplo: Em a = "python" o uso a.capitalize() gera 'Python' 
c) count(): Informa quantas vezes um caractere (ou uma sequência de caracteres) aparece na 
string. 
Exemplo: Em b = "Linguagem Python" o uso b.count("n") retorna 2 
d) startswith(): Verifica se uma string inicia com uma determinada sequência. 
Exemplo: Em c = "Python" o uso c.startswith("Py") retorna True 
e) endswith(): Verifica se uma string termina com uma determinada sequência. 
Exemplo: Em d = "Python" o uso d.endswith("Py") retorna False 
f) isalnum(): Verifica se a string possui algum conteúdo alfanumérico (letra ou número). 
Exemplo: Em e = "!@#$%" o uso e.isalnum() retorna False 
g) isalpha(): Verifica se a string possui apenas conteúdo alfabético. 
Exemplo: Em f = "Python" o uso f.isalpha() retorna True 
h) islower(): Verifica se todas as letras de uma string são minúsculas. 
Exemplo: Em g = "pytHon" o uso g.islower() retorna False 
i) isupper(): Verifica se todas as letras de uma string são maiúsculas. 
Exemplo: Em h = "# PYTHON 12" o uso h.isupper() retorna True 
j) lower(): Retorna uma cópia da string trocando todas as letras para minúsculo. 
Exemplo: Em i = "#PYTHON 3" o uso i.lower() gera '#python 3' 
k) upper(): Retorna uma cópia da string trocando todas as letras para maiúsculo. 
Exemplo: Em j = "Python" o uso j.upper() gera 'PYTHON' 
l) swapcase(): Inverte o conteúdo da string (Minúsculo / Maiúsculo). 
Exemplo: Em k = "Python" o uso k.swapcase() gera 'pYTHON' 
m) title(): Converte para maiúsculo todas as primeiras letras de cada palavra da string. 
Exemplo: Em l = "apostila de python" o uso l.title() gera 'Apostila De Python' 
n) split(): Transforma a string em uma lista, utilizando os espaços como referência. 
Exemplo: Em m = "cana de açúcar" o uso m.split() gera ['cana', 'de', 'açúcar'] 
o) replace(S1, S2): Substitui na string o trecho S1 pelo trecho S2. 
Exemplo: Em n = "Apostila teste" o uso n.replace("teste", "Python") gera 'Apostila Python' 
p) find(): Retorna o índice da primeira ocorrência de um determinado caractere na string. Se o 
caractere não estiver na string retorna -1. 
Exemplo: Em o = "Python" o uso o.find("h") restorna 3 
q) ljust(): Ajusta a string para um tamanho mínimo, acrescentando espaços à direita se 
necessário. 
Exemplo: Em p = " Python" o uso p.ljust(15) gera ' Python ' 
r) rjust(): Ajusta a string para um tamanho mínimo, acrescentando espaços à esquerda se 
necessário. 
Exemplo: Em q = "Python" o uso q.rjust(15) gera ' Python' 
s) center() Ajusta a string para um tamanho mínimo, acrescentando espaços à esquerda e à 
direita, se necessário. 
Exemplo: Em r = "Python" o uso r.center(10) gera ' Python ' 
t) lstrip(): Remove todos os espaços em branco do lado esquerdo da string. 
Exemplo: Em s = " Python " o uso s.lstrip() gera 'Python ' 
u) rstrip(): Remove todos os espaços em branco do lado direito da string. 
Exemplo: Em t = " Python " o uso t.rstrip() gera ' Python' 
v) strip(): Remove todos os espaços em branco da string. 
Exemplo: Em u = " Python " o uso u.strip() gera 'Python'
Além dessas funções existe ainda a possibilidade de fatiamento de Strings que permite extrar 
do string apenas uma parte dos elementos de uma string. 
O fatiamento é uma ferramenta usada para extrair apenas uma parte dos elementos de uma 
string. O formato usado é:
NomeDoString [LimiteInferior : LimiteSuperior]
Ele retorna string com os elementos das posições do limite inferior até o limite superior - 1.
Exemplos:
Para s = "Python" o uso s[1:4] seleciona os elementos das posições 1,2,3 e gera 'yth'
Para s = "Python" o uso s[2:] seleciona os elementos a partir da posição 2 e gera 'thon'
Para s = "Python" o uso s[:4] seleciona os elementos até a posição 3 e gera 'Pyth'
"""

hello = 'hello' 
# String literais se usa aspa simples

world = "world" 
# ou aspas dupla indiferentemente

print(hello) 
# Mostra "hello"

print(len(hello)) 
# Identifica o tamanho da String e mostra “5”

hw = hello + ' ' + world 
# Operador “+” concatena Strings 

print(hw) 
# Mostra "hello world"

hw12 = '%s %s %d' % (hello, world, 12) 
# formata como o printf da linguagem C

print(hw12) 
# Mostra "hello world 12"


hw12 = '{} {} {}'.format(hello, world, 12)
print(hw12)
# Mostra "hello world 12"

s = "hello"
print(s.capitalize()) 
# Coloca em maiúsculo o 1a letra e mostra "Hello"

print(s.upper()) 
# Converte para maiúsculo tudo e mostra "HELLO"

print(s.rjust(7)) 
# Justifica à direita e mostra " hello"

print(s.center(7)) 
# Centraliza e mostra " hello "

print(s.replace('l', '(ell)')) 
# troca todos ‘l’ por ‘ell’ e mostra "he(ell)(ell)o"

print(' world '.strip()) 
# Tira os espaços e mostra "world  