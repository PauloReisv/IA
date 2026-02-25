# Tuplas são listas que não podem ser alteradas. Em tuplas usamos parênteses “( )” ao invés de colchetes “[ ]” como em listas. 

tp1 = (1,2,3,4,5,6)
# Cria uma tupla

print(tp1)
# Mostra a tupla (1, 2, 3, 4, 5, 6)
print(tp1[4])
# Mostra “5”

d = {(0, 1): 0, (1, 2): 1, (2, 3): 2, (3, 4): 3, (4, 5): 4,
(5, 6): 5, (6, 7): 6, (7, 8): 7, (8, 9): 8, (9, 10): 9}
# Cria dicionários com tuplas como chaves
print(d)
# Mostra todas as tuplas do dicionário
tp2 = (5, 6) 
# Cria uma tupla
print(type(tp2)) 
# Mostra "<class 'tuple'>"
print(d[tp2]) 
# Mostra "5"
print(d[(1, 2)]) 
# Mostra "1"

d = {(x, x + 1): x for x in range(10)}
# Cria dicionários com tuplas como chaves

print(d)
# Mostra todas as tuplas do dicionário
# {(0, 1): 0, (1, 2): 1, (2, 3): 2, (3, 4): 3, (4, 5): 4, 
# (5, 6): 5, (6, 7): 6, (7, 8): 7, (8, 9): 8, (9, 10): 9}

tp2 = (5, 6) 
# Cria uma tupla

print(type(tp2)) 
# Mostra "<class 'tuple'>"

print(d[tp2]) 
# Mostra "5"

print(d[(1, 2)]) 
# Mostra "1"