funcionalidade1 = str(input())
funcionalide1_ponto = int(input())
funcionalidade2 = str(input())
funcionalide2_ponto = int(input())
funcionalidade3 = str(input())
funcionalide3_ponto = int(input())
funcionalidade4 = str(input())
funcionalide4_ponto = int(input())
funcionalidade5 = str(input())
funcionalide5_ponto = int(input())

soma_funcionalidade = int(funcionalide1_ponto + funcionalide2_ponto + funcionalide3_ponto + funcionalide4_ponto + funcionalide5_ponto)

if funcionalidade1 == 'novo lançador de teias':
  print('Com calma, aranha')

if funcionalidade1 == 'novo lançador de teias' and funcionalidade2 == 'lentes de visão avançada':
  print('Lembre de desativar as lentes depois, e cuidado ao usar as teias no escuro')

if funcionalidade1 == 'novo lançador de teias' and funcionalidade2 == 'lentes de visão avançada' and funcionalidade3 == 'traje à prova de balas':
  print('UOU, só tente sair dessa vivo, vou otimizar a energia aqui')
  
if funcionalidade1 == 'ativação de inteligência artificial':
  print('Espero que não esteja ativando isso para usar nas provas')
if funcionalidade2 == 'ativação de inteligência artificial':
  print('Espero que não esteja ativando isso para usar nas provas')
if funcionalidade3 == 'ativação de inteligência artificial':
  print('Espero que não esteja ativando isso para usar nas provas')
if funcionalidade4 == 'ativação de inteligência artificial':
  print('Espero que não esteja ativando isso para usar nas provas')
if funcionalidade5 == 'ativação de inteligência artificial':
  print('Espero que não esteja ativando isso para usar nas provas')

if (soma_funcionalidade) >= 80:
  print('Vou descarregar em questão de minutos, pare AGORA')
  
if ((funcionalidade1 =='ativação de inteligência artificial') or (funcionalidade2 =='ativação de inteligência artificial') or (funcionalidade3 == 'ativação de inteligência artificial') or (funcionalidade4 == 'ativação de inteligência artificial') or (funcionalidade5 == 'ativação de inteligência artificial')) and ((funcionalidade1 == 'membranas planadoras') or (funcionalidade2 == 'membranas planadoras') or (funcionalidade3 == 'membranas planadoras') or (funcionalidade4 == 'membranas planadoras') or (funcionalidade5 == 'membranas planadoras')) and ((funcionalidade1=='novo lançador de teias') or (funcionalidade2=='novo lançador de teias') or (funcionalidade3=='novo lançador de teias') or (funcionalidade4 =='novo lançador de teias') or (funcionalidade5 == 'novo lançador de teias')):
  print('Tudo certo, mas cuidado ao ficar conversando com IA enquanto voa')
  
print(f'Aranha, nessa sequência você usou {soma_funcionalidade} de energia!')


