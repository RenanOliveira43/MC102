def calcula_chave(operador, operando1, operando2, string):
    if operando1 == 'numero':
        index1 = 0
        for i in enumerate(string):
            if string.isdigit():
                index1 = i
                break
            index2 = string.find(operando2, index1 + len(operando1))
    elif operando2 == 'numero':
        index2 = 0
        for i in enumerate(string):
            if string.isdigit():
                index2 = i
                break
            index1 = string.find(operando1)
    else:
        index1 = string.find(operando1)
        index2 = string.find(operando2, index1 + len(operando1))

    if operador == '+':
        chave = index1 + index2
        return chave

    elif operador == '-':
        chave = index1 - index2
        return chave

    elif operador == '*':
        chave = index1 * index2
        return chave


def main():
    operador = input()
    operando1 = input()
    operando2 = input()
    n_linhas = int(input())

    for i in range(n_linhas):
        mensagem = input()

    print(calcula_chave(operador, operando1, operando2, mensagem))


if __name__ == "__main__":
    main()
