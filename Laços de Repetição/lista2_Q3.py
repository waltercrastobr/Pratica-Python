qnt_garrafas = 20
frase = input()

while frase != ('O InterCIn acabou!!! Vamos verificar nosso estoque de bebidas'):
    if frase == ('Acabou uma partida e precisamos da seguinte quantidade de garrafas para matar a sede dos jogadores'):
        qnt_jogadores = int(input())
        if qnt_jogadores > qnt_garrafas:
            n = (qnt_jogadores) - qnt_garrafas
            print(f'Não teremos água para todos os jogadores... Temos que garantir {n} garrafas!!')
            qnt_garrafas = qnt_garrafas * 2
            if qnt_garrafas < qnt_jogadores:
                qnt_garrafas = qnt_garrafas - qnt_jogadores
            elif qnt_jogadores <= qnt_garrafas:
                qnt_garrafas = qnt_garrafas - qnt_jogadores
        else:
          qnt_garrafas = qnt_garrafas - qnt_jogadores
        frase = input()

    elif frase == ('Encham o cooler! O jogo vai começar!!!!'):
      qnt_garrafas = qnt_garrafas + 15
      print('Geladeira cheia!')
      frase = input()

    elif frase == ('Timeout da partida! Verifiquem quantas garrafas pediram aos voluntários'):
        quantidade_1 = int(input())
        quantidade_2 = int(input())
        quantidade_3 = int(input())
        quantidade_4 = int(input())
        quantidade_5 = int(input())
        total = (quantidade_1) + (quantidade_2) + (quantidade_3) + (quantidade_4) + (quantidade_5)
        if qnt_garrafas < total:
            n = abs(total - qnt_garrafas)
            print(f'Faltaram {n} garrafas para atender o pedido feito aos voluntários')
            qnt_garrafas = qnt_garrafas - total
            frase = 'O InterCIn acabou!!! Vamos verificar nosso estoque de bebidas'
        else:
            qnt_garrafas = qnt_garrafas - total
            frase = input()

else:
    if qnt_garrafas > 0:
        print(f'Sobraram {qnt_garrafas} garrafas, vamos guardar na geladeira :D')
    elif qnt_garrafas == 0:
        print('Vendemos todas as garrafas! Nosso planejamento foi perfeito!')
    elif qnt_garrafas < 0:
        print('Por questões logísticas, teremos que acabar com os jogos...')