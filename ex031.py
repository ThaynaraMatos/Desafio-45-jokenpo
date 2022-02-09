'''distancia = float(input('Eai usuário, qual vai ser a distância da sua viajem em km?'))
if distancia <= 200:
   print(f'Sua viagem custará {distancia*0.50:.2f} ')
else:
   print(f'Sua viagem custará {distancia*0.45:.2f} ')'''


print('Agora vamos tentar daquele jeitinho simplificado!')
distancinha = float(input('\033[4;33mEai usuário, qual vai ser a distância da sua viajem em km?\033[m'))
print(f'Você está prestes a começar uma viajem de {distancinha}Km!')
preço = distancinha * 0.50 if distancinha <= 200 else distancinha * 0.45
print(f'\033[1;32mE o preço da sua passagem será de R${preço:.2f} ')




