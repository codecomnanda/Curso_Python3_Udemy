'''# Contagem simples com while: Faça um programa que mostre os números de 1 a 5

num = 1
while num <= 5:
    print(num)
    num += 1 '''

'''# Contagem regressiva com while: Faça um programa que mostre os números de 5 a 1

num = 5
while num >=1:
    print(num)
    num -= 1'''

# Somando números com while: Faça um programa que some os números. Peça números ao usuário até ele digitar 0.

numero = int(input("Digite um número (0 para sair): "))
soma = 0

while numero != 0:
    soma += numero
    numero = int(input("Digite outro número (0 para sair): "))

print(f"A soma dos números é {soma}")





