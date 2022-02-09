salário = float(input('\033[1;32mDigite seu salário R$\033[m'))
novo = salário + (salário*15/100)
print(f'\033[1;32;107mO Seu antigo salário de {salário:.2f} com 15% de aumento ficará {novo:.2f}\033[m')


preço = float(input('\033[1;35mDigite o preço de um produto R$\033[m'))
novoo = preço - preço*10/100
print(f'\033[1;4;35mO preço de {preço:.2f} com 10% de desconto a vista, ficará por {novoo:.2f}\033[m')
print('\033[1;4;35mCaso você quiser pagar parcelado, você terá 8% de aumento, que então ficará:\033[m ' ,end='')
aumentado = preço + preço*8/100
print(f'\033[1;4;35m{aumentado:.2f}\033[m')


