"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
'''
hora = input('Que horas são? ')
if hora.isdigit(): # isdigit() -> verifica se é um número inteiro positivo
    hora = int(hora) # convertendo string para inteiro
    if hora >= 0 and hora <= 11:
        print('Bom dia!')
    elif hora >= 12 and hora <=17:
        print('Boa tarde!')
    elif hora >=18 and hora <=23:
        print('Boa noite!')
else:
    print('Por favor, digite um número inteiro válido!')
'''

# Outra forma de fazer com try/except

hora = input("Que horas são? ")
try:
    hora = int(hora)
except ValueError:
    print("Por favor, digite um número inteiro válido!")
if hora >= 0 and hora <= 11:
    print("Bom dia!")
elif hora >= 12 and hora <= 17:
        print("Boa tarde!")
elif hora >= 18 and hora <= 23:
        print("Boa noite!")
else:
    print("Por favor, digite um número inteiro entre 0 e 23!")


