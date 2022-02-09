'''from math import sqrt, pow
print('Vamos calcular o comprimento da hipotenusa do cateto oposto e o cateto adjacente do trangulo retangulo!')
oposto = float(input('Digite o comprimento do cateto oposto:'))
adjacente = float(input('Digite o comprimento do cateto adjacente:'))
hipotenusa = sqrt(pow(oposto, 2) + pow(adjacente, 2))
print(f'O valor da hipotenusa é {hipotenusa:.2f}')'''

from math import hypot
oposto = float(input('\033[4;32mDigite o comprimento do cateto oposto:\033[m'))
adjacente = float(input('\033[4;33mDigite o comprimento do cateto adjacente:\033[m'))
hipotenusa = hypot(oposto, adjacente)
print(f'\033[4;34mO valor da hipotenusa é {hipotenusa:.2f}\033[m')