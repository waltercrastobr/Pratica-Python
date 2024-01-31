dicionario_expressoes = {
    "Oooh look at him": '0',
    "Baseball bat": '1',
    "Aesthetic": '2',
    "Fake Natty": '3',
    "Chris Bumbstead, o CBUM": '4',
    "Pope Francis": '5',
    "O suco vicia": '6',
    "I don't know you tell me": '7',
    "Não é mesmo?": '8',
    "Rodrigo Goes out": '9'
}

entradas = []
numeros = []
contagem_numeros = {}

n = int(input())

for c in range(0,n):
  info = input()
  entradas.append(info)
  
for entrada in entradas:
  partes = entrada.split('+')
  expressao_concatenada = ''
  for i in partes:
    expressao_concatenada += dicionario_expressoes[i]
  numeros.append(int(expressao_concatenada))
numeros.sort()

count_0 = numeros.count(0)
count_atual = 0

correto = True
if 0 not in numeros:
  correto = False
else:
  for p in range(0, len(numeros) - 1):
    count_atual = numeros.count(p)
    if count_atual > count_0:
      correto = False
    else:
      count_0 = count_atual
      if int(numeros[p]) != int(numeros[p + 1]):
        if int(numeros[p + 1]) - int(numeros[p]) > 1:
          correto = False

if correto == True:
  print('YES')
elif correto == False:
  print('NO')
  
