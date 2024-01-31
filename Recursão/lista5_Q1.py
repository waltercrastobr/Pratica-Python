letras_min = ['a', 'e', 'i', 'o', 'u','b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'y', 'w', 'z']

def fatorial_k(n):
  if n == 0:
    return 1
  else:
    return n * fatorial_k(n-1)

def id_min_mai(str_random):
  cont_letras_min = 0
  cont_letras_mai = 0

  for letra in str_random:
    if letra in letras_min:
      cont_letras_min += 1
    else:
      cont_letras_mai += 1
      
  if cont_letras_mai != cont_letras_min:
    if cont_letras_mai > cont_letras_min:
      return fatorial_k(cont_letras_mai) * len(str_random)
    elif cont_letras_min > cont_letras_mai:
      return fatorial_k(cont_letras_min) * len(str_random)
      
  elif cont_letras_mai == cont_letras_min:
    return (len(str_random)**2)
  

str_random = input()
preco = id_min_mai(str_random)

if preco >= 100:
  print(f'Hum... {preco}? Acho que na volta eu compro')
else:
  print(f'{preco}! Vou comprar todos!')
  


