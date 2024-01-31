def ordenar_por_nota(lista):
  for i in range(len(lista)):
    indice_max_nota = i
    for c in range(i + 1, len(lista)):
      if lista[c]["Nota"] > lista[indice_max_nota]["Nota"]:
        indice_max_nota = c
    lista[i], lista[indice_max_nota] = lista[indice_max_nota], lista[i]
        
dicionario_artistas = {}
entradas = []
lista_natty = []
lista_fake = []

n = int(input())

for c in range(0,n):
  info = input()
  entradas.append(info)
  
for entrada in entradas:
  partes = entrada.split('- ')
  nome = partes[0]
  nota = int(partes[1])
  avaliacao = partes[2]

  dicionario_artistas[nome] = {"Nome": nome, "Nota": nota, "Avaliação": avaliacao}
  

for nome, partes in dicionario_artistas.items():
  if partes["Avaliação"] == 'natty':
    lista_natty.append({"Nome": nome,"Nota": partes["Nota"], "Avaliação": partes["Avaliação"]})
  elif partes["Avaliação"] == 'FAKE NATTY':
    lista_fake.append({"Nome": nome,"Nota": partes["Nota"], "Avaliação": partes["Avaliação"]})
    
ordenar_por_nota(lista_natty)
ordenar_por_nota(lista_fake)

tupla_natty = tuple(lista_natty)
tupla_fake = tuple(lista_fake)

for artista in tupla_natty:
  print(f"{artista['Nome']}- {artista['Nota']} - {artista['Avaliação']}")

for artista in tupla_fake:
  print(f"{artista['Nome']}- {artista['Nota']} - {artista['Avaliação']}")