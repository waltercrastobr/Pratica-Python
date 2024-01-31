n1 = ''
n2 = ''
n3 = ''
n4 = ''
n5 = ''

l1 = ''
l2 = ''
l3 = ''
l4 = ''
l5 = ''

elo1 = ''
elo2 = ''
elo3 = ''
elo4 = ''
elo5 = ''

Top = ''
Jungler = ''
Mid = ''
Adc = ''
Suporte = ''

qnt_jogadores = 0
pontuacao_time = 0

while qnt_jogadores < 5:
  nome = input()
  if nome == 'Bruna':
    print('LOL NÃO!!! TUDO MENOS LOL!!!')
    qnt_jogadores = 6
  else:
    lane = input()
    elo = input()
    if elo != 'Bronze' and elo != 'Prata' and elo != 'Ouro' and elo != 'Platina' and elo != 'Diamante' and elo != 'Desafiante' and elo != '':
      print('Não conheço esse elo, então vou considerar que é um elo ruim.')
    if lane == Top or lane == Mid or lane == Jungler or lane == Adc or lane == Suporte:
      print(f'{nome} não foi aceito, que pena.')
    elif lane != Top or lane != Mid or lane != Jungler or lane != Adc or lane != Suporte:
      print(f'{nome} entrou pro time.')
      if nome == 'Artur':
        print('Ele tá meio enferrujado...')
        pontuacao_time -= 18
      if nome == 'Frej':
        print('Joga muito!')
        pontuacao_time += 18
      qnt_jogadores += 1
      if lane == 'Top':
        Top = lane
      elif lane == 'Jungler':
        Jungler = lane
      elif lane == 'Mid':
        Mid = lane
      elif lane == 'Adc':
        Adc = lane
      elif lane == 'Suporte':
        Suporte = lane

      if n1 == '':
        n1 = nome
      elif n1 != '' and n2 == '':
        n2 = nome
      elif n1 != '' and n2 != '' and n3 == '':
        n3 = nome
      elif n1 != '' and n2 != '' and n3 != '' and n4 == '':
        n4 = nome
      elif n1 != '' and n2 != '' and n3 != '' and n4 != '' and n5 == '':
        n5 = nome
      
      
      if l1 == '':
        l1 = lane
      elif l1 != '' and l2 == '':
        l2 = lane
      elif l1 != '' and l2 != '' and l3 == '':
        l3 = lane
      elif l1 != '' and l2 != '' and l3 != '' and l4 == '':
        l4 = lane
      elif l1 != '' and l2 != '' and l3 != '' and l4 != '' and l5 == '':
        l5 = lane
      
      
      if elo1 == '':
        elo1 = elo
        if elo1 != 'Bronze' or elo1 != 'Prata' or elo1 != 'Ouro'or elo1 != 'Platina' or elo1 != 'Diamante' or elo1 != 'Desafiante':
          pontuacao_time += 0
        if elo1 == 'Bronze':
          pontuacao_time += 1
        if elo1 == 'Prata':
          pontuacao_time += 2
        if elo1 == 'Ouro':
          pontuacao_time += 4
        if elo1 == 'Platina':
          pontuacao_time += 6
        if elo1 == 'Diamante':
          pontuacao_time += 8
        if elo1 == 'Desafiante':
          pontuacao_time += 10
            
      elif elo1 != '' and elo2 == '':
        elo2 = elo
        if elo2 != 'Bronze' or elo2 != 'Prata'or elo2 != 'Ouro'or elo2 != 'Platina'or elo2 != 'Diamante'or elo2 != 'Desafiante':
          pontuacao_time += 0
        if elo2 == 'Bronze':
          pontuacao_time += 1
        if elo2 == 'Prata':
          pontuacao_time += 2
        if elo2 == 'Ouro':
          pontuacao_time += 4
        if elo2 == 'Platina':
          pontuacao_time += 6
        if elo2 == 'Diamante':
          pontuacao_time += 8
        elif elo2 == 'Desafiante':
          pontuacao_time += 10
            
                  
      elif elo1 != '' and elo2 != '' and elo3 == '':
        elo3 = elo
        if elo3 != 'Bronze' or elo3 != 'Prata'or elo3 != 'Ouro'or elo3 != 'Platina'or elo3 != 'Diamante'or elo3 != 'Desafiante':
          pontuacao_time += 0
        if elo3 == 'Bronze':
          pontuacao_time += 1
        if elo3 == 'Prata':
          pontuacao_time += 2
        if elo3 == 'Ouro':
          pontuacao_time += 4
        if elo3 == 'Platina':
          pontuacao_time += 6
        if elo3 == 'Diamante':
          pontuacao_time += 8
        elif elo3 == 'Desafiante':
          pontuacao_time += 10
      
      elif elo1 != '' and elo2 != '' and elo3 != '' and elo4 == '':
        elo4 = elo
        if elo4 != 'Bronze' or elo3 != 'Prata' or elo3 != 'Ouro' or elo3 != 'Platina' or elo3 != 'Diamante' or elo3 != 'Desafiante':
          pontuacao_time += 0
        if elo4 == 'Bronze':
          pontuacao_time += 1
        if elo4 == 'Prata':
          pontuacao_time += 2
        if elo4 == 'Ouro':
          pontuacao_time += 4
        if elo4 == 'Platina':
          pontuacao_time += 6
        if elo4 == 'Diamante':
          pontuacao_time += 8
        elif elo4 == 'Desafiante':
          pontuacao_time += 10
                  
      elif elo1 != '' and elo2 != '' and elo3 != '' and elo4 != '' and elo5 == '':
        elo5 = elo
        if elo5 != 'Bronze' or elo3 != 'Prata' or elo3 != 'Ouro' or elo3 != 'Platina' or elo3 != 'Diamante' or elo3 != 'Desafiante':
          pontuacao_time += 0
        if elo5 == 'Bronze':
          pontuacao_time += 1
        if elo5 == 'Prata':
          pontuacao_time += 2
        if elo5 == 'Ouro':
          pontuacao_time += 4
        if elo5 == 'Platina':
          pontuacao_time += 6
        if elo5 == 'Diamante':
          pontuacao_time += 8
        elif elo5 == 'Desafiante':
          pontuacao_time += 10

if qnt_jogadores == 5:
  print('O time está completo.')
  print(f'{n1} - {l1} ({elo1})')
  print(f'{n2} - {l2} ({elo2})')
  print(f'{n3} - {l3} ({elo3})')
  print(f'{n4} - {l4} ({elo4})')
  print(f'{n5} - {l5} ({elo5})')
  if pontuacao_time > 18:
    print('A GENTE VAI GANHAR!!!')
  else:
    print('Vai dar ruim...')