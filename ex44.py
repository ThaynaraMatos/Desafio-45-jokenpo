import emoji
from time import sleep
print(' \033[1;33m====\033[m\033[1;36mLOJAS\033[m\033[1;33m==\033[m\033[1;36mNASCIMENTO\033[m\033[1;33m====\033[m')
preco = float(input('\033[1;32m Olá, digite o preço do produto R$\033[m '))
print('\033[1;30;107m FORMAS DE PAGAMENTOS:\033[m \n \033[1;30;47m [1] À VISTA NO DINHEIRO/CHEQUE \033[m \n \033[1;30;47m [2] À VISTA NO CARTÃO \033[m\n \033[1;30;47m [3] 2X NO CARTÃO \033[m\n \033[1;30;47m [4] 3X OU MAIS NO CARTÃO \033[m')
escolha = int(input('\033[1;31mDigite o meio de pagamento aqui:\033[m '))
print('\033[1;4;32mPROCESSANDO...\033[m')
sleep(2)
if escolha == 1:
    dinheiro = (preco * 10 / 100)
    desconto = preco - dinheiro
    print(f'\033[1;34m À vista no dinheiro/cheque (10% de desconto), você pagará R${desconto:.2f}! \033[m')
elif escolha == 2:
    cartao = (preco * 5 / 100)
    descontinho = preco - cartao
    print(f'\033[1;34m À vista no cartão (5% de desconto) você pagará R${descontinho:.2f}! \033[m')
elif escolha == 3:
    normal = preco
    print(f'\033[1;34m Em até 2x no cartão (preço normal), você pagará 2 parcelas de R${normal/2:.2f}! \033[m')
elif escolha == 4:
    parcelas = int(input('\033[1;36m Em quantas parcelas: \033[m'))
    if parcelas <= 2:
        print('\033[1;37m Opção inválida. Tente novamente.\033[m')
    else:
     aumento = (preco * 20 / 100)
     juros = preco + aumento
     parcelinhas = juros / parcelas
     print(f'\033[1;34m Em até 3x ou mais (20% de juros), você pagará o valor total de R${juros:.2f}! \n Em {parcelas} parcelas de R${parcelinhas:.2f}! \033[m')
elif escolha == 0 or escolha > 4:
    print('\033[1;37mOpção inválida. Tente novamente.\033[m')































