'''
CONSTANTE = "Varriáveis" que não mudam de valor
Muitas condições no mesmo if (ruim para a legibilidade)
    <- Contagem de complexidade (ruim para a legibilidade)

Simples é melhor que complexo
Complexo é melhor que complicado


velocidade = 61 # Velocidade atual do carro
local_carro = 100 # Local onde o carro está

RADAR_1 = 60 # Velocidade máxima do radar 1
LOCAL_1 = 100 # Local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

vel_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
local_carro <= (LOCAL_1 + RADAR_RANGE) # local_carro <= 101
carro_multado_radar_1 = vel_carro_passou_radar_1 and carro_passou_radar_1

if vel_carro_passou_radar_1:
    print('Velocidade do carro passou do radar 1')

if carro_passou_radar_1:
    print('Carro passou no radar 1')

if carro_multado_radar_1:
    print('Carro multado no radar 1')
'''

# PROGRAMA PRA SABER SE O ALUNO FOI APROVADO OU REPROVADO

'''
# Código “confuso” (funciona, mas é difícil de ler):

nota = 8
presenca = 80

if nota >= 7 and presenca > 75:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")

'''

# Código “claro” (mais fácil de ler e entender):

nota = 8
presenca = 80

NOTA_MINIMA = 7
PRESENCA_MINIMA = 75

atingiu_nota = nota >= NOTA_MINIMA
atingiu_presenca = presenca >= PRESENCA_MINIMA

if atingiu_nota and atingiu_presenca:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")
