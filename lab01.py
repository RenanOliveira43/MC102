escolha_she = input()
escolha_reg = input()

if escolha_she == escolha_reg:
    print('empate')
elif escolha_she == 'pedra':
    if escolha_reg == 'lagarto' or escolha_reg == 'tesoura':
        print('Interestelar')
    else:
        print('Jornada nas Estrelas')
elif escolha_she == 'papel':
    if escolha_reg == 'pedra' or escolha_reg == 'spock':
        print('Interestelar')
    else:
        print('Jornada nas Estrelas')
elif escolha_she == 'tesoura':
    if escolha_reg == 'papel' or escolha_reg == 'lagarto':
        print('Interestelar')
    else:
        print('Jornada nas Estrelas')
elif escolha_she == 'lagarto':
    if escolha_reg == 'spock' or escolha_reg == 'papel':
        print('Interestelar')
    else:
        print('Jornada nas Estrelas')
elif escolha_she == 'spock':
    if escolha_reg == 'tesoura' or escolha_reg == 'pedra':
        print('Interestelar')
    else:
        print('Jornada nas Estrelas')