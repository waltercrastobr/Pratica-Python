n = int(input())
def calculadora (operacao):
  if operacao == 'Quero somar esses dois números:':
    res = n1 + n2
    print(f'O resultado da {c}ª operação foi {res:.1f}')
  elif operacao == 'Preciso subtrair um pelo outro':
    res = n1 - n2
    print(f'O resultado da {c}ª operação foi {res:.1f}')
  elif operacao == 'Quanto dá o produto disso?':
    res = n1 * n2
    print(f'O resultado da {c}ª operação foi {res:.1f}')
  elif operacao == 'Vou dividir aqui rapidinho':
    res = n1 / n2
    print(f'O resultado da {c}ª operação foi {res:.1f}')
  elif operacao == 'E se eu elevar um pelo outro?':
    res = n1 ** n2
    print(f'O resultado da {c}ª operação foi {res:.1f}')
    
  
for c in range(1, n+1):
  operacao = input()
  n1 = float(input())
  n2 = float(input())
  calculadora(operacao)
  
if n == 0:
  print('Vou relaxar aqui na minha nave')
else:
  print('Ufa, já deu de cálculos por hoje!')
  
    
  
  