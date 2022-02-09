from time import sleep
print('\033[1;4;35mVamos saber o antecessor e o sucessor do seu numero!\033[m')
n = int(input('\033[1;4;34mDigite um número:\033[m ' ))
print('\033[1;4;32mPROCESSANDO..\033[m')
sleep(1)
print(f'\033[1;4;36mO antecessor de {n} é {n-1} e o sucessor é {n+1}\033[m')

