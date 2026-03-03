"""
A Estrutura de repetição também conhecida como “loop” é utilizada para executar uma 
sequência de comandos por várias vezes. A repetição está associada ou a uma condição, que 
indica se deve continuar a repetição, ou a uma sequência de valores, que determina quantas 
vezes a sequência deve ser repetida.  
4.1 Laço while  
No laço while, o trecho de código da repetição está associado a uma condição. Enquanto a 
condição tiver valor verdadeiro, o trecho é executado. Quando a condição passa a ter valor 
falso, a repetição termina.  
Sintaxe:  
while <condição>: 
<instruções>  
Exemplo:  
"""

senha = "54321"  
leitura =" "  
while (leitura != senha):  
    leitura = input("Digite a senha: ")  
    if leitura == senha : print('Acesso liberado ')  
    else: print('Senha incorreta. Tente novamente')  

"""
----------------------------------------------------------------------------------------------------- 
Digite a senha: 12345 
Senha incorreta. Tente novamente 
Digite a senha: abcde 
Senha incorreta. Tente novamente 
Digite a senha: 54321 
Acesso liberado 
Exemplo: Encontrar a soma de 5 valores.  
"""

contador = 0  
somador = 0  
while contador < 5:  
contador = contador + 1  
valor = float(input('Digite o '+str(contador)+'º valor: '))  
somador = somador + valor  
print('Soma = ', somador)

"""
 ----------------------------------------------------------------------------------------------------- 
Digite o 1º valor: 1 
Digite o 2º valor: 2 
Digite o 3º valor: 3 
Digite o 4º valor: 4 
Digite o 5º valor: 5 
Soma =  15.0 
4.2 Laço for  
O laço for é a estrutura de repetição mais utilizada em Python. Pode ser utilizado com uma 
sequência numérica (gerada com o comando range) ou associado a uma lista. O trecho de 
código da repetição é executado para cada valor da sequência numérica ou da lista.  
Sintaxe:  
for <variável> in range (<início>, <limite>, <passo>): 
<instruções>   
ou  
for <variável> in <lista>:  
<instruções>   
Exemplos:  
a) Encontrar a soma S = 1+4+7+10+13+16+19  
"""

S=0  
for x in range(1,20,3):  
    S = S+x  
print('Soma = ',S)

"""
----------------------------------------------------------------------------------------------------- 
Soma =  70 
b) As notas de um aluno estão armazenadas em uma lista. Calcular a média dessas notas. 
"""

Lista_notas= [3.4,6.6,8,9,10,9.5,8.8,4.3]  
soma=0  
for nota in Lista_notas:  
    soma = soma+nota  
    média = soma/len(Lista_notas)  
print('Média = ', '{:.4f}'.format(média))

"""
----------------------------------------------------------------------------------------------------- 
Média =  7.4500 
É importante notar que todas estas estruturas de controle de fluxo de execução podem estar 
dentro das funções que aprendemos a declarar. Veja exemplos anteriores implementados 
como funções que permitem a execução com qualquer coleção de dados de entrada. 
"""

def CalcMedia(lista):
    soma=0  
    for nota in lista:  
        soma = soma+nota  
    return soma/len(lista)  

Lista_notas= [3.4,6.6,8,9,10,9.5,8.8,4.3]  
media = CalcMedia(Lista_notas) 
print('Média = ', '{:.4f}'.format(media))

"""
----------------------------------------------------------------------------------------------------- 
Média =  7.4500 
No caso de estruturas de decisão isso também é verdade. Veja como fica como função o 
código que indica a categoria a partir da idade. 
"""

def categoria(idade): 
    if idade < 3: 
        ctg = 'Bebê'  
    elif idade < 10: 
        ctg = 'Infantil'  
    elif idade < 14: 
        ctg = 'Junior'  
    elif idade < 18: 
        ctg = 'Adolescente'  
    elif idade < 30: 
        ctg = 'Jovem'  
    else: 
        ctg = 'Adulto'  
    return ctg 
   
idd = int(input("Digite sua idade:")) 
print("Sua categoria é:", categoria(idd))

