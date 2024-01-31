def termo_mais_repetido(lista_strings):
  
  contador = {}
  for termo in lista_strings:
    if termo in contador:
      contador[termo] += 1
    else:
      contador[termo] = 1
            
  max_repeticoes = max(contador.values())  
    
  termos_com_max_repeticoes = []  
  for termo, freq in contador.items():
    if freq == max_repeticoes:
      termos_com_max_repeticoes.append(termo)
      
  termo_mais_comum = min(termos_com_max_repeticoes) 
    
  return termo_mais_comum, max_repeticoes
  
  
dicionario_letras = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g',
8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p',
17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}

lista_strings = []

qnt_linhas = int(input())

for c in range(0,qnt_linhas):
  string_underline = input()
  for i in dicionario_letras:
    string_letra = string_underline.replace('_', str(dicionario_letras[i]))
    lista_strings.append(string_letra)

termo, quantidade = termo_mais_repetido(lista_strings)

print(f'{termo} {quantidade}')

 