local_esconderijo = str(input()).lower()
local_procurar = str(input()).lower()

if local_esconderijo != local_procurar:
    print('Carambolas, ele não está aqui. Ele continua se divertindo!')
    local_procurar_2 = str(input()).lower()
    if local_esconderijo != local_procurar_2:
        print('Carambolas, ele não está aqui. Ele continua se divertindo!')
        local_procurar_3 = str(input()).lower()
        if local_esconderijo != local_procurar_3:
            print('Carambolas, ele não está aqui. Ele continua se divertindo!')
            print('AAAAAAAH, ele escapou de vez!')
        elif local_esconderijo == local_procurar_3:
            print('Ahá, te encontrei e é o fim das suas férias!')
    elif local_esconderijo == local_procurar_2:
        print('Ahá, te encontrei e é o fim das suas férias!')

elif local_esconderijo == local_procurar:
    print('Ahá, te encontrei e é o fim das suas férias!')
    