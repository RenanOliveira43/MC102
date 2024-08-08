# finalizar 
def scan_ambiente(comodo):
    linha = len(comodo)
    coluna = len(comodo[0])
    imprime(comodo)
    
    for i in range(linha):
        if i % 2 == 0:
            for j in range(coluna):
                if comodo[i][j] == '.':
                    comodo[i][j] = 'r'
                    imprime(comodo)

                if comodo[i][j] == 'r':
                    comodo[i][j] = '.'

                if comodo[i][j] == 'o':
                    comodo[i][j] = 'r'
                    imprime(comodo)
                    comodo[i][j] = '.'
        else:
            for j in range(coluna - 1, -1, -1):
                if comodo[i][j] == '.':
                    comodo[i][j] = 'r'
                    imprime(comodo)

                if comodo[i][j] == 'r':
                    comodo[i][j] = '.'

                if comodo[i][j] == 'o':
                    comodo[i][j] = 'r'
                    imprime(comodo)
                    comodo[i][j] = '.'


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
