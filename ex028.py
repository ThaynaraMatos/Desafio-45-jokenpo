from random import randint
import emoji
from time import sleep
num = randint(0,5)
print('-=-' * 20)
print(emoji.emojize('\033[30;47mEae, belê? É o seguinte, to pensando em um número entre 0 e 5, dúvido você adivinhar qual é :relieved:\033[m', use_aliases=True))
print('-=-' * 20)
tentativa = int(input('Digite um número então: '))
print('PROCESSANDO...')
sleep(2)
if tentativa == num:
    print(f'\033[1;33mACERTOOU MIZERAVI! O número realmente era {num}\033[m! ')
else:
    print(f'\033[1;31mERROOOU, o número certo era {num}!\033[m')

