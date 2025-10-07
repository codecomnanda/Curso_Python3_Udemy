"""
Formatação Básica de Strings (f-strings)
s - String
d - Int
f - Float
.<número de dígitos>f - Quantidade de dígitos (float)
x e X - Hexadecimal 
(Caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - centro
Sinal + ou -  (espaço)
Ex: 0>-100,.1f
Conversion flags !r !s !a
"""
variavel = 'ABC'
print(f'{variavel}') # Interpolação básica
print(f'{variavel:>10}.') # Alinhado à direita
print(f'{variavel:<10}.') # Alinhado à esquerda
print(f'{variavel:^10}.') # Alinhado ao centro
print(f'{variavel:$^10}.') # Alinhado ao centro com $ preenchendo
print(f'{1000.4925465:,.1f}') # Formatação de número

