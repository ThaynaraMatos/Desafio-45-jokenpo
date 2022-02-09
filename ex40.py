import emoji
print(emoji.emojize('\033[1;31;46m Olá, irei calcular a média de seu aluno(a) :nerd_face::pencil2:\033[m',use_aliases=True))
nota1 = float(input('\033[1;36;41m Digite a primeira nota de seu aluno(a):\033[m '))
nota2 = float(input('\033[1;36;41m Digite a segunda nota de seu aluno(a):\033[m '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print(f'\033[1;31;44m A média foi {media}! Portanto, seu aluno(a) foi REPROVADO!\033[m')
elif media >= 5.0 and media < 7.0: #Você tambem pode fazer desse jeito if 7 > média >= 5:
    print(f'\033[1;31;44m A média foi {media}! Portanto, seu aluno(a) está de RECUPERAÇÃO!\033[m')
if media >= 7.0:
    print(f'\033[1;31;44m A média foi {media}! Portanto, seu aluno foi APROVADO!\033[m')
print(emoji.emojize('\033[1;97;45m Tenha um bom dia :smiley: \033[m',use_aliases=True ))

