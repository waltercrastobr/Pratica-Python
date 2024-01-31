pontosmanchestergeral = 0
pontosspicinggeral = 0
cont = 0
continuar = True

n = int(input())
while cont < n and continuar == True:
    nome = input()
    if nome == 'Manchester CIn':
        gols = int(input())
        chutes = int(input())
        ca = int(input())
        cv = int(input())
        pontosmanchester = ((10 * gols) + (3 * chutes) + ((-2) * (ca)) + ((-4) * (cv)))
        pontosmanchestergeral += pontosmanchester
        cont += 1
        if gols >= (0.3) * chutes:
            pontosmanchestergeral += 3
        if cv >= ca:
            pontosmanchestergeral -= 3
        if pontosmanchestergeral < 0:
          continuar = False
            

    if nome == 'SpiCIn Girls':
        gols = int(input())
        chutes = int(input())
        ca = int(input())
        cv = int(input())
        pontosspicing = ((10 * gols) + (3 * chutes) + ((-2) * (ca)) + ((-4) * (cv)))
        pontosspicinggeral += pontosspicing
        cont += 1
        if gols >= (0.3) * chutes:
            pontosspicinggeral += 3
        if cv >= ca:
            pontosspicinggeral -= 3
        if pontosspicinggeral < 0:
          continuar = False

if pontosmanchestergeral < 0:
    print(f'O time Manchester CIn ficou com pontuação negativa. A aposta não é segura, podemos perder nosso dinheiro.')
elif pontosspicinggeral < 0:
    print(f'O time SpiCIn Girls ficou com pontuação negativa. A aposta não é segura, podemos perder nosso dinheiro.')
else:
    if pontosmanchestergeral > pontosspicinggeral:
        print(f'Com {(100 * pontosmanchestergeral) / (pontosspicinggeral + pontosmanchestergeral):.2f}% dos pontos, o time Manchester CIn pode garantir nosso dinheiro na CInBet, é uma das grandes apostas do InterCIn.')
    if pontosspicinggeral > pontosmanchestergeral:
        print(f'Com {(100 * pontosspicinggeral) / (pontosspicinggeral + pontosmanchestergeral):.2f}% dos pontos, o time SpiCIn Girls pode garantir nosso dinheiro na CInBet, é uma das grandes apostas do InterCIn.')