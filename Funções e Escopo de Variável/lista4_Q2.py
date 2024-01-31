def relatorio_participante():
    velocidade_inicial = qtd_propulsores * velocidade_propulsor
    velocidade_final = qtd_propulsores_final * velocidade_propulsor
    print(f'--- Participante: {nome_participante} ---')
    print(f'Qtd de propulsores Final: {qtd_propulsores_final}')
    print(f'Velocidade Inicial: {velocidade_inicial} km/h')
    print(f'Velocidade Final: {velocidade_final} km/h')

def relatorio_final():
    if participantes_classificados >= 1:
        print(f'Relatório da CIn Pod Race: {participantes_classificados} participantes terminaram a corrida e {participantes_desclassificados} foram desclassificados.')
    elif participantes_classificados == 0:
        print('NÃO! Esses Droides me pagam, sabotaram minha corrida!')

continua_rodadas = True
continua_partida = True

participantes_classificados = 0
participantes_desclassificados = 0
participantes_total = 0
qtd_propulsores_final = 0

while continua_partida == True:
    informacoes = input()
    if informacoes == 'FIM':
      continua_partida = False
    else:
      informacoes = informacoes.split(' ')
      nome_participante = informacoes[0]
      qtd_propulsores = int(informacoes[1])
      qtd_propulsores_final = qtd_propulsores
      velocidade_propulsor = int(informacoes[2])
      while continua_rodadas == True:
        situacao = input()
        if situacao == 'FIM':
            relatorio_participante()
            participantes_classificados += 1
            continua_partida = False
            break
  
        elif situacao == 'Pit-Stop Espacial':
            qtd_propulsores_final += 1
  
        elif situacao == 'Um Droide apareceu do nada na pista, do nadaaa! Perdi o controle e bati em uma pedra.':
            qtd_propulsores_final -= 1
            if qtd_propulsores_final == 0:
                print(f'BUUMM!! Infelizmente, {nome_participante} está fora da corrida.')
                participantes_desclassificados += 1
                participantes_total += 1
                break
            else:
              participantes_total += 1
                
  
        elif situacao == 'Opa esse participante tem ID de Droide, desclassificando em 3, 2, 1...':
            print(f'O {nome_participante} achou que não descobriríamos, tirem {nome_participante} imediatamente da pista.')
            participantes_desclassificados += 1
            participantes_total += 1
            break
            
  
        elif situacao == 'Próximo':
            relatorio_participante()
            participantes_classificados += 1
            participantes_total += 1
            break

if continua_partida == False:
    relatorio_final()

