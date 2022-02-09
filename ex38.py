num1 = int(input('\033[1;34mDigite um número:\033[m '))
num2 = int(input('\033[1;36mDigite outro número:\033[m '))
if num1 > num2:
    print('\033[1;32mO PRIMEIRO valor é maior!\033[m')
elif num2 > num1:
    print('\033[1;32mO SEGUNDO valor é maior!\033[m')
else:
    print('\033[1;97mNão existe valor maior, os dois são IGUAIS.\033[m')

