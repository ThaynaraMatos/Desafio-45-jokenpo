'''import emoji
print(emoji.emojize('Olá, digite o seu salário que irei calcular quanto você receberá de aumento :smiley:', use_aliases=True))
salario = int(input('Digite aqui por favor: '))
aumento = (salario*10)/100
aumentao = (salario*15)/100
if salario > 1250:
    print(f'Já que seu salário é superior a 1250, você ganhará um aumento de 10%, portanto receberá {salario+aumento:.2f}! ')
else:
    if salario <= 1250:
        print(f'Já que seu salário é igual ou inferior a 1250, você ganhará um aumento de 15%, portanto receberá {salario+aumentao:.2f}! ')'''


salario = float(input('\033[1;97mQual é o salário do funcionário: R$\033[m'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print(f'Quem ganhava \033[4mR${salario:.2f}\033[m passa a ganhar \033[30;107mR${novo:.2f}\033[m agora.')



