import random
import emoji
from time import sleep
print(emoji.emojize('\033[1;31m EAE?! BORA JOGAR\033[m \033[1;31;107m JOKENPÔ?!!!\033[m \033[1;31mISTO É\033[m \033[1;37m\U0001f5ff\033[m \033[1;97m\U0001f4dc\033[m \033[1;34m\u2702\033[m \033[m\n\033[1;31m É MUITO FÁCIL! APENAS DIGITE PEDRA, PAPEL OU TESOURA. DE ACORDO COM SUA INTUIÇÃO :smiley: \033[m ',use_aliases=True))
pedra = 'PEDRA'.upper()
papel = 'PAPEL'.upper()
tesoura = 'TESOURA'.upper()
lista = [pedra,papel,tesoura]
escolha = random.choice(lista)
usuario = str(input('\033[1;35m VOCÊ COMEÇA:\033[m ')).upper().strip()
print('\033[1;31mJO\033[m')
sleep(1)
print('\033[1;31mKEN\033[m')
sleep(1)
print('\033[1;31mPÔ!!!\033[m')
if usuario == 'PEDRA' and escolha == 'TESOURA':
    print(f'{escolha}')
    print(emoji.emojize(f'\033[1;34mA pedra quebra a tesoura. Você GANHOU :sunglasses:\033[m',use_aliases=True))
elif usuario == 'PEDRA' and escolha == 'PEDRA':
    print(f'{escolha}')
    print(emoji.emojize('\033[1;33mEmpate :neutral_face:\033[m',use_aliases=True))
elif usuario == 'PEDRA' and escolha == 'PAPEL':
    print(f'{escolha}')
    print(emoji.emojize('\033[1;32mO papel embrulha a pedra. Eu VENCI :sunglasses:\033[m',use_aliases=True))
elif usuario == 'PAPEL' and escolha == 'PEDRA':
    print(f'{escolha}')
    print(emoji.emojize('\033[1;34mO papel embrulha a pedra. Você GANHOU :sunglasses:\033[m',use_aliases=True))
elif usuario == 'PAPEL' and escolha == 'TESOURA':
    print(f'{escolha}')
    print(emoji.emojize('\033[1;32mA tesoura corta o papel. Eu VENCI :sunglasses:\033[m',use_aliases=True))
elif usuario == 'PAPEL' and escolha == 'PAPEL':
    print(f'{escolha}')
    print(emoji.emojize('\033[1;33mEmpate :neutral_face:\033[m',use_aliases=True))
elif usuario == 'TESOURA' and escolha == 'PAPEL':
    print(f'{escolha}')
    print(emoji.emojize('\033[1;34mA tesoura corta o papel. Você GANHOU :sunglasses:\033[m',use_aliases=True))
elif usuario == 'TESOURA' and escolha == 'PEDRA':
    print(f'{escolha}')
    print(emoji.emojize('\033[1;32mA pedra quebra a tesoura. Eu VENCI :sunglasses:\033[m',use_aliases=True))
elif usuario == 'TESOURA' and escolha == 'TESOURA':
    print(f'{escolha}')
    print(emoji.emojize('\033[1;33mEmpate :neutral_face:\033[m',use_aliases=True))
else:
    print('\033[1;37mOpção inválida. Tente novamente.\033[m')




