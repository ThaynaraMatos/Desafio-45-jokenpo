import emoji
from datetime import date
print(emoji.emojize('\033[1;32;40m Olá, caro(a) jovem! Irei dizer como está a sua situação em relação ao alistamento OBIGATÓRIO no exército :thumbsup: \033[m',use_aliases=True))
nascimento = int(input('\033[1;32;40m Por favor, digite o ano de seu nascimento, por ex:1989,1990..:\033[m '))
sexo = int(input('\033[1;31;40m Digite:\033[m \n\033[1;31;40m [1] Masculino \033[m  \n\033[1;31;40m [2] Feminino  \033[m \n\033[1;31;40m Sua resposta: \033[m '))
if sexo == 1:
    print('\033[1;32;40m Seu alistamento militar é OBRIGATÓRIO. Vamos começar o teste! \033[m')
elif sexo == 2:
    print('\033[1;32;40m Seu alistamento não é obrigatório. \033[m')
    alistar = str(input('\033[1;33;40m (Digite SIM ou NÃO) Deseja se alistar? \033[m')).upper().strip()
    if alistar == 'NÃO':
       print('\033[1;31;40m Fim do programa! \033[m')
    elif alistar == 'NAO':
     print('\033[1;31;40m Fim do programa. \033[m')
    else:
        print('\033[1;36;40m Seja bem-vinda ao alistamento no exército, minha jovem! \033[m')
ano = date.today().year
idade = ano - nascimento
print(f'\033[1;30;42m Sua idade é {idade}! \033[m ')
if idade < 18:
    saldo = 18 - idade
    print(f'\033[1;32;40m Você é de menor! Portanto terá que se alistar, faltam {saldo} anos para seu alistamento, caro(a) jovem! \033[m')
    tempo = ano + saldo
    print(f'\033[1;32;40m Seu alistamento será em {tempo}! \033[m')
elif idade == 18:
    print('\033[1;32;40m SOLDADO PROMOVIDO! Já está na hora de se alistar, caro(a) jovem! \033[m')
elif idade > 18:
    saldao = idade - 18
    print(f'\033[1;32;40m Já passou do tempo de seu alistamento! Foi há {saldao} anos, caro(a) jovem! \033[m')
    tempao = ano - saldao
    print(f'\033[1;32;40m Seu alistamento foi em {tempao}! \033[m')







