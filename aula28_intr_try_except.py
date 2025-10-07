'''
Introdução ao Try / Except
Try -> Tentar executar o código
Except -> Ocorreu algum erro ao tentar executar o código
'''
# O if não evita erros ele checa a condição e muda o fluxo do código
# O try tenta executar o código e se der erro ele pula para o except

num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')
try:
    print(f'A soma é {int(num1) + int(num2)}') # Tenta converter para inteiro e somar
except: # Se der erro ele cai aqui
    print('Um dos valores digitados não é um número inteiro.')