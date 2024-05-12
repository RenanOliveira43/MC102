num_jogadores = int(input())
num_retirados = list(map(int, input().split()))
intervalo = list(map(int, input().split()))

grupo1 = num_jogadores // 2 + num_jogadores % 2
grupo2 = num_jogadores // 2

pontos = []
j = 1
i = 0
p = 0
m = 0
while i < grupo1:
    pontos.append((intervalo[j] - intervalo[m]) * num_retirados[p])
    j += 2
    i += 1
    m += 2
    p += 1

l = 1
k = 0
m = 0
while k < grupo2:
    pontos.append((intervalo[l] - intervalo[m]) + num_retirados[p])
    l += 2
    k += 1
    m += 2
    p += 1

if pontos.count(max(pontos)) > 1:
    print("Rodada de cerveja para todos os jogadores!")
else:
    vencedor = pontos.index(max(pontos)) + 1
    print("O jogador número %i vai receber o melhor bolo da cidade pois venceu com %i ponto(s)!" % (vencedor, max(pontos)))