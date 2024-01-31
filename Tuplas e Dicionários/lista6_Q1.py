def ordenar_por_nome(item):
    return item['Nome']

dicionario_artistas = {}
entradas = []
lista_fake = []

qnt_famosos = int(input())

for c in range(0, qnt_famosos):
  info = input()
  entradas.append(info)

for entrada in entradas:
  partes = entrada.split('-')
  detalhes = partes[1].split(' ')
  nome = partes[0]
  profissao = detalhes[1]
  avaliacao = detalhes[2]
  mes = int(detalhes[3])

  dicionario_artistas[nome] = {"Nome": nome, "Profissão": profissao, "Avaliação": avaliacao, "Mês": mes}

mes_consultado = int(input())

for nome, detalhes in dicionario_artistas.items():
  if detalhes["Mês"] == mes_consultado:
    if detalhes["Avaliação"] == 'fake':
      lista_fake.append({"Nome": nome, "Profissão": detalhes["Profissão"]})
      
lista_fake_ordenada = sorted(lista_fake, key = ordenar_por_nome)
      
if len(lista_fake) == 0:
  print('Até agora não temos ninguém pra expor na internet neste mês :(')
else:
  print(f'Os fake nattys do mês são:')
  for artista in lista_fake_ordenada:
    print(f"{artista['Nome']}- {artista['Profissão']}")