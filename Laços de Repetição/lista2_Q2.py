qnt_participantes = int(input())
maior = 0
nomemaior = 0
for c in range(1, (qnt_participantes + 1)):
    nome = input()
    pont = int(input())
    penal = int(input())
    pont_final = pont - penal
    if c == 1:
        maior = pont_final
        nomemaior = nome
    else:
        if pont_final > maior:
            maior = pont_final
            nomemaior = nome
print(f'O grande vencedor do torneio foi {nomemaior} com um total de {maior} pontos!')