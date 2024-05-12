dia = int(input())

for i in range(dia):
    qtd_brigam = int(input())

    pares_brigam = []
    for j in range(qtd_brigam):
        pares_brigam.append(input().split())

    proced_disponivel = input().split()
    
    for h in range(1, len(proced_disponivel), 2):
        proced_disponivel[h] = int(proced_disponivel[h])

    qtd_animais = int(input())

    proced_animal = []
    for k in range(qtd_animais):
        proced_animal.append(input().split())

    print('Dia:', i + 1)
    
    # verifica se houve brigas e contabiliza 
    brigas = 0

    for x in pares_brigam:
        for animal in proced_animal:
            if x[0] == animal[0]:
                for animal in proced_animal:
                    if x[1] == animal[0]:
                        brigas += 1

    
    print('Brigas:', brigas)

    #verifica se e quais animais foram atendidos
    animais_atendidos = []
    animais_nao_atendidos = []
    proced_nao_disponivel = []
    
    for animal in proced_animal:
        for l in range(0, len(proced_disponivel), 2):
            if animal[1] == proced_disponivel[l]:
                proced_disponivel[l + 1] -= 1

                if proced_disponivel[l + 1] >= 0:
                    animais_atendidos.append(animal[0])

                if proced_disponivel[l + 1] < 0:
                    animais_nao_atendidos.append(animal[0])

        if animal[1] not in proced_disponivel:
            proced_nao_disponivel.append(animal[0])


    if len(animais_atendidos) > 0:
        print('Animais atendidos:', end=" ")
        print(*animais_atendidos, sep=", ") 

    if len(animais_nao_atendidos) > 0:
        print('Animais não atendidos:', end=" ")
        print(*animais_nao_atendidos, sep=", ")

    if len(proced_nao_disponivel) > 0:
        for animal in range(len(proced_nao_disponivel)):
            print('Animal %s solicitou procedimento não disponível.' % proced_nao_disponivel[animal])
    
    print()