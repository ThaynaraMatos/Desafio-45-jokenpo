largura = float(input('\033[1;4;97mDigite a largura em metros da sua parede:\033[m'))
altura = float(input('\033[1;4;97mDigite a altura em metros sua da parede:\033[m'))
a = largura*altura
tinta = a/2
print(f'\033[1;4;32mVocê tem a área de\033[m \033[1;32;107m{a}m²\033[m \033[1;4;32me precisa de\033[m \033[1;32;107m{tinta}\033[m \033[1;4;32mlitros de tinta para pinta-la.\033[m')
