print('Por favor digite 3 números diferentes que eu irei dizer qual é o maior e o menor:')
num1 = int(input('Digite o primeiro número:'))
num2 = int(input('Digite o segundo número:'))
num3 = int(input('Digite o terceiro número:'))
numeros = [num1,num2,num3]
sortear = sorted(numeros)
print(f'O maior número é {sortear[2]} e o menor número é o {sortear[0]}')

'''print('Por favor digite 3 números diferentes que eu irei dizer qual é o maior e o menor:')
num1 = int(input('\033[34mDigite o primeiro número:'))
num2 = int(input('\033[34mDigite o segundo número:'))
num3 = int(input('\033[mDigite o terceiro número:'))
#verificando quem é menor
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
#verificando quem é o maior
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
print(f'O menor valor digitado é {menor}')
print(f'O maior digitado é {maior}')'''
