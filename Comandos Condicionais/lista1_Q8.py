dica=int(input())

if dica % 2== 0:
    msg=(((dica/2)**(1/2) +2))
else:
    msg= (dica/3) + 3

filme_1=input()
filme_2=input()
filme_3=input()

if filme_1 == 'Coringa' or filme_1 == 'Batman vs Superman' or filme_1 == 'O Cavaleiro das Trevas':
    print ('Algo de errado não está certo!')
else:
    if len(filme_1) == msg:
      print('Miles: Achei o easter egg!!!')
      cansaco = 1
      nome_filme=input()
      duracao=int(input())
      
      if filme_1 == 'Vingadores: Ultimato':
        cansaco = 2
        
    if len(filme_1) != msg:
      print ('Miles: Tou frio, melhor ir procurar nas fases mais antigas')
      cansaco = 1
      
      if filme_1 == 'Vingadores: Ultimato':
        cansaco = 2
      
      
      if len(filme_2) == msg:
        print('Miles: Achei o easter egg!!!')
        cansaco = 2
        nome_filme=input()
        duracao=int(input())
        if filme_1 == 'Vingadores: Ultimato':
          cansaco = 3 
      
      if len(filme_2) != msg:
        print('Gwen: Cadê o velho??? Queria um autógrafo')
        cansaco = 2
        if filme_2 == 'Vingadores: Ultimato':
          cansaco = 3
        
        if len(filme_3) == msg:
          print('Miles: Achei o easter egg!!!')
          cansaco = 3
          nome_filme=input()
          duracao=int(input())
          if filme_3 == 'Vingadores: Ultimato':
            cansaco = 4
            
        if len(filme_3) != msg:
          print('Peter: Parece que o próximo filme do aranha-verso vai demorar mais do que esperado pra sair...')
          cansaco = 3
          if filme_3 == 'Vingadores: Ultimato':
            cansaco = 4
      
      
if len (filme_1)== msg or len(filme_2) == msg or len (filme_3) == msg:
  if cansaco >= 2 and duracao >=135:
    print('Miles: A mimir')
  if cansaco >= 2 and  120 <= duracao < 135:
    print('Gwen: Nada que uma xícara de café não resolva!')
  if cansaco < 2 or duracao < 120:
    print(f'Peter: {nome_filme} é o melhor filme do homem aranha, 10/10')
  
    
    