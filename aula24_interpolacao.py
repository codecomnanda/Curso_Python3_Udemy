"""
Interpolação básica de strings é a inserção de variáveis dentro de strings.
Existem 3 formas principais de fazer isso:
1 - Usando o operador %
2 - Usando o método format()
3 - Usando f-strings (a partir do Python 3.6)
s - 'String'
d e i - Int
f - Float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Luiz'
preco = 1000.9589765
variavel = '%s, o preço é R$%.2f' % (nome, preco) # operador %
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500)) # operador %