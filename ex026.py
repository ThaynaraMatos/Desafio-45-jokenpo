import emoji
frase = str(input(emoji.emojize('\033[33mEscreva uma frase :smirk: :\033[m',use_aliases= True))).lower().strip()
frase = frase.replace(' ', '')
letras = frase.count("a")
if letras > 1:
    print(f'\033[4;34mA frase tem {letras} letras A e a primeira letra A aparece na posição {frase.find("a")+1} e a ultima letra A aparece na posição {frase.rfind("a")+1}! \033[m')
if letras == 1:
    print(f'\033[4;35mA frase tem {letras} letra A e a única letra A aparece na posição {frase.find("a")+1}!\033[m')
if letras == 0:
    print(f'\033[4;97mNão há nenhuma letra A na frase, então é igual a {letras}!\033[m ')







'''frase = str(input('Digite uma frase: ')).strip().upper()
letra = str(input('Digite uma letra: ')).upper()
if frase.count(letra) == 0:
    print ('Não há nenhuma letra {} na frase'.format(letra.upper()))
if frase.count(letra) == 1:
    print ('há uma 1 letra {} na frase'.format(letra.upper()))
if frase.count(letra) > 1:
    print ('há {} letras {} na frase'.format(frase.count(letra), letra.upper()))
print ('A letra {} aparece pela primeira vez no caractere {}'. format(letra.upper(), frase.find(letra)+1))
print ('a letra {} aparece pela última vez no caractere {}'.format(letra.upper(), (frase[::-1].find(letra)-len(frase))*-1))'''


'''frase = str(input('Digite uma frase.')).strip().upper()
x = 'A' in frase
if x == True:
    print('A letra A aparece na frase {} vezes.'.format(frase.count('A')))
    print('A letra A aparece pela primeira vez na posição {}.'.format(frase.find('A') + 1))
    print('A letra A aparece pela última vez na posição {}.'.format(frase.rfind('A') + 1))
else:
    print('A letra A não aparece nenhuma vez nessa frase.')'''









