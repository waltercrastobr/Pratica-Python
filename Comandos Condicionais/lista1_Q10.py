nomeAranha = input()
ataqueAranha = int(input())
defesaAranha = int(input())
nomeAliado = input()
ataqueAliado = int(input())
defesaAliado = int(input())

nomeVilao = input()
ataqueVilao = int(input())
defesaVilao = int(input())
nomeCapanga = input()
ataqueCapanga = int(input())
defesaCapanga = int(input())

s1 = int(input())
s2 = int(input())
s3 = int(input())

vitoriaAranha = 0
vitoriaVilao = 0

print('1° confronto:')
if s1 == 0:
    if ataqueAranha > defesaVilao:
        vitoriaAranha += 1
        print(f'O {nomeAranha} acertou vários golpes no {nomeVilao}')
    elif defesaVilao > ataqueAranha:
        vitoriaVilao += 1
        print(f'O {nomeVilao} está dificultando a vida do {nomeAranha}')
    elif ataqueAranha == defesaVilao:
        vitoriaAranha += 1
        print(f'O {nomeAranha} acertou vários golpes no {nomeVilao}')

elif s1 == 1:
    if (ataqueAranha + ataqueAliado) > defesaVilao:
        vitoriaAranha += 1
        print(f'O {nomeAranha} acertou vários golpes no {nomeVilao}')
    elif defesaVilao > (ataqueAranha + ataqueAliado):
        vitoriaVilao += 1
        print(f'O {nomeVilao} está dificultando a vida do {nomeAranha}')
    elif (ataqueAranha + ataqueAliado) == defesaVilao:
        vitoriaAranha += 1
        print(f'O {nomeAranha} acertou vários golpes no {nomeVilao}')

elif s1 == 2:
    if ataqueAranha > (defesaVilao + defesaCapanga):
        vitoriaAranha += 1
        print(f'O {nomeAranha} acertou vários golpes no {nomeVilao}')
    elif (defesaVilao + defesaCapanga) > ataqueAranha:
        vitoriaVilao += 1
        print(f'O {nomeVilao} está dificultando a vida do {nomeAranha}')
    elif ataqueAranha == (defesaVilao + defesaCapanga):
        vitoriaVilao += 1
        print(f'O {nomeVilao} está dificultando a vida do {nomeAranha}')

elif s1 == 3:
    if (ataqueAranha + ataqueAliado) > (defesaVilao + defesaCapanga):
        vitoriaAranha += 1
        print(f'O {nomeAranha} acertou vários golpes no {nomeVilao}')
    elif (defesaVilao + defesaCapanga) > (ataqueAranha + ataqueAliado):
        vitoriaVilao += 1
        print(f'O {nomeVilao} está dificultando a vida do {nomeAranha}')
    elif (ataqueAranha + ataqueAliado) == (defesaVilao + defesaCapanga):
        vitoriaAranha += 1
        print(f'O {nomeAranha} acertou vários golpes no {nomeVilao}')

print('2° confronto:')
if s2 == 0:
    if ataqueVilao > defesaAranha:
        vitoriaVilao += 1
        print(f'O {nomeAranha} não consegue se defender contra o {nomeVilao}')
    elif defesaAranha > ataqueVilao:
        vitoriaAranha += 1
        print(f'O {nomeAranha} contra-atacou o {nomeVilao}')
    elif ataqueVilao == defesaAranha:
        vitoriaAranha += 1
        print(f'O {nomeAranha} contra-atacou o {nomeVilao}')

elif s2 == 1:
    if (ataqueVilao + ataqueCapanga) > defesaAranha:
        vitoriaVilao += 1
        print(f'O {nomeAranha} não consegue se defender contra o {nomeVilao}')
    elif defesaAranha > (ataqueVilao + ataqueCapanga):
        vitoriaAranha += 1
        print(f'O {nomeAranha} contra-atacou o {nomeVilao}')
    elif (ataqueVilao + ataqueCapanga) == defesaAranha:
        vitoriaVilao += 1
        print(f'O {nomeAranha} não consegue se defender contra o {nomeVilao}')

