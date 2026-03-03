"""
Um dos recursos que as vezes precisamos considerar é o de receber valores de quem está 
usando a aplicação. Isto permite que as funções e conjunto de instruções em Python no Colab 
se tornem mais genéricas sem necessidade de alterá-las a todo o momento para alterar 
determinados valores. Para isso é possível utilizar a instrução “input”. A instrução “input” para 
a execução da célula ou função, solicita ao usuário que digite um determinado valor e após a 
digitação do valor atribui para uma eventual variável o valor digitado. 
Veja o exemplo: 
"""
def leitura(): 
    nome = input("Digite seu nome:") 
    sobrenome = input("Digite seu sobrenome:") 
    nomecompleto = nome+" "+sobrenome 
    print("seu nome completo eh: ",nomecompleto)   
leitura()
"""
Digite seu nome:joao 
Digite seu sobrenome:Souza 
seu nome completo eh:  joao Souza    
Note que quando você executa o código a execução para a cada instrução input e apresenta 
uma caixa de texto a ser preenchida conforme a figura 1: 
Figura 1. Caixa de texto de entrada de dados 
Esta será a forma padrão de eventuais entradas de dados. Note que a variável nome e 
sobrenome se tornam variáveis tipo String e por isso se a entrada de dados necessita ser de 
um tipo específico é necessário fazer a conversão indicando o tipo para o qual a entrada deve 
ser transformada. Para isso, utiliza-se o int (string) para converter para o tipo inteiro, ou float 
(string) para converter para o tipo float. Veja os exemplos: 
Exemplo com tipo de dados int (inteiro):   
"""
def potencia(a,b):
    c = a**b
    return c
    
x = int(input("Digite um valor:")) 
y = int(input("Digite o valor de potência:")) 
print(potencia(x,y))
"""
Digite um valor:3 
Digite o valor de potência:4 
81 
Outro exemplo agora com o tipo de dados float (ponto flutuante):  
"""
def soma(a,b): 
    c=a+b 
    return c 
    
x = float(input("Digite um valor:"))
y = float(input("Digite um valor:"))
print(soma(x,y))
"""
Digite um valor:3.24 
Digite um valor:5.4 
8.64 
Em termos de formatação existem duas formas de contornar os problemas com números em 
ponto flutuante em termos de apresentação. Uma é usando um recurso do Python 2 que é o 
formato entre aspas no print. Outra forma de resolver é usando a função format, ou ainda usar 
a função round. Como nosso foco não é este não vamos discutir o problema em detalhes mas 
seguem alguns exemplos de formatação.  
a) format para String: “:[preencher][alinhar][largura].[precisão]”.format(<string>) 
Onde:  
[preencher]: Qualquer caractere.  
[alinhar]: “<” para alinhar à esquerda, “>” à direita e “^” ao centro.  
[largura]: Largura mínima do campo. 
[precisão] Largura máxima do campo. 
Veja um exemplo: 
"""
s = 'Teste String' 
# alinha a direita com 20 espaços em branco
print("{0:>20}".format(s))
# alinha a direita com 20 símbolos #
print("{0:#>20}".format(s))
# alinha ao centro com 10 “ “ a esquerda e 10 “ “ a direita
print("{0:^20}".format(s))
# imprime só as primeiras cinco letras
print("{0:.5}".format(s))
"""
Teste String 
########Teste String 
Teste String     
Teste 
b) format para números: “:[preencher][alinhar][sinal][largura].[precisão][tipo]”.format(<num>) 
Onde: 
[preencher]: Qualquer caractere.  
[alinhar]: “<” para alinhar à esquerda, “>” à direita e “^” ao centro.  
[sinal]: + se apresentar 
[largura]: Largura mínima do campo. 
[precisão] Largura máxima do campo. 
[tipo]: d ou i (inteiro), f ou F (float), o (octal), x ou X (hexadecimal), e ou E (exponencial)   
Veja o exemplo: 
"""
print("{0:4}".format(-123))
# aparece '-123' 
print("{0:4}".format(123))
# aparece ' 123' 
print("{0:4.2f}".format(33.3287))
# aparece '33.33' 
print("{0:+4.2f}".format(33.3287))
# aparece '+33.33' 
print("{0:+4.2e}".format(33.3287))
# aparece '+3.33e+01' 
print("{0:b}".format(123))
# aparece '1111011'
"""
123 
33.33 
+33.33 
+3.33e+01 
1111011 
Quem estiver interessado em ler mais sobre o problema de ponto flutuante leia sobre isso em: 
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html 
Para o controle do fluxo de execução em funções no Python existem instruções específicas que 
indicam as condições e iterações. A seguir conheceremos estas estruturas.  
"""