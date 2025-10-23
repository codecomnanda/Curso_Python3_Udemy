'''
Iterando strings com while

nome = 'Fernanda Guimarães' # Iteráveis
tamanho_nome = len(nome) # len() -> função que retorna o tamanho de uma string
print(nome)
print(tamanho_nome)
print(nome[3]) 

'''
nome = 'Fernanda Guimarães'
tamanho_nome = len(nome) # len() -> função que retorna o tamanho de uma string
indice = 0
while indice < tamanho_nome: # enquanto indice for menor que o tamanho do nome
    print(f'*{nome[indice]}', end='') # end='' -> para não pular linha
    indice += 1 # incrementa o índice, ou seja, soma +1 a cada iteração
print('*')