nome_aluno = input()
nome_professor = input()

pontos_aluno = 0
pontos_professor = 0

vitoria_partida_aluno = 0
vitoria_partida_professor = 0

print(f'E agora, só pela resenha:')
print(f'Melhor de 3 entre: {nome_aluno} e {nome_professor}!')
print('COMEÇOU!')

while vitoria_partida_aluno < 2 and vitoria_partida_professor < 2:
  num = int(input())
  if num % 2 != 0:
    pontos_aluno += 1
    print(f'{pontos_aluno} - {pontos_professor}')
    
  elif num % 2 == 0:
    pontos_professor += 1
    print(f'{pontos_aluno} - {pontos_professor}')
    
  if pontos_aluno >= 11 and pontos_aluno > 1 + pontos_professor:
    vitoria_partida_aluno += 1
    pontos_aluno = 0
    pontos_professor = 0
    print(f'{nome_aluno} ganhou esta partida!')
    print(f'Placar: {nome_aluno} [{vitoria_partida_aluno}-{vitoria_partida_professor}] {nome_professor}')

  elif pontos_professor >= 11 and pontos_professor > 1 + pontos_aluno:
    vitoria_partida_professor += 1
    pontos_aluno = 0
    pontos_professor = 0
    print(f'{nome_professor} ganhou esta partida!')
    print(f'Placar: {nome_aluno} [{vitoria_partida_aluno}-{vitoria_partida_professor}] {nome_professor}')
        
else:
  print('FIM DA SÉRIE!')
  if vitoria_partida_aluno >= 2:
    print(f'{nome_aluno} ganhou a série! Puro talento!')
  elif vitoria_partida_professor >= 2:
    print(f'{nome_professor} ganhou a série! A experiência ganhou!')


    