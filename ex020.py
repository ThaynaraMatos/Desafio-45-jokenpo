from random import shuffle #random significa aleatório
a1 = str(input('\033[1;30;42mDigte o nome do primeiro aluno:\033[m '))
a2 = str(input('\033[1;30;43mDigite o nome do segundo aluno:\033[m '))
a3 = str(input('\033[1;30;44mDigite o nome do terceiro aluno:\033[m '))
a4 = str(input('\033[1;30;45mDigite o nome do quarto aluno:\033[m '))
alunos = [a1,a2,a3,a4]
shuffle(alunos) #suffle significa embaralhar
print(alunos)