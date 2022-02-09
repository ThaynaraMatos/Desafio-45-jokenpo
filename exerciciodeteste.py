print('Por favor digite 4 números, que irei dizer qual é o maior e o menor!')
numero1 = int(input('Digite um número:'))
numero2 = int(input('Digite um número:'))
numero3 = int(input('Digite um número:'))
numero4 = int(input('Digite um número:'))
numeros = [numero1,numero2,numero3,numero4]
adivinhar = sorted(numeros)
print(f'O maior número é {adivinhar[3]} e o menor número é {adivinhar[0]}')
