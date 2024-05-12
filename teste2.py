def scan_ambiente(comodo):
    linha = len(comodo)
    coluna = len(comodo[0])
    pos_inicial = (0, 0)
    retorna_scan = False  
    imprime(comodo)
    
    while True:
        i, j = pos_inicial
        if comodo[i][j] == '.':
            comodo[i][j] = 'r'
            imprime(comodo)

        if comodo[i][j] == 'r':
            comodo[i][j] = '.'

        if comodo[i][j] == 'o':
            comodo[i][j] = 'r'
            imprime(comodo)
            comodo[i][j] = '.'
        
        if retorna_scan:
            return 

        pos_adjacente = [(i, j - 1), (i - 1, j), (i, j + 1), (i + 1, j)]
        
        for adj_i, adj_j in pos_adjacente:
            if 0 <= adj_i < linha and 0 <= adj_j < coluna and comodo[adj_i][adj_j] == 'o':
                retorna_scan = False
                pos_inicial = (adj_i, adj_j)
                break
        else:
            if i % 2 == 0:
                if j < coluna - 1:
                    pos_inicial = (i, j + 1)
                else:
                    retorna_scan = True
            else:
                if j > 0:
                    pos_inicial = (i, j - 1)
                else:
                    retorna_scan = True


def imprime(comodo):
    for linha in comodo:
        for i in range(len(linha) - 1):
            print(linha[i], end=" ")
        print(linha[-1])


def main():
    comodo = []
    num_linhas = int(input())
    
    for i in range(num_linhas):
        linhas = input().split()
        comodo.append(linhas)

    scan_ambiente(comodo)


if __name__ == "__main__":
    main()
