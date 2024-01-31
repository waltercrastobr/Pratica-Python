def distancia_formula(ponto_1, ponto_2):
    x1, y1 = ponto_1
    x2, y2 = ponto_2
    
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def astronauta_sobrevive(posicao_astronauta, posicao_explosao, raio_impacto):
    distancia = distancia_formula(posicao_astronauta, posicao_explosao)
    
    return distancia > raio_impacto

def encontrar_ponto_central(astronautas):
    num_astronautas = len(astronautas)
    if num_astronautas == 0:
        return None
        
    soma_x = 0
    soma_y = 0
    
    for astronauta in astronautas:
        soma_x += astronauta[0]
        soma_y += astronauta[1]
        
    return [soma_x / num_astronautas, soma_y / num_astronautas]

def resgatar_astronautas(capsulas, posicao_explosao, raio_impacto):
    sobreviventes_totais = 0
    pontos_centrais = []

    for capsula in capsulas:
        sobreviventes = []
        for astronauta in capsula:
            if astronauta_sobrevive(astronauta, posicao_explosao, raio_impacto):
                sobreviventes.append(astronauta)
                
        sobreviventes_totais += len(sobreviventes)
        ponto_central = encontrar_ponto_central(sobreviventes)
        if ponto_central:
            pontos_centrais.append(ponto_central)

    return [sobreviventes_totais, pontos_centrais]


capsulas_str = input()
posicao_explosao_str = input()
raio_impacto = int(input())

capsulas_lista = eval(capsulas_str)
posicao_explosao_lista = eval(posicao_explosao_str)

resultado = resgatar_astronautas(capsulas_lista, posicao_explosao_lista, raio_impacto)
print(resultado)
