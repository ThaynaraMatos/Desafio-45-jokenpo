from time import sleep
num = int(input('\033[4mEscreva um número, que irei dizer se ele é par ou ímpar:\033[m '))
print('\033[1;32mPROCESSANDO...\033[m')
sleep(2)
resto = num % 2
if resto == 0:
    print('\033[1;32mSeu número é par.')
else:
    print('\033[1;31mSeu número é ímpar.')

