repetidas = 0
lista = []
lista_final = []

n = int(input())
while len(lista) < n:
    nome_da_criatura = input()
    lista.append(nome_da_criatura)
    if lista.count(nome_da_criatura) > 1:
        repetidas += 1
    elif lista.count(nome_da_criatura) == 1:
        lista_final.append(nome_da_criatura)

for c in range(0, repetidas):
    print('Criatura repetida')
print('Registradas:')
for i in lista_final:
    print(i)