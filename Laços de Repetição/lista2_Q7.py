qnt_partidas = int(input())

partida_atual = 1
rodada_atual = 0


vitoria_rodada_jogador = 0
vitoria_rodada_adversario = 0

vitoria_partida_jogador = 0
vitoria_partida_adversario = 0

while(partida_atual< qnt_partidas):
  qnt_rodadas = int(input())
  rodada_atual = 0
  vitoria_rodada_jogador = 0
  vitoria_rodada_adversario = 0
  print(f'Vai começar a {partida_atual}º partida. Esse jogo terá {qnt_rodadas} rodada(s).')
  while(rodada_atual < qnt_rodadas):
    rodada_atual += 1
    habilidade_jogador = int(input())
    habilidade_adversario = int(input())
    if habilidade_adversario > habilidade_jogador:
      vitoria_rodada_adversario += 1
    else:
      vitoria_rodada_jogador += 1
  else:
    print(f'Fim de jogo! O placar foi {vitoria_rodada_jogador}x{vitoria_rodada_adversario}')
    if vitoria_rodada_jogador == vitoria_rodada_adversario:
      print('Não foi dessa vez! Treinar pro ano que vem!')
      partida_atual = qnt_partidas
    if vitoria_rodada_adversario > vitoria_rodada_jogador:
      print('Não foi dessa vez! Treinar pro ano que vem!')
      partida_atual = qnt_partidas
    if vitoria_rodada_jogador - vitoria_rodada_adversario >= 5:
      print('QUE GOLEADAAAA!!! Essa vitória fez os outros times desistirem e a equipe de IP/P1 é a campeã!')
      partida_atual = qnt_partidas
    if vitoria_rodada_jogador > vitoria_rodada_adversario and not (vitoria_rodada_jogador - vitoria_rodada_adversario >= 5):
      print('Vamos para próxima fase!')
      partida_atual += 1

else:
   if not (vitoria_rodada_jogador == vitoria_rodada_adversario) and not (vitoria_rodada_jogador - vitoria_rodada_adversario >= 5) and (vitoria_rodada_jogador > vitoria_rodada_adversario):
     rodada_atual_final = 0
     rodadas_final = int(input())
     vitoria_jogador_final = 0
     vitoria_adversario_final = 0
     print(f'Tá na hora da grande final! Esse jogo terá {rodadas_final} rodada(s).')
     while rodada_atual_final < rodadas_final:
       habilidade_jogador = int(input())
       habilidade_adversario = int(input())
       if habilidade_adversario > habilidade_jogador:
         vitoria_adversario_final += 1
       else:
         vitoria_jogador_final += 1
       rodada_atual_final += 1 
      

     else:
       print(f'Fim de jogo! O placar foi {vitoria_jogador_final}x{vitoria_adversario_final}')
       if vitoria_adversario_final >= vitoria_jogador_final:
         print('Ah não!! Chegaram tão longe mas não foi dessa vez. :(')
       else:
         print('É CAMPEÃO! O TIME DE IP/P1 GARANTIU A TAÇA!')