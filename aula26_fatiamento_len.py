"""
Fatiamento de strings
012345678
Olá Mundo
-987654321
Fatiamento [i:f:p] (início:fim:passo) [::]
Obs: a função len retorna a quantidade de caracteres da string
"""

variavel = 'Olá Mundo'
print(variavel [5]) # Imprime o caractere na posição 5
print(variavel[-4]) # Começa de trás para frente
print(variavel[4:]) # Começa na posição 4 e vai até o final
print(variavel[:5]) # Começa do início e vai até a posição 5
print(variavel[4:8]) # Começa na posição 4 e vai até a posição 8
print(len(variavel)) # len Retorna a quantidade de caracteres da string
print(len(variavel[3])) # Retorna a quantidade de caracteres do caractere na posição 3 
print(variavel[0:9:2]) # Começa na posição 0, vai até a posição 9, pulando de 2 em 2
print(variavel[::2]) # Começa no início, vai até o final, pulando de 2 em 2
print(variavel[::-1]) # Inverte a string