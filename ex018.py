from math import radians, cos, tan, sin
angulo = float(input('\033[4;32mDigite o valor do ângulo que deseja:\033[m'))
cosseno = cos(radians(angulo))
print(f'\033[4;97mO angulo {angulo} tem o cosseno de {cosseno:.2f}\033[m')
seno = sin(radians(angulo))
print(f'\033[4;97mO angulo {angulo} tem o seno de {seno:.2f}\033[m')
tangente = tan(radians(angulo))
print(f'\033[4;97mO angulo {angulo} tem o tangente de {tangente:.2f}\033[m')

