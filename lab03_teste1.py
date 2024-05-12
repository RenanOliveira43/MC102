num_jogadores = int(input())
num_retirados = list(map(int, input().split()))
intervalo = list(map(int, input().split()))

grupo1 = num_jogadores // 2 + num_jogadores % 2
grupo2 = num_jogadores // 2

j = 1
pontos = []
for i in range(grupo1):
    pontos.append((intervalo[j] - intervalo[i]) * num_retirados[i])
    j += 2
l = 2
for k in range(grupo2):
    pontos.append((intervalo[l] - intervalo[k]) + num_retirados[l])
    l += 2

print(grupo1)
print(grupo2)
print(pontos)
if pontos.count(max(pontos)) > 1:
    print("Rodada de cerveja para todos os jogadores!")
else:
    vencedor = pontos.index(max(pontos)) + 1
    print("O jogador número %s vai receber o melhor bolo da cidade pois venceu com %s ponto(s)!" % (vencedor, max(pontos)))