import emoji
nome = str(input(emoji.emojize('\033[1;36mEscreva seu nome completo :blush: :\033[m', use_aliases= True))).strip()
primeiro = nome.split()
print(f'Seu primeiro nome é \033[4;33m{primeiro[0]}\033[m e o seu último nome é \033[4;33m{primeiro[-1]}\033[m ')









