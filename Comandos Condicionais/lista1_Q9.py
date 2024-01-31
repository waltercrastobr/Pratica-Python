vida_max_venom = int(input())
ataque_venom = int(input())
pocao_venom = int(input())
ataque_creeper = ataque_venom
vida_inicial_creeper = int(input())
vida_druida = int(input())
ataque_druida = int(input())
vitoria_venom = 0

print('SENHORAS E SENHORES! AGORA O VENOM ENFRENTARÁ O CREEPER!')
if ataque_creeper >= vida_max_venom:
    if ataque_creeper < vida_inicial_creeper:
        print('O venom não tankou e foi de base...')
        print('AH NÃO! O VENOM PEGOU EM BOMBA!')
        vitoria_venom += 0
    elif ataque_creeper >= vida_inicial_creeper:
        print('O venom não tankou e foi de base...')
        print('O creeper não tankou e foi de base...')
        print('AH NÃO! O VENOM PEGOU EM BOMBA!')
        vitoria_venom += 0

elif ataque_venom >= vida_inicial_creeper:
    if ataque_venom < vida_max_venom:
        print('O creeper não tankou e foi de base...')
        print('Isso aí! Ele é todo esquentadinho, mas no final deu tudo certo!')
        vitoria_venom += 1
        vida_venom = vida_max_venom - ataque_creeper
        if vida_venom + pocao_venom <= vida_max_venom:
            vida_venom = vida_venom + pocao_venom
            print('Ah! Essa poção é da boa!')

    elif ataque_venom >= vida_max_venom:
        print('O venom não tankou e foi de base...')
        print('O creeper não tankou e foi de base...')
        print('AH NÃO! O VENOM PEGOU EM BOMBA!')
        vitoria_venom += 0

elif ataque_venom < vida_inicial_creeper and ataque_creeper < vida_max_venom:
    vida_venom = vida_max_venom - ataque_creeper
    vida_creeper = vida_inicial_creeper - ataque_creeper
    dano_recebido_venom1 = ataque_creeper
    dano_recebido_creeper = ataque_venom
    if vida_venom > vida_creeper:
        print(f'Vida atual do Venom: {vida_venom}')
        print(f'Dano sofrido pelo Venom: {dano_recebido_venom1}')
        print(f'Vida atual do creeper: {vida_creeper}')
        print(f'Dano sofrido pelo creeper: {dano_recebido_creeper}')
        print('Isso aí! Ele é todo esquentadinho, mas no final deu tudo certo!')
        vitoria_venom += 1
        if vida_venom + pocao_venom <= vida_max_venom:
            vida_venom = vida_venom + pocao_venom
            print('Ah! Essa poção é da boa!')

    elif vida_venom < vida_creeper:
        print(f'Vida atual do Venom: {vida_venom}')
        print(f'Dano sofrido pelo Venom: {dano_recebido_venom1}')
        print(f'Vida atual do creeper: {vida_creeper}')
        print(f'Dano sofrido pelo creeper: {dano_recebido_creeper}')
        print('AH NÃO! O VENOM PEGOU EM BOMBA!')
        vitoria_venom += 0

    else:
        print(f'Vida atual do Venom: {vida_venom}')
        print(f'Dano sofrido pelo Venom: {dano_recebido_venom1}')
        print(f'Vida atual do creeper: {vida_creeper}')
        print(f'Dano sofrido pelo creeper: {dano_recebido_creeper}')
        print('AH NÃO! O VENOM PEGOU EM BOMBA!')
        vitoria_venom += 0

if vitoria_venom == 0:
    print('Pelo visto as aventuras do Miles terminaram por aqui...')
    
if vitoria_venom == 1:
    print('SENHORAS E SENHORES! AGORA O VENOM ENFRENTARÁ O DRUIDA!')

    vida_venom3 = vida_venom + pocao_venom
    if vida_venom3 > vida_max_venom:
        vida_venom4 = vida_max_venom - (vida_venom3 - vida_max_venom)
    else:
        vida_venom4 = vida_venom3

    taxa_envenenamento = vida_venom3 - vida_max_venom

    vida_venom_final = vida_venom4 - ataque_druida
    vida_druida2 = vida_druida - ataque_venom

    if vida_druida2 <= 0 and vida_venom_final >= 1:
        print('O druida não tankou e foi de base...')
        print('Quase me dei mal, nunca mais aceito nada de estranho...')
        vitoria_venom += 1

    elif vida_druida2 >= 1 and vida_venom_final <= 0:
        print('O venom não tankou e foi de base...')
        print('Pelo visto a poção tava fora do prazo de validade :(')
        vitoria_venom += 0

    elif vida_druida2 <= 0 and vida_venom_final <= 0:
        print('O venom não tankou e foi de base...')
        print('O druida não tankou e foi de base...')
        print('Pelo visto a poção tava fora do prazo de validade :(')
        vitoria_venom += 0

    elif vida_druida2 >= 1 and vida_venom_final >= 1:
        print(f'Vida atual do Venom: {vida_venom_final}')
        print(f'Dano sofrido pelo Venom: {ataque_druida + taxa_envenenamento}')
        print(f'Vida atual do druida: {vida_druida2}')
        print(f'Dano sofrido pelo druida: {ataque_venom}')

        if ataque_venom > ataque_druida:
            print('Quase me dei mal, nunca mais aceito nada de estranho...')
            vitoria_venom += 1
        elif ataque_venom < ataque_druida:
            print('Pelo visto a poção tava fora do prazo de validade :(')
            vitoria_venom += 0
        elif ataque_druida == ataque_venom:
            if vida_venom_final > vida_druida2:
                print('Quase me dei mal, nunca mais aceito nada de estranho...')
                vitoria_venom += 1
            elif vida_venom_final < vida_druida2:
                print('Pelo visto a poção tava fora do prazo de validade :(')
                vitoria_venom += 0
            elif vida_venom_final == vida_druida2:
                print('Pelo visto a poção tava fora do prazo de validade :(')

    if vitoria_venom == 2:
        print('Essa aventura foi epicamente épica, meu amigo! Boa viagem aí! * Começa a tocar saxofone *')
    elif vitoria_venom < 2:
        print('Pelo visto as aventuras do Miles terminaram por aqui...')