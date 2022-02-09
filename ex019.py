import emoji, random #random significa aleatório
print(emoji.emojize("\033[1;4;35mOlá professor(a) :smiley: abaixo digite o nome dos seus quatros alunos e sortearemos quem apagará o quadro!\033[m", use_aliases=True))
a1 = str(input('\033[1;4;33mDigite o nome do 1ºaluno:\033[m'))
a2 = str(input('\033[1;4;33mDigite o nome do 2ºaluno:\033[m'))
a3 = str(input('\033[1;4;33mDigite o nome do 3º aluno:\033[m'))
a4 = str(input('\033[1;4;33mDigite o nome do 4º aluno:\033[m'))
lista = [a1,a2,a3,a4]
sorteio = random.choice(lista) #choice significa escolha
print(f'\033[1;30;42mO ganhador(a) do sorteio foi {sorteio}, Parabéns!\033[m')



