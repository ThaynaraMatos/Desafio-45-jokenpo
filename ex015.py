dias = int(input('\033[1;30;47mQuantidade de dias o carro será alugado:\033[m'))
quilometro = float(input('\033[1;30;43mEscreva a quantidade de Km que será percorridos:\033[m'))
pago = (dias * 60) + (quilometro * 0.15)
print(f'\033[1;30;47mO total a pagar é de R${pago:.2f}\033[m')
