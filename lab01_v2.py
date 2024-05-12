escolha_she= input()
escolha_reg = input()

#lista com as regras do jogo:
regras = [{"tesoura":["papel", "lagarto"]}, {"papel":["pedra", "spock"]}, 
        {"pedra":["lagarto", "tesoura"]}, {"lagarto":["spock", "papel"]}, 
        {"spock":["tesoura", "pedra"]}]

if escolha_she == escolha_reg:
    print("empate")
else:
    for item in regras:
        if escolha_she in item:
            if escolha_reg in item[escolha_she]:
                print("Interestelar")
            else:
                print("Jornada nas Estrelas")