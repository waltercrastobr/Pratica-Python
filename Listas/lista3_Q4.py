desejo = input()
cont_arara = 0
lista_final = []
continuar = True

if desejo == 'Meninas, acho que já falei demais. Vamos para o shopping?':
    continuar = False
else:
    while desejo == 'Explorar arara':
        print(f'Arara {cont_arara}:')
        cont_arara += 1
        lista_profissoes = input().split(', ')
        lista_barbie = input().split(', ')
        lista_possui = []

        if len(lista_profissoes) != len(lista_barbie):
            print('Hmm, estranho! Acho que a Barbie se confundiu na organização e nas lembranças!')
        else:
            for profissao in lista_profissoes:
                if profissao in lista_barbie:
                    lista_possui.append(profissao)
            if len(lista_possui) == len(lista_profissoes):
                print('Boa, Barbie! Não bagunçou nada, pode contar todas as suas histórias!')
            if len(lista_profissoes) == len(lista_barbie) and len(lista_profissoes) != len(lista_possui):
                for item in lista_profissoes:
                    if item not in lista_possui:
                        lista_final.append(item)
                out = ', '.join(lista_final)
                print(f'Poxa, Barbie! Você acabou desorganizando essa arara, e {len(lista_profissoes) - len(lista_possui)} profissões vão ficar de fora da conversa. São elas: {out}.')

        desejo = input()
        lista_final.clear()