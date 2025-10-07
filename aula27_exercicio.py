'''
Exercício
Peça para o usuário digitar o seu nome
Peça para o usuário digitar a sua idade
Se nome e idade forem digitados, exiba:
         Seu nome é {nome}
         Seu nome invertido é {nome invertido}
         Seu nome contém (ou não) espaços
         Seu nome tem {número de letras} letras
         A primeira letra do seu nome é {primeira letra}
         A última letra do seu nome é {última letra}
Se nada for digitado em nome ou idade, exiba:
         Desculpe, você deixou algum campo vazio.   
'''
nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')
if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}') # Invertendo a string
    if ' ' in nome: # Verificando se tem espaço no nome
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')
    print(f'Seu nome tem {len(nome)} letras') # Contando a quantidade de letras no nome
    print(f'A primeira letra do seu nome é {nome[0]}') # Pegando a primeira letra do nome
    print(f'A última letra do seu nome é {nome[-1]}') # Pegando a última letra do nome
else:
    print('Desculpe, você deixou algum campo vazio.')