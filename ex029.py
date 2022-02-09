import emoji
print('\033[1;97;41mO LIMITE DE VELOCIDADE É 80KM/H\033[m')
velocidade = float(input('\033[4mEscreva a velocidade que você está dirigindo por favor:\033[m'))
if velocidade > 80:
    print(f'\033[1;30;43mVocê excedeu o limite de velocidade que é de 80km/h\033[m')
    multa = (velocidade - 80) * 7
    print(f'\033[1;30;43mVocê deve pagar uma multa de R${multa:.2f}\033[m ')
print(emoji.emojize('\033[1;32mTenha um bom dia! Dirija com \033[1;31;107msegurança\033[m!:red_car:\033[m',use_aliases=True))





