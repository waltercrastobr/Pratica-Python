n = int(input())
n1 = 1
n2 = 1
if n > 1:
  print(f'A sequência de número das camisas do seu time será: {n1}, {n2}', end ='')
  cont = 3
  while cont <= n and n > 1:
    n3 = n1 + n2
    print(f', {n3}' , end='')
    n1 = n2
    n2 = n3
    cont += 1
    
elif n == 1:
  print('A sequência de número das camisas do seu time será: 1')
  
