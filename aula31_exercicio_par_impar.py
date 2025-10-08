"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

num = input('Digite um número inteiro: ')
if num.isdigit():
    num = int(num)
    if num % 2 == 0:
        print(f'O número {num} é par.')
    else:
        print(f'O número {num} é ímpar.')
else:
    print('Isso não é um número inteiro!')

# Outra forma de fazer
