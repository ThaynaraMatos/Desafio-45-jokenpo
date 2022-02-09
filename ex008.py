medida = float(input('\033[1;30;107mEscreva uma distancia em metros:\033[m'))
km = medida / 1000
hm = medida / 100  # hectometro equivale a 100 metros
dam = medida / 10  # dividir o metro em partes iguais
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print(f'\033[1;30;107mA medida em quilometros é {km}\033[m \n \033[1;30;107mMedida em hectometro é {hm}\033[m \n \033[1;30;107mMedida em decametros é {dam}\033[m \n \033[1;30;107mMedida em decimetros é {dm}\033[m \n \033[1;30;107mMedida de centimetros é {cm:.0f}\033[m \n \033[1;30;107mE a medida em milimetros é {mm:.0f}\033[m ')
