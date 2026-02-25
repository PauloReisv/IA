"""
Um Dicionário é um conjunto de valores, um a um, associados a uma chave de acesso. Um 
dicionário em Python é declarado dentro de chaves com cada chave e valor separado por “:” e 
cada conjunto de chave e valor separados por vírgulas conforme o exemplo abaixo que tem
para cada valor de produto um nome associado como chave:
Precos = {'lapis': 5.5, 'borracha': 7.0, 'caneta': 6.5}
Para mostrar todo o dicionário basta indicar o nome do dicionário no print:
Print(Precos)
Para acessar um valor específico do dicionário basta usar o nome do dicionário e a chave entre 
parênteses:
print("o preco da borracha eh:", Precos ['borracha'])
Algumas funções dos dicionários que podem ser úteis são:
a) del: exclui um item informando a chave.
Exemplo: del Precos[’borracha’] retirará ‘borracha’ e deixará Precos com [‘lapis’: 5.5, ‘caneta’:
6.5]
b) in: verificar se uma chave existe no dicionário.
Exemplo: ‘caneta’ in Precos retorna True e ‘caderno’ in Precos retorna False
c) keys ( ) : obtém as chaves de um dicionário. 
Exemplo: Precos.keys ( ) retorna dict_keys([‘lapis’, ‘borracha’, ‘caneta’]) 
d) values ( ): obtém os valores de um dicionário. 
Exemplo: Precos.values ( ) retorna dict_values([5.5, 7.0, 6.5])
Executando os exemplos citados temos:
"""

Precos = {'lapis': 5.5, 'borracha': 7.0, 'caneta': 6.5}
print(Precos)
print("o preco da borracha eh:", Precos ['borracha'])
print(Precos.keys())
print(Precos.values())
print('caneta' in Precos)
print('caderno' in Precos)
del Precos['borracha']
print(Precos)

d = {'gato': 'cat', 'cachorro': 'dog'} 
# Cria um novo dicionário com alguns dados

print(d['gato']) 
# Identifica significado de uma entrada e mostra "cat"

print('gato' in d) 
# Verifica se uma chave está e mostra "True"

print(d)
d['peixe'] = 'fish' 
# Inclui um element em um dicionário

print(d['peixe']) 
# Mostra "fish"

print(d['macaco']) 
# KeyError: 'macaco' porque não é uma chave do dicionário d

print(d.get('macaco', 'N/A')) 
# Busca um elemento com valor default para falha, mostra "N/A"

print(d.get('peixe', 'N/A')) 
# Busca um elemento com valor default para falha, mostra "fish"

del d['peixe'] 
# Remove um element do dicionário

print(d.get('peixe', 'N/A'))
# Busca um elemento com valor default para falha, mostra "N/A"