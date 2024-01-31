lista_ja_tenho_em_casa = []
lista_desejo = input().split(', ')
lista_casa = input().split(', ')
for objeto_desejado in lista_desejo:
  if objeto_desejado in lista_casa:
    lista_ja_tenho_em_casa.append(objeto_desejado)

if len(lista_ja_tenho_em_casa) == 0:
  print(f'Nossa, irei ao shopping agora mesmo! Não tenho nenhum dos {len(lista_desejo)} itens em casa.')
elif len(lista_ja_tenho_em_casa) <= len(lista_casa) and len(lista_ja_tenho_em_casa) != 0:
  print('Esses são os itens que já tenho em casa:')
  for c in range(0, len(lista_ja_tenho_em_casa)):
    print(f'{c+1}º item: {lista_ja_tenho_em_casa [c]}')
  preciso_comprar = int(len(lista_desejo) - len(lista_ja_tenho_em_casa))
  if preciso_comprar == 0:
    print(f'Que ótimo, consegui encontrar cada um dos {len(lista_desejo)} itens!')
  elif preciso_comprar > 0:
    print(f'Irei precisar comprar {preciso_comprar} itens antes do meu encontro!')
  
print('Isso é tudo! Hora de me preparar!')