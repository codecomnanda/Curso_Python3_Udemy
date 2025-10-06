# Operaddores in e not in
# Strings são iteráveis
# 0 1 2 3 4 5 
# P y t h o n
#-6-5-4-3-2-1

#nome = 'Python'
#print(nome [2])
#print(nome [-5])

#print('th' in 'Python') # True
#print('py' in 'Python') # False

#print( 10 * '-')

#print('py' not in 'Python') # True
#print('thon' not in 'Python') # False

nome = input('Qual seu nome? ')
encontrar = input('Qual letra deseja encontrar no seu nome? ')
if encontrar in nome:
    print(f'Sim, existe a letra {encontrar} no seu nome')
else:
    print(f'Não, não existe a letra {encontrar} no seu nome')

