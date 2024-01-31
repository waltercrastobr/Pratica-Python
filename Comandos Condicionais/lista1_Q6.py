nome = str(input())
total_pessoas = int(input())
coef = float(input())

if total_pessoas % 2 == 0:
  pessoas_fumantes = coef * (total_pessoas - 1) + 1
else:
  pessoas_fumantes = coef * (total_pessoas - 1) / 2
  
decimal_fumantes = float(pessoas_fumantes) - int(pessoas_fumantes)  

if decimal_fumantes > 0.5:
  pessoas_fumantes_final = int(pessoas_fumantes) + 1
else:
  pessoas_fumantes_final = int(pessoas_fumantes)
  
prop = (pessoas_fumantes_final / total_pessoas) * 100

print(f'Vamos verificar se {nome} vai fumar singaro!')
print(f'{int(prop)}% dos seus amigos fumam singaro')

if prop < 25:
  print('Você tem poucas chances de fumar singaro, fuma não pow, cuide da sua saúde')
elif 50 > prop > 25:
  print('Cuidado pra não fumar ein, fuma não pow, cuide da sua saúde')
else:
  print('TIRA ESSE SINGARO DA BOCA. FUMA NÃO POW, CUIDE DA SUA SAÚDE!')
