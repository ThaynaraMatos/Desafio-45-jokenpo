from time import sleep
import emoji
nome = input(emoji.emojize('\033[1;4;35mOlá, digite seu nome :smiley::\033[m',use_aliases=True))
print('\033[1;32mPROCESSANDO...\033[m')
sleep(2)
print(emoji.emojize(f'\033[1;34mQue nome lindo que você tem! É um prazer te conhecer,\033[m \033[1;33m{nome}\033[m \033[1;34m:smirk:!\033[m',use_aliases=True))
