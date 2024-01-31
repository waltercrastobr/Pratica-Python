lista_n = input().split(' ; ')
limite_item = int(lista_n[0])
limite_custo = int(lista_n[1])

lista_itens = []
lista_precos = []
lista_filmes = []

objeto_filme = []
filme_preco = []

itens = 0
custo = 0
frase = input()

while frase != 'Fim! Muito obrigada pela ajuda!!':
  if frase == 'Quero adicionar um item':
    item_adicionado = input()
    objeto_filme = item_adicionado.split(' - ')
    filme_preco = item_adicionado.split(' , ')
    objeto = objeto_filme[0]
    preco = int(filme_preco[1])
    if itens >= limite_item or custo + preco > limite_custo:
      print('Avise a Barbie que isso não será possível.')
    else:
      lista_itens.append(objeto)
      lista_precos.append(preco)
      lista_filmes.append(filme_preco[0])
      itens += 1
      custo += int(preco)
      print(f'Vá em frente, Ken! Você ainda tem {limite_custo - custo} barbieCoins disponíveis')

  elif frase == 'Quero remover um item':
    item_removido = input()
    if item_removido not in lista_itens:
      print('Barbie, infelizmente não consegui fazer isso.')
    else:
      print('Ok, Barbie!')
      posicao_item_removido = int(lista_itens.index(item_removido))
      itens -= 1
      custo -= int(lista_precos[posicao_item_removido])
      lista_itens.pop(posicao_item_removido)
      lista_precos.pop(posicao_item_removido)
      lista_filmes.pop(posicao_item_removido)
      print(f'Ken, você ainda tem {limite_custo - custo} barbieCoins disponíveis')

  elif frase == 'Poderia me lembrar os itens que estão até então e de qual filme eles foram recuperados?':
    if len(lista_itens) == 0:
      print('Por enquanto seu museu está vazio, Barbie. Vamos trabalhar nisso!')
    else:
      print('Claro!')
      for c in lista_filmes:
        print(c)
        
  frase = input()

if frase == 'Fim! Muito obrigada pela ajuda!!':
    print('Por nada! Estou sempre à disposição!')
    