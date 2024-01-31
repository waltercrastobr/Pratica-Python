time1 = input()
time2 = input()

vitoria_time1 = 0
vitoria_time2 = 0
cont = 0

while vitoria_time1 < 3 and vitoria_time2 < 3:
  pontuacao_do_time1 = int(input())
  pontuacao_do_time2 = int(input())
  cont += 1
  if pontuacao_do_time1 > pontuacao_do_time2:
    vitoria_time1 += 1
    print(f'O vencedor da {cont}ª rodada foi: {time1}')
    if vitoria_time1 >= 3:
      print(f'O time {time1} ganhou a partida final!')
  elif pontuacao_do_time2 > pontuacao_do_time1:
    vitoria_time2 += 1
    print(f'O vencedor da {cont}ª rodada foi: {time2}')
    if vitoria_time2 >= 3:
      print(f'O time {time2} ganhou a partida final!')
      
 

  