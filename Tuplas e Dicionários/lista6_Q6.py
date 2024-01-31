dicionario_linha = {}
dicionario_tri = {}
partes = []
termos_encontrados = []
linha_atual = ''
cont_linha = 0
continuar = True

while continuar == True:
  linha_atual = str(input()).lower()
  if linha_atual == 'end_of_file':
    continuar = False
  else:
    dicionario_linha.update({linha_atual: cont_linha})
    for i in range(0, len(linha_atual), 3):
      dicionario_tri.update({linha_atual[i:i + 3]: cont_linha})
  cont_linha += 1
  
qtd_buscas = int(input())

for c in range(0, qtd_buscas):
  trecho = input().lower()
  tri_grama = trecho[:3]
  for termo, cont_linha in dicionario_linha.items():
    if tri_grama in termo:
      if trecho in termo:
        termos_encontrados.append(cont_linha)
    
  if len(termos_encontrados) > 0:
    print(termos_encontrados[0])
  else:
      print('-1')
    
  termos_encontrados = []