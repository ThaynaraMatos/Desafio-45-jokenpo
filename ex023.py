numero = int(input('\033[1;30;44mDigite um número de 0 a 9999:\033[m '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print(f'\033[1;30;43mA unidade do seu número é {unidade}\033[m \n \033[1;30;43mA dezena do seu número é {dezena}\033[m \n \033[1;30;43mA centena do seu número é {centena}\033[m \n \033[1;30;43mO milhar do seu número é {milhar}\033[m')



