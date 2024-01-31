n = int(input())
maior = 0
menor = 0
duplavencedora = ''
duplaperdedora = ''
pontfinalvencedor = 0
pontfinalperdedor = 0

for c in range (1, (n + 1)):
  nome_duplas = input()
  periodo_duplas = int(input())
  pontos_duplas = int(input())
  pont_final = pontos_duplas / periodo_duplas
  if c == 1:
    maior = pont_final
    duplavencedora = (nome_duplas)
    pontfinalvencedor = (pont_final)
    menor = pont_final
    duplaperdedora = (nome_duplas)
    pontfinalperdedor = (pont_final)
  else:
    if pont_final > maior:
      maior = pont_final
      duplavencedora = (nome_duplas)
      pontfinalvencedor = (pont_final)
    if pont_final < menor:
      menor = pont_final
      duplaperdedora = (nome_duplas)
      pontfinalperdedor = (pont_final)

print(f'A dupla vencedora foi {duplavencedora} com a pontuação final de {pontfinalvencedor :.2f} pontos.')
print(f'A dupla perdedora foi {duplaperdedora} com a pontuação final de {pontfinalperdedor :.2f} pontos.')

    
    
