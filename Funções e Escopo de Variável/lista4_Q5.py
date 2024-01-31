vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'y', 'w', 'z',
              'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Y', 'W', 'Z']
numeros = []


def pos_x(eixo_x):
    cont_vogais = 0
    cont_consoantes = 0
    for elem in eixo_x:
        if elem in vogais:
            cont_vogais += 1
        elif elem in consoantes:
            cont_consoantes += 1

    if cont_consoantes == 0:
        return 0
    else:
        variavel_x = (cont_vogais // cont_consoantes)
        return variavel_x % 7


def pos_y(eixo_y):
    cont_vogais = 0
    cont_consoantes = 0
    for elem in eixo_y:
        if elem in vogais:
            cont_vogais += 1
        elif elem in consoantes:
            cont_consoantes += 1

    if cont_consoantes == 0:
        return 0
    else:
        variavel_y = (cont_vogais // cont_consoantes)
        return variavel_y % 7



def multiplos_sequencia_x(eixo_x):
    numeros = [int(elem) for elem in eixo_x if elem.isdigit()]
    if len(numeros) == 0:
        return pos_x(eixo_x)
    else:
        primeiro_num = numeros[0]
        cont_num = 0
        for num in numeros:
            if int(num) % primeiro_num == 0:
                cont_num += 1
        if cont_num == len(numeros):
            return 3
        else:
            return pos_x(eixo_x)


def multiplos_sequencia_y(eixo_y):
    numeros = [int(elem) for elem in eixo_y if elem.isdigit()]
    if len(numeros) == 0:
        return pos_y(eixo_y)
    else:
        primeiro_num = numeros[0]
        cont_num = 0
        for num in numeros:
            if int(num) % primeiro_num == 0:
                cont_num += 1
        if cont_num == len(numeros):
            return 3
        else:
            return pos_y(eixo_y)


eixo_x = input()
multiplos_sequencia_x(eixo_x)

eixo_y = input()
multiplos_sequencia_y(eixo_y)


matriz = [['.' for c in range(7)] for c in range(7)]
linha = int(multiplos_sequencia_x(eixo_x))
coluna = int(multiplos_sequencia_y(eixo_y))
elem = '☆'
matriz[linha][coluna] = elem
for x in matriz:
    print(" ".join(x))

if (linha == 3) and (coluna == 3):
  print('Ótimo, a estrela vai ficar exatamente no meio da fotografia! Posição melhor não existe!')
  print('Obrigado pela ajuda! A foto ficou ótima!')
elif (linha == 0) or (linha == 6) or (coluna == 0) or (coluna == 6):
  print('Ihhh, vou ter que relocalizar a câmera, uma fotografia com a estrela na borda não dá! Infelizmente demora um pouco para criar outro código...')
  print('Mesmo que eu não tenha conseguido uma matriz boa para tirar a foto, obrigado pelo seu tempo.')
else:
  print('Ok, agora é só enviar a matriz!')
  print('Obrigado pela ajuda! A foto ficou ótima!')

    
  
  