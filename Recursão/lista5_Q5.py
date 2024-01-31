def percursso_link(mapa, sala_atual, possui_espada, salas_percorridas):
    continuar = True
    if sala_atual in salas_percorridas:
        return 0, False

    salas_percorridas.add(sala_atual)
    itens_sala = mapa[sala_atual]

    quantidade_rupees = 0
    princesa_resgatada = False

    for item in itens_sala:
        if item == "espada":
            possui_espada = True

        elif item == "Zelda":
            continuar = False
            if possui_espada:
                princesa_resgatada = True
            elif 'Agahnim' not in itens_sala:
                princesa_resgatada = True

        elif item == "◇":
            quantidade_rupees += 1

        elif item.isnumeric():
            if continuar == True and 'Zelda' not in itens_sala:
              num = int(item)
              rupees, resgatada = percursso_link(mapa, num, possui_espada, salas_percorridas)
              quantidade_rupees += rupees
              if resgatada:
                  princesa_resgatada = True

    return quantidade_rupees, princesa_resgatada

quantidade_salas = int(input())
mapa = []

for c in range(quantidade_salas):
    componentes_sala = input().split(" - ")
    mapa.append(componentes_sala)

sala_inicial = int(input())
salas_visitadas = set()
possui_espada = False

qtd_rupees, resgatada = percursso_link(mapa, sala_inicial, possui_espada, salas_visitadas)

if resgatada:
    print(f'A princesa Zelda está a salvo e ainda conseguimos coletar {qtd_rupees} rupees')
else:
    print(f'Infelizmente a princesa ainda corre perigo, mas temos {qtd_rupees} rupees para nos ajudar nas buscas')
