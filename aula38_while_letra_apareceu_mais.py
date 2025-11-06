
'''frase = 'O Python é uma linguagem de programação' \
'multiparadgma. ' \
'Python foi criado por Guido Van Rossum.'

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''
while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qta_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qta_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qta_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual
    i += 1

print(f'A letra que apareceu mais vezes foi a "{letra_apareceu_mais_vezes}", '
      f'que apareceu {qtd_apareceu_mais_vezes} vezes.')'''

      

frase = 'Python é muito divertido!' # frase determinada para a contagem
i = 0 # índice inicial, começando do primeiro caractere

mais_frequente = '' # variável para armazenar a letra mais frequente
maior_contagem = 0 # variável para armazenar a maior contagem de aparições

while i < len(frase): # loop através de cada caractere na frase
    letra = frase[i] # caractere atual sendo analisado, ou seja, a letra na posição i

    if letra == ' ': # se o caractere for um espaço
        i += 1 # incrementa o índice para pular o espaço
        continue  # pula o espaço

    contagem = frase.count(letra) # conta quantas vezes a letra atual aparece na frase

    if contagem > maior_contagem: # se a contagem atual for maior que a maior contagem registrada
        maior_contagem = contagem # atualiza a maior contagem
        mais_frequente = letra # atualiza a letra mais frequente

    i += 1 # incrementa o índice para analisar o próximo caractere

print(f'A letra mais frequente é "{mais_frequente}" ({maior_contagem} vezes)')
