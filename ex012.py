p = float(input('\033[1;4;36mDigite o preço do produto R$\033[m'))
novo = p - (p*5 /100)
print(f'\033[1;4;97mO produto que custava\033[m \033[42mR${p:.2f}\033[m, \033[1;4;97mna promoção com desconto de 5% vai custar \033[42mR${novo:.2f}\033[m')

