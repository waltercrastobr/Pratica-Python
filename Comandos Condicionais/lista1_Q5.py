c1 = str(input())
c2 = str(input())

nome = str(input())

hab = str(input())

n1 = int(input())
n2 = int(input())
n3 = int(input())
media = int((n1 + n2 + n3) / 3)

if (c1 == ('Humildade') and c2 == ('Bondade')) and (nome == ('Mary') or nome == ('Ninguem')) and (hab == ('Dancar') or hab == ('Lancar')) and media >= 7:
    print('Siga em frente, olhe para o lado. Bem-vindo ao aranhaverso, Miranha Furacao!')

elif (c1 != ('Humildade')) or (c2 != ('Bondade')):
    print('Ops, parece que não foi dessa vez, Miranha. Você terá que continuar na Carreta Furacao mesmo!')
    print('Infelizmente você não possui as característica necessárias!')

elif (nome != ('Ninguem')) and (nome != ('Mary')):
    print('Ops, parece que não foi dessa vez, Miranha. Você terá que continuar na Carreta Furacao mesmo!')
    print('Infelizmente você não está apaixonado pela pessoa certa!')

elif (hab != ('Dancar')) and (hab != ('Lancar')):
    print('Ops, parece que não foi dessa vez, Miranha. Você terá que continuar na Carreta Furacao mesmo!')
    print('Infelizmente você não possui as habilidades necessárias!')

elif media < 7:
    print('Ops, parece que não foi dessa vez, Miranha. Você terá que continuar na Carreta Furacao mesmo!')
    print('Infelizmente você não obteve um bom desempenho escolar!')
            
        
        
