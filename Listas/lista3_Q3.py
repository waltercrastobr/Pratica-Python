continuar = True
cont = 0
soma_nota = 0
n = int(input())
while cont < n:
  continuar = True
  colecao = input().split(', ')
  notas = input().split(', ')
  cont += 1
  for item in colecao:
    if continuar == True:
      if item == 'colete preto' or item == 'coturno' or item or item == 'vestido com babados' or item == 'blusa bufante':
        if item == 'colete preto' or item == 'coturno':
          print(f'{item} é uma peça muito gótica, não faz o estilo da Glimmer.')
          continuar = False
        elif item == 'vestido com babados' or item == 'blusa bufante':
          print(f'{item} é uma peça muito antiquada, infelizmente essa coleção não vai servir...')
          continuar = False
  else:
    for c in notas:
      soma_nota += int(c)
    media = soma_nota / len(notas)
    if media < 6 and continuar == True:
      print('Até que as peças são bonitinhas, mas não o bastante. Essa coleção não vai servir.')
      continuar = False
    elif media >= 6 and continuar == True:
      print('Que coleção linda! Com certeza vai ajudar Glimmer a se inspirar.')
    soma_nota = 0
