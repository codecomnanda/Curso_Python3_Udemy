# if / elif      / else
# se / se não se / se não
entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar': # primeira condição a ser testada
    print('Você entrou no sistema') # o tab significa que esse print está dentro do bloco do if

elif entrada == 'sair': # segunda condição a ser testada
    print('Você saiu do sistema')

else: # se nenhuma das condições anteriores forem True, executa o else
    print('Você não digitou nem entrar e nem sair.')

print('...FIM...') # esse print não está dentro do bloco do if, pois não está tabulado