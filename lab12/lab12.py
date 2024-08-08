# finalizar

def bubble_sort(dicionario):
    valores_cartas = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                      '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'O': 14, 'E': 15, 'C': 16, 'P': 17
                      }

    keys = list(dicionario.keys())
    n = len(keys)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            parte1_carta = tuple(dicionario[keys[j]])
            parte2_carta = tuple(dicionario[keys[j + 1]])

            valor1 = valores_cartas[parte1_carta[0]]
            valor2 = valores_cartas[parte2_carta[0]]
            
            if valor1 > valor2:
                keys[j], keys[j + 1] = keys[j + 1], keys[j]

    sorted_dict = {}
    for key in keys:
        sorted_dict[key] = dicionario[key]

    return sorted_dict


def main():
    mao_jogadores = {}
    num_jogadores = int(input())
    
    for i in range(num_jogadores):
        cartas_jogadores = input().split(', ')
        mao_jogadores[i + 1] = cartas_jogadores

    # jogadas_duvido = int(input())
    # print(ordenar_cartas(mao_jogadores))
    print(bubble_sort(mao_jogadores))



if __name__ == "__main__":
    main()