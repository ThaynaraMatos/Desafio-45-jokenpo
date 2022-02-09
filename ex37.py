num = int(input('\033[1;33mDigite um número inteiro qualquer: \033[m'))
escolha = input('\033[1;35mAgora escolha uma das base de conversão!\033[m \nDigite \033[1;31m[1]\033[m para \033[1;31mBinário\033[m, \033[1;32m[2]\033[m para \033[1;32mOctal\033[m e \033[1;33m[3]\033[m para \033[1;33mHexadecimal\033[m: ')
if escolha == '1':
    print(f'\033[1;31mO número {num} convertido em binário é {bin(num)[2:]}!\033[m')
elif escolha == '2':
    print(f'\033[1;32mO número {num} convertido em octal é {oct(num)[2:]}!\033[m')
elif escolha == '3':
    print(f'\033[1;33mO número {num} convertido em hexadecimal é {hex(num)[2:]}!\033[m')
else:
    print('\033[1;37mOpção inválida. Tente novamente.\033[m')




