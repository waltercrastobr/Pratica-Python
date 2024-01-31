profissao_prevista = input()
bolsa = []
profissao_do_dia = input()
bolsa_certa = []

if profissao_do_dia == 'Medica':
  bolsa_certa =['Estetoscopio', 'Esfigmomanometro', 'Jaleco', 'Caneta' , 'Celular']
if profissao_do_dia == 'Assistente de Informatica':
  bolsa_certa = ['Calculadora', 'Oculos', 'Notebook', 'Camisa Social', 'Caderno']
if profissao_do_dia == 'Padeira':
  bolsa_certa = ['Rolo', 'Caneta', 'Avental', 'Colher de Pau', 'Caderno']
if profissao_do_dia == 'Economista':
  bolsa_certa = ['Calculadora', 'Caneta', 'Camisa Social', 'Agenda', 'Celular']
if profissao_do_dia == 'Personal Trainer':
  bolsa_certa = ['Halter', 'Agenda', 'Celular', 'Legging', 'Corda']
  
if profissao_prevista == 'Medica':
  bolsa = ['Estetoscopio', 'Esfigmomanometro', 'Jaleco', 'Caneta' , 'Celular']
if profissao_prevista == 'Assistente de Informatica':
  bolsa = ['Calculadora', 'Oculos', 'Notebook', 'Camisa Social', 'Caderno']
if profissao_prevista == 'Padeira':
  bolsa = ['Rolo', 'Caneta', 'Avental', 'Colher de Pau', 'Caderno']
if profissao_prevista == 'Economista':
  bolsa = ['Calculadora', 'Caneta', 'Camisa Social', 'Agenda', 'Celular']
if profissao_prevista == 'Personal Trainer':
  bolsa = ['Halter', 'Agenda', 'Celular', 'Legging', 'Corda']

acao = input()
while acao != 'Sair':
  item = input()
  if acao == 'Adicionar':
    if item in bolsa_certa and item not in bolsa:
     print(f'{item} adicionado à bolsa')
     bolsa.append(item)
    elif item not in bolsa_certa:
      print(f'Barbie, {item} não esta na lista de itens de {profissao_do_dia}')
    elif item in bolsa:
      print(f'Barbie, você já colocou {item} na bolsa')
      
  elif acao == 'Retirar':
    if item in bolsa and item not in bolsa_certa:
      print(f'{item} retirado da bolsa')
      bolsa.remove(item)
    elif item in bolsa and item in bolsa_certa:
      print(f'Não faca isso Barbie, você precisa de {item} para trabalhar de {profissao_do_dia}')
    elif item not in bolsa:
      print('Barbie, como você vai retirar algo que já não esta ai?')
      
  acao=input()
  
if acao == 'Sair':
  lista_final = sorted(bolsa)
  lista_itens = ', '.join(lista_final)
  print(f'Itens na bolsa: {lista_itens}')
    
  if sorted(lista_final) == sorted(bolsa_certa):
    print('Boa Barbie, foi na correria mas tudo deu certo!')
    
  else:
    for i in bolsa_certa:
      if i not in bolsa:
        print(f'Oh não!! Barbie, você esqueceu de pegar {i}!!')
    for c in bolsa:
      if c not in bolsa_certa:
        print(f'Barbie, você esqueceu de tirar {c}, você não usa ele trabalhando de {profissao_do_dia}')    
    
  