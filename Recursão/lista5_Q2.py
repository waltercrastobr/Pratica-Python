cont_vitoria = 0
cont_derrota = 0

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
        
lista_fibo = []
for c in range(0, 21):
  lista_fibo.append(fibo(c))

M_N = input().split(' ')
total_vidas = int(M_N[0])
total_casas = int(M_N[1])
casas_iniciais = total_casas

while cont_derrota < total_vidas and total_casas > 0:
  numero_da_casa = int(input())
  if numero_da_casa in lista_fibo:
    total_casas -= 1
  else:
    cont_derrota += 1
    total_casas = casas_iniciais
    print('Oh nao Link! Voce nao pode parar ainda, voce e a ultima esperanca de Hyrule!')
    
else:
  if cont_derrota == total_vidas:
    print('A ultima defesa de hyrule caiu, nao sobrou ninguem capaz de se opor a Ganondorf')
  elif total_casas == 0:
    print('Voce Adicionou A Master Sword ao seu inventario\nLink Salve Hyrule!!!')