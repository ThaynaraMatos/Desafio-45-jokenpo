import emoji
from datetime import date
print(emoji.emojize('\033[1;97;46m Vamos saber a sua categoria na confederação nacional de natação \U0001f3ca \033[m',use_aliases=True))
nascimento = int(input('\033[1;34;107m Digite seu ano de nascimento ex:1989,1990:\033[m '))
ano = date.today().year
idade = ano - nascimento
if idade <= 9:
    print(f'\033[1;97;44m Como você tem {idade} anos, você se encaixa na categoria MIRIM! \033[m')
elif idade <= 14:
    print(f'\033[1;97;44m Como você tem {idade} anos, você se encaixa na categoria INFANTIL! \033[m')
elif idade <= 19:
    print(f'\033[1;97;44m Como você tem {idade} anos, você se encaixa na categoria JUNIOR! \033[m')
elif idade <= 25:
    print(f'\033[1;97;44m Como você tem {idade} anos, você se encaixa na categoria SÊNIOR! \033[m')
elif idade > 25:
    print(f'\033[1;97;44m Como você tem {idade} anos, você se encaixa na categoria MASTER! \033[m')
print(emoji.emojize('\033[1;97;44m Boa sorte! :smiley:\U0001f3ca \033[m',use_aliases=True))


