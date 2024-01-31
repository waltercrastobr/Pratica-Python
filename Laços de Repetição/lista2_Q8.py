equipe1_nome1 = input()
equipe1_nome2 = input()
equipe2_nome1 = input()
equipe2_nome2 = input()
quantidade_partidas = int(input())
continuar = True

vitoria_time1 = 0
vitoria_time2 = 0
pontos_totais_time1 = 0
pontos_totais_time2 = 0

print(f'VAMO VER QUEM VAI COMER GRAMA! TEREMOS {quantidade_partidas} PARTIDAS ENTRE:')
print(f'{equipe1_nome1} e {equipe1_nome2} X {equipe2_nome1} e {equipe2_nome2}')

for c in range(0, quantidade_partidas):
    if continuar == True:
        pontuacao_time1 = int(input())
        pontuacao_time2 = int(input())
        pontos_totais_time1 += pontuacao_time1
        pontos_totais_time2 += pontuacao_time2
        if pontuacao_time1 == 0:
            print("JOGO ENCERRADO POR DESISTÊNCIA DA EQUIPE 1, QUE VERGONHA")
            continuar = False
        elif pontuacao_time2 == 0:
            print('JOGO ENCERRADO POR DESISTÊNCIA DA EQUIPE 2, QUE VERGONHA')
            continuar = False
        else:
            if pontuacao_time1 > pontuacao_time2:
                vitoria_time1 += 1
            elif pontuacao_time1 < pontuacao_time2:
                vitoria_time2 += 1
            elif pontuacao_time1 == pontuacao_time2:
                vitoria_time1 += 1

coeficiente_time1 = pontos_totais_time1 * (vitoria_time1 / quantidade_partidas)
coeficiente_time2 = pontos_totais_time2 * (vitoria_time2 / quantidade_partidas)

if continuar == True:
    print(f'CARAMBA! Tivemos um total de {pontos_totais_time1 + pontos_totais_time2} bolas ao chão ao longo dessa disputa.')
    if coeficiente_time1 >= coeficiente_time2 :
        print(f'{equipe1_nome1} e {equipe1_nome2} são os grandes vencedores!')
        print(f'Mataram {pontos_totais_time1} bolas, ganhando {vitoria_time1} partidas')
    else:
        print(f'{equipe2_nome1} e {equipe2_nome2} são os grandes vencedores!')
        print(f'Mataram {pontos_totais_time2} bolas, ganhando {vitoria_time2} partidas')