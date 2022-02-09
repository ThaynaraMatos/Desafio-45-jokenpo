print('\033[34mEscreva o comprimento de 3 retas que irei dizer se ele forma um triângulo ou não!')
r1 = float(input('\033[34mDigite um comprimento: '))
r2 = float(input('\033[34mDigite um comprimento: '))
r3 = float(input('\033[34mDigite um comprimento: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('\033[4;32mAs retas acima PODEM FORMAR um triângulo\033[m', end='')
    if r1 == r2 == r3:
        print(' EQUILÁTERO! ')
    elif r1 != r2 != r3 != r1:
        print(' ESCALENO! ')
    else:
        print(' ISÓSCELES! ')
else:
    print('\033[4;31mAs retas acima NÃO PODEM formar um triângulo!\033[m')

