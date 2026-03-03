"""
As estruturas de decisão permitem alterar o fluxo de execução de um programa, percorrendo 
um ou outro conjunto de instruções de acordo com o valor (Verdadeiro/Falso) de um teste 
lógico. Em Python temos as estruturas de decisão “se” (if), “se/senão” (if..else) e “se/senão 
se/senão” (if..elif..else) 
A instrução if é utilizado quando precisamos decidir se um trecho do programa deve ou não 
ser executado. Ele é associado a uma condição, e o trecho de código será executado se o valor 
da condição for verdadeiro.  
Sintaxe:  
if <condição>:  
<instruções> 
Exemplo:  
"""
nota = float(input("Digite sua nota na disciplina:")) 
if nota < 6.0: 
print('Reprovado!')

"""
----------------------------------------------------------------------------------------------------- 
Digite sua nota na disciplina:5.5 
Reprovado! 
Na instrução if..else um trecho de código será executado se a condição for verdadeira e outro 
se a condição for falsa.  
Sintaxe:  
if <condição1>:  
<instruções1> 
else :  
<instruções2> 
Exemplo:   
"""

nota = float(input("Digite sua nota na disciplina:")) 
if nota >= 6.0: 
    print('Aprovado!')  
else: 
    print('Reprovado!')

"""
----------------------------------------------------------------------------------------------------- 
Digite sua nota na disciplina:5.66 
Reprovado! 
A instrução if..elif..else é usada quando houver diversas condições, cada uma associada a um 
trecho de código. 
Sintaxe:  
if <condição1>:  
<instruções1> 
elif <condição2>:  
<instruções2> 
elif <condição3>:  
<instruções3> 
... 
else :  
<instruçõesN> 
Note que somente o bloco de comandos associado à 1a condição verdadeira encontrada será 
executado. Se nenhuma das condições tiver valor verdadeiro, executa o bloco de comandos 
default.  
Exemplo: 
"""

idade = int(input("Digite sua idade:")) 
if idade < 3: 
    print('Bebê')  
elif idade < 10: 
    print('Infantil')  
elif idade < 14: 
    print('Junior')  
elif idade < 18: 
    print('Adolescente')  
elif idade < 30: 
    print('Jovem')  
else: 
    print('Adulto')

"""
----------------------------------------------------------------------------------------------------- 
Digite sua idade:10 
Junior 
"""