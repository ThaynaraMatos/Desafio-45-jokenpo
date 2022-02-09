n = int(input('\033[1;4;34mDigite um número para sabermos sua tabuada: ')) #Do jeito mais simples que criei kkk
tabuada = n*1, n*2, n*3, n*4, n*5, n*6, n*7, n*8, n*9, n*10
print(f'A tabuada de {n} é {tabuada}\033[m')

num = int(input('\033[1;4;35mDigite outro número para sabermos a sua tabuada: '))
print('-'*15)
print(f'A tabuada deste número é:\n{num} x 1 = {num*1}')
print(f'{num} x 2 = {num*2}\n{num} x 3 = {num*3}')
print(f'{num} x 4 = {num*4}\n{num} x 5 = {num*5}')
print(f'{num} x 6 = {num*6}\n{num} x 7 = {num*7}')
print(f'{num} x 8 = {num*8}\n{num} x 9 = {num*9}')
print(f'{num} x 10 = {num*10}')
print('-'*15)
print('É isso ae :D\033[m')
