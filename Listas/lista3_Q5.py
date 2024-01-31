lista = []
n = int(input())
for c in range(0, n):
    for i in range(0, n):
      tamanho_comodo = input()
      lista.append(tamanho_comodo)
      lista_final = ' '.join(lista)
    lista.clear()
    print(lista_final)
