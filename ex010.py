r = float(input('\033[1;4;32mQuanto você tem na sua carteira em R$\033[m'))
print(f'\033[1;4;33mCom o valor de\033[m \033[1;30;43m{r:.2f}\033[m \033[1;4;33mvocê poderá comprar\033[m \033[1;30;43m{r/5.46:.2f}\033[m \033[1;33mU$\033[m')
print(f'\033[1;4;33mE com esse valor de\033[m \033[1;30;43m{r:.2f}\033[m \033[1;4;33mvocê poderá comprar em euros\033[m \033[1;30;43m{r/6.38:.2f}\033[m \033[1;33m€\033[m')