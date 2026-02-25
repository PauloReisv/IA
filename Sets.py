#Sets são conjuntos não ordenados de elementos. Para sets usamos chaves.

animais = {'gato', 'cachorro'}
print('gato' in animais) 
# Verifica se um elemento está no set e mostra "True"

print('peixe' in animais) 
# Mostra "False"

animais.add('peixe') 
# Inclui um elemento no set

print('peixe' in animais) 
# Mostra "True"

print(len(animais)) 
# Identifica o número de elementos do set e mostra "3"

animais.add('gato') 
# Incluir um elemento que já existem não faz nada

print(len(animais)) 
# Mostra "3"

animais.remove('gato') 
# Remove um elemento do set

print(len(animais)) 
# Mostra "2"