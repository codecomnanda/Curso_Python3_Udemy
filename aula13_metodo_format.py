a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}' 
formato = string.format(nome1=a, nome2=b, nome3=c) # nome1, nome2 e nome3 são parâmetros, ou seja, variáveis que você cria

print(formato)