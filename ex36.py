import emoji
from time import sleep
print(emoji.emojize('\033[4mOlá, seja bem vindo(a)!\nAqui irei aprovar se o Sr(a) poderá fazer um empréstimo bancário para a compra de sua casa :smiley:\033[m',use_aliases=True))
ValorDaCasa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o seu salário: R$'))
anos = int(input('Em quantos anos você irá pagar?'))
print('PROCESSANDO...')
sleep(2)
prestacao = ValorDaCasa / (anos * 12)
print(f'O valor da prestação mensal será de R${prestacao:.2f} ')
exceder = (salario*30/100)
if prestacao > exceder:
    print('\033[1;4mLamentamos, mas seu empréstimo foi\033[m \033[1;4;31mNEGADO!\033[m')
else:
    print('\033[1;4mSeu empréstimo foi aprovado com\033[m \033[1;4;32mSUCESSO!\033[m')

