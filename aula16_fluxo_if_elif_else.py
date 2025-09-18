# if / elif      / else
# se / se não se / se não

condicao1 = True
condicao2 = True
condicao3 = True
condicao4 = True

if condicao1: # pode viver sem o elif e o else, mas não pode viver sem o if
    print('Código para condição 1')
    print('Código para condição 1')
elif condicao2: # não pode ser usado sem o if
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')
else: # não pode ser usado sem o if
    print('Nenhuma condição foi satisfeita.')

if 10 == 10:
    print('Outro if')

print('Fora do if')