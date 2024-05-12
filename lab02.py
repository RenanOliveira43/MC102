print('Este é um sistema que irá te ajudar a escolher a sua próxima Distribuição Linux. Responda a algumas poucas perguntas para ter uma recomendação.')
print('Seu SO anterior era Linux?')
print('(0) Não')
print('(1) Sim')
entrada1 = input()
if entrada1 == '0':
    print('Seu SO anterior era um MacOS?')
    print('(0) Não')
    print('(1) Sim')
    entrada2 = input()
    if entrada2 == '0':
        print('Você passará pelo caminho daqueles que decidiram abandonar sua zona de conforto, as distribuições recomendadas são: Ubuntu Mate, Ubuntu Mint, Kubuntu, Manjaro.')
    elif entrada2 == '1':
        print('Você passará pelo caminho daqueles que decidiram abandonar sua zona de conforto, as distribuições recomendadas são: ElementaryOS, ApricityOS.')
    else:
        print('Opção inválida, recomece o questionário.')
elif entrada1 == '1':
    print('É programador/ desenvolvedor ou de áreas semelhantes?')
    print('(0) Não')
    print('(1) Sim')
    print('(2) Sim, realizo testes e invasão de sistemas')
    entrada3 = input()
    if entrada3 == '0':
        print('Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são: Ubuntu Mint, Fedora.')
    elif entrada3 == '1':
        print('Gostaria de algo pronto para uso ao invés de ficar configurando o SO?')
        print('(0) Não')
        print('(1) Sim')
        entrada4 = input()
        if entrada4 == '0':
            print('Já utilizou Arch Linux?')
            print('(0) Não')
            print('(1) Sim')
            entrada5 = input()
            if entrada5 == '0':
                print('Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são: Antergos, Arch Linux.')
            elif entrada5 == '1':
                print('Suas escolhas te levaram a um caminho repleto de desafios, para você recomendamos as distribuições: Gentoo, CentOS, Slackware.')
            else:
                print('Opção inválida, recomece o questionário.')
        elif entrada4 == '1':
            print('Já utilizou Debian ou Ubuntu?')
            print('(0) Não')
            print('(1) Sim')
            entrada6 = input()
            if entrada6 == '0':
                print('Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são: OpenSuse, Ubuntu Mint, Ubuntu Mate, Ubuntu.')
            elif entrada6 == '1':
                print('Suas escolhas te levaram a um caminho repleto de desafios, para você recomendamos as distribuições: Manjaro, ApricityOS.')
            else:
                print('Opção inválida, recomece o questionário.')
        else:
            print('Opção inválida, recomece o questionário.')
    elif entrada3 == '2':
        print('Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são: Kali Linux, Black Arch.')
    else:
        print('Opção inválida, recomece o questionário.')
else:
    print('Opção inválida, recomece o questionário.')