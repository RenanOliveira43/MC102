escolha_she = input()
escolha_reg = input()

if escolha_she == 'pedra':
    if escolha_reg == 'lagarto' or escolha_reg == 'tesoura':
        print('Interestelar')
    elif escolha_she == escolha_reg:
        print('empate')
    else:
        print('Jornada nas Estrelas')

if escolha_she == 'papel':
    if escolha_reg == 'pedra' or escolha_reg == 'spock':
        print('Interestelar')
    elif escolha_she == escolha_reg:
        print('empate')
    else:
        print('Jornada nas Estrelas')

if escolha_she == 'tesoura':
    if escolha_reg == 'papel' or escolha_reg == 'lagarto':
        print('Interestelar')
    elif escolha_she == escolha_reg:
        print('empate')
    else:
        print('Jornada nas Estrelas')

if escolha_she == 'lagarto':
    if escolha_reg == 'spock' or escolha_reg == 'papel':
        print('Interestelar')
    elif escolha_she == escolha_reg:
        print('empate')
    else:
        print('Jornada nas Estrelas')

if escolha_she == 'spock':
    if escolha_reg == 'tesoura' or escolha_reg == 'pedra':
        print('Interestelar')
    elif escolha_she == escolha_reg:
        print('empate')
    else:
        print('Jornada nas Estrelas')