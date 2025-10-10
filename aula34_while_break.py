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
'''
contador = 0
while contador < 10:
    contador += 1
    if contador == 6:
        continue # pula o 6. O continue faz com que o código volte para o início do loop
    print(contador)
'''

# while dentro de while

qtd_linhas = 5 
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas: # enquanto linha for menor ou igual a qtd_linhas
    print("--------")  # separa visualmente o início de cada nova linha
    coluna = 1 # reiniciando a coluna para 1 a cada nova linha
    while coluna <= qtd_colunas: # enquanto coluna for menor ou igual a qtd_colunas
        print(f'({linha=}, {coluna=})') # imprime o valor de linha e coluna
        coluna += 1 # incrementa a coluna
    linha += 1 # incrementa a linha


'''
🧠 CÓDIGO ORIGINAL EXPLICADO
qtd_linhas = 5 
qtd_colunas = 5


👉 Aqui você define quantas linhas e quantas colunas quer percorrer.
Ou seja, você quer formar uma espécie de tabela 5x5, percorrendo linha por linha, coluna por coluna.

linha = 1


👉 Começamos com a primeira linha.
Vamos percorrer as linhas de 1 até 5.

while linha <= qtd_linhas: 


👉 Este é o primeiro loop (externo).
Ele vai repetir enquanto linha for menor ou igual a 5.
Cada vez que ele roda, significa que estamos em uma nova linha da tabela.

    coluna = 1


👉 Antes de começar a rodar as colunas, a gente zera (ou melhor, reinicia) a contagem de colunas pra 1.
Isso é importante, porque quando mudar de linha, precisamos começar novamente da coluna 1.

    while coluna <= qtd_colunas:


👉 Este é o segundo loop (interno).
Ele vai repetir enquanto a coluna for menor ou igual a 5.
Ou seja, dentro de cada linha, ele percorre todas as colunas.

        print(f'({linha=}, {coluna=})')


👉 Aqui ele mostra na tela qual é o número da linha e da coluna atual.
O f'({linha=}, {coluna=})' é só um jeito de formatar bonito, pra aparecer algo como:

(linha=1, coluna=1)
(linha=1, coluna=2)
(linha=1, coluna=3)
...

        coluna += 1


👉 Aumenta o valor da coluna em 1.
Assim, o while interno vai para a próxima coluna até chegar na 5ª.

    linha += 1


👉 Quando o while interno acaba (ou seja, depois de percorrer as 5 colunas),
o código volta pro while externo e aumenta a linha em 1.
Agora ele começa a nova linha, e repete tudo até chegar em linha = 5.
'''