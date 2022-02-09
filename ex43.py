import emoji
print(emoji.emojize('\033[1;30;43m Seja bem-vindo(a), vamos calcular seu IMC \U0001f3cb \033[m',use_aliases=True))
peso = float(input('\033[1;30;42m Digite seu peso (kg):\033[m'))
altura = float(input('\033[1;30;44m Digite sua altura (metro e cm):\033[m'))
imc = peso / (altura ** 2)
print(f'\033[1;30;45m Seu IMC é {imc:.1f} \033[m')
if imc < 18.5:
    print('\033[1;30;41m ABAIXO DO PESO. \033[m')
elif imc >= 18.5 and imc <= 25:
    print('\033[1;30;43m PESO IDEAL. \033[m')
elif imc > 25 and imc <= 30:
    print('\033[1;30;47m SOBREPESO. \033[m')
elif imc > 30 and imc <= 40:
    print('\033[1;30;41m OBESIDADE \033[m')
elif imc > 40:
    print('\033[1;30;41m OBESIDADE MÓRBIDA.\033[m')