"""
 ----------------------------------------------------------------------------------------------------- 
Digite sua idade:23 
Sua categoria é: Jovem 
Já uma função “MaiorValor” para retornar o maior número de uma lista precisa de usar tanto 
as estruturas de repetição quanto as estruturas de repetição. Veja: 
"""
def MaiorValor(lista): 
  if len(lista) > 0: 
    maior = lista[0] 
  else: 
    maior = 0;      
  for valor in lista:  
    if valor > maior: 
      maior = valor  
  return maior 
 
ListaNotas= [3.4,6.6,8,9,10,9.5,8.8,4.3]  
resultado = MaiorValor(ListaNotas) 
print(resultado)

"""
----------------------------------------------------------------------------------------------------- 
10  
Para ler uma lista basta usar a instrução “for” com o “range”. Veja esta função “Leitura” que 
recebe uma lista e inclui uma determinada quantidade de valores inteiros na lista: 
"""

def Leitura(lista,qtd): 
  for i in range(1,qtd+1):  
    lista.append(int(input("Digite o valor do elemento "))) 
 
ListaNotas= []  
Leitura(ListaNotas,5) 
print(ListaNotas)

"""
----------------------------------------------------------------------------------------------------- 
Digite o valor do elemento 1 
Digite o valor do elemento 2 
Digite o valor do elemento 3 
Digite o valor do elemento 4 
Digite o valor do elemento 5 
[1, 2, 3, 4, 5] 
Agora veremos um exemplo de uso de funções com dicionários. Neste exemplos criamos uma 
agenda simples com nomes e telefones: 
"""

def cria(): 
    d = {}  
    return d 
 
def inclui(d):   
    nome = input("Digite o nome a incluir: ") 
    if nome in d: 
        print("Nome já existe não pode ser incluído") 
    else:     
        fone = input("Digite o fone: ") 
        d[nome]=fone  
 
def consulta(d): 
    nome = input("Digite o nome a consultar: ") 
    print("Telefone: ",d.get(nome, 'Não disponível')) 
 
def altera(d): 
    nome = input("Digite o nome do fone a alterar: ") 
    print("Telefone atual: ",d.get(nome, 'Não disponível')) 
    if nome in d: 
        fone = input("Digite o novo fone: ") 
        d[nome]=fone 
        print("Telefone alterado!") 
    else: 
        print("Telefone não pode ser alterado!") 
 
def exclui(d): 
    nome = input("Digite o nome a excluir: ") 
    if nome in d: 
        del d[nome] 
        print("Nome e fone excluídos!") 
    else: 
        print("Nome Inexistente!") 
   
def mostra(d): 
    print("Agenda:") 
    for nome in d.keys():  
        print(nome,d[nome]) 
 
agenda = cria() 
inclui(agenda) 
inclui(agenda) 
inclui(agenda) 
consulta(agenda) 
altera(agenda) 
exclui(agenda) 
mostra(agenda)

"""
----------------------------------------------------------------------------------------------------- 
Digite o nome a incluir: Marcelo 
Digite o fone: 11111 
Digite o nome a incluir: Helena 
Digite o fone: 22222 
Digite o nome a incluir: Marcelo 
Nome já existe não pode ser incluído 
Digite o nome a consultar: Cynthia 
Telefone:  Não disponível 
Digite o nome do fone a alterar: Helena 
Telefone atual:  22222 
Digite o novo fone: 33333 
Telefone alterado! 
Digite o nome a excluir: Cynthia 
Nome Inexistente! 
Agenda: 
Marcelo 11111 
Helena 33333 
 
Uma possível alternativa para o programa principal é a apresentação de um menu de opções: 
"""
 
agenda = cria() 
opc = 10 
while opc != 0: 
    opc = int(input("Digite 0.Sair,1.Inc,2.Con,3.Alt,4.Exc,5.Most:")) 
        if opc == 1: 
        inclui(agenda) 
    elif opc == 2: 
        consulta(agenda) 
    elif opc == 3: 
        altera(agenda) 
    elif opc == 4: 
        exclui(agenda) 
    elif opc == 5: 
        mostra(agenda) 
    elif opc == 0: 
        print("Bye!") 
    else: 
        print("Opção inválida!")  