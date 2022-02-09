nome = str(input('\033[4;97mOlá, escreva seu nome completo por favor:\033[m')).strip()
print(f'\033[4;31mSeu nome com todas as letras maiúsculas:\033[m', nome.upper())
print(f'\033[4;32mSeu nome com todas as letras minúsculas:\033[m', nome.lower())
print(f'\033[4;33mSeu nome tem ao todo: {len(nome) -nome.count(" ")} letras.\033[m')
#print(f'Seu primeiro nome tem: {nome.find(" ")} letras.')
separa = nome.split()
print(f'\033[4;34mSeu primeiro nome é {separa[0]} e tem {len(separa[0])} letras\033[m')


