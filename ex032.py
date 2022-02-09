from datetime import date
ano = int(input('\033[97;40mDigite qualquer ano, que eu irei dizer se ele é bisssexto ou não. Coloque 0 para analisar o ano atual: \033[m'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'\033[1;33mO ano {ano} é BISSEXTO')
else:
    print(f'\033[1;31mO ano {ano} não é BISSEXTO')


