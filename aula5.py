# conversão de tipos, coerção de tipos (casting)
# type convertion, typecasting, coercion
# É o ato de converter um tipo de dado em outro
# Tipos imutáveis e primitivos: str, int, float, bool
print(1 + 1)  # int + int = int
print('a' + 'b')  # str + str = str. Ele concatena, ou seja, junta as duas strings

print(int('1'), type(int('1')))  # Faz a conversão (coerção) de str para int
print(float('1') + 1)  # Faz a conversão (coerção) de str para float e depois faz a soma 
print(bool(''))  # É considerada False
print(bool(' '))  # É considerada True
print(str(11) + 'b')  # Converte o int 11 para str e depois concatena com 'b'