def id_palindromo(expressao_variavel):
    expressao_sem_espaço = ''.join(expressao_variavel.split())
    termos = expressao_sem_espaço.split()
    junto = ''.join(termos)
    inverso = junto[::-1]
    if inverso == junto:
        if expressao_sem_espaço.isdigit() == True and expressao_sem_espaço.isalpha() == False:
            print(f'O número "{expressao_print}" é um palíndromo!')
            contador_termos(expressao_sem_espaço)
            
        elif expressao_sem_espaço.isdigit() == False and expressao_sem_espaço.isalpha() == True:
            print(f'A frase "{expressao_print}" é um palíndromo!')
            contador_termos(expressao_sem_espaço)
            
        elif expressao_sem_espaço.isdigit() == False and expressao_sem_espaço.isalpha() == False:
            print('A frase ou o número não é um palíndromo.')
    else:
        print('A frase ou o número não é um palíndromo.')

def contador_termos(expressao_sem_espaço):
    termos_distintos = set(expressao_sem_espaço)
    if expressao_variavel.isdigit() == True:
        print(f'Há {len(termos_distintos)} número(s) distinto(s) na sequência de números.')
    else:
        print(f'Há {len(termos_distintos)} letra(s) distinta(s) na frase.')


n = int(input())
for c in range(0, n):
    expressao = input()
    expressao_print = expressao
    expressao_variavel = expressao.strip().lower()
    expressao_sem_espaço = ''.join(expressao_variavel.split())
    id_palindromo(expressao_variavel)
  
  
  