elif s2 == 2:
    if ataqueVilao > (defesaAranha + defesaAliado):
        vitoriaVilao += 1
        print(f'O {nomeAranha} não consegue se defender contra o {nomeVilao}')
    elif (defesaAranha + defesaAliado) > ataqueVilao:
        vitoriaAranha += 1
        print(f'O {nomeAranha} contra-atacou o {nomeVilao}')
    elif ataqueVilao == (defesaAranha + defesaAliado):
        vitoriaAranha += 1
        print(f'O {nomeAranha} contra-atacou o {nomeVilao}')

elif s2 == 3:
    if (ataqueVilao + ataqueCapanga) > (defesaAranha + defesaAliado):
        vitoriaVilao += 1
        print(f'O {nomeAranha} não consegue se defender contra o {nomeVilao}')
    elif (defesaAranha + defesaAliado) > (ataqueVilao + ataqueCapanga):
        vitoriaAranha += 1
        print(f'O {nomeAranha} contra-atacou o {nomeVilao}')
    elif (ataqueVilao + ataqueCapanga) == (defesaAranha + defesaAliado):
        vitoriaAranha += 1
        print(f'O {nomeAranha} contra-atacou o {nomeVilao}')

print('3° confronto:')
if s3 == 0:
    if ataqueAranha > defesaVilao:
        vitoriaAranha += 1
        print(f'O {nomeAranha} acertou vários golpes no {nomeVilao}')
    elif defesaVilao > ataqueAranha:
        vitoriaVilao += 1
        print(f'O {nomeVilao} está dificultando a vida do {nomeAranha}')
    elif ataqueAranha == defesaVilao:
        vitoriaAranha += 1
        print(f'O {nomeAranha} acertou vários golpes no {nomeVilao}')

elif s3 == 1:
    if (ataqueAranha + ataqueAliado) > defesaVilao:
        vitoriaAranha += 1
        print(f'O {nomeAranha} acertou vários golpes no {nomeVilao}')
    elif defesaVilao > (ataqueAranha + ataqueAliado):
        vitoriaVilao += 1
        print(f'O {nomeVilao} está dificultando a vida do {nomeAranha}')
    elif (ataqueAranha + ataqueAliado) == defesaVilao:
        vitoriaAranha += 1
        print(f'O {nomeAranha} acertou vários golpes no {nomeVilao}')

elif s3 == 2:
    if ataqueAranha > (defesaVilao + defesaCapanga):
        vitoriaAranha += 1
        print(f'O {nomeAranha} acertou vários golpes no {nomeVilao}')
    elif (defesaVilao + defesaCapanga) > ataqueAranha:
        vitoriaVilao += 1
        print(f'O {nomeVilao} está dificultando a vida do {nomeAranha}')
    elif ataqueAranha == (defesaVilao + defesaCapanga):
        vitoriaVilao += 1
        print(f'O {nomeVilao} está dificultando a vida do {nomeAranha}')

elif s3 == 3:
    if (ataqueAranha + ataqueAliado) > (defesaVilao + defesaCapanga):
        vitoriaAranha += 1
        print(f'O {nomeAranha} acertou vários golpes no {nomeVilao}')
    elif (defesaVilao + defesaCapanga) > (ataqueAranha + ataqueAliado):
        vitoriaVilao += 1
        print(f'O {nomeVilao} está dificultando a vida do {nomeAranha}')
    elif (ataqueAranha + ataqueAliado) == (defesaVilao + defesaCapanga):
        vitoriaAranha += 1
        print(f'O {nomeAranha} acertou vários golpes no {nomeVilao}')

if vitoriaAranha > vitoriaVilao:
    print(f'O {nomeAranha} e {nomeAliado} conseguiram derrotar o {nomeVilao} e recuperar o multiverso!')
elif vitoriaVilao > vitoriaAranha:
    print(f'O {nomeVilao} e {nomeCapanga} invadiram Nova York, onde estão os outros aranhas??')
    