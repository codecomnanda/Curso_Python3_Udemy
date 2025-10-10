'''
Repetições 
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
loop infinito -> código que nunca termina
break (interrompe)
'''

'''
contador = 0
while contador < 10:
    contador = contador + 1
    print(contador)
print('Acabou!')
'''

'''
Operadores de atribuição no while
= += -= *= /= //= **= %=
'''
'''
contador = 0
while contador < 10:
    contador += 1 # contador = contador + 1
    print(contador)
'''

# Break
'''
contador = 0
while contador <= 10:
    contador += 1
    print(contador) # com o print antes do break, o 6 também é impresso, se for no final só vai até o 5
    if contador == 6:
        break # interrompe o loop
'''
    

# Continue - pula a iteração atual
contador = 0
while contador < 10:
    contador += 1
    if contador == 6:
        continue # pula o 6. O continue faz com que o código volte para o início do loop
    print(contador)