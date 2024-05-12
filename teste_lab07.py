def calcula_chave(operador, operando1, operando2, string):
    if operando1 == 'vogal':
        operando1 = acha_vogal(string)
    elif operando2 == 'vogal':
        operando2 = acha_vogal(string)

    if operando1 == 'numero':
        operando1 = acha_numero(string)
    elif operando2 == 'numero':
        operando2 = acha_numero(string)

    index1 = string.find(operando1)
    index2 = string.find(operando2, index1 + 1)

    if operador == '+':
        chave = index1 + index2
        return chave

    elif operador == '-':
        chave = index1 - index2
        return chave

    elif operador == '*':
        chave = index1 * index2
        return chave


def acha_vogal(string):
    vogais = 'AaEeIiOoUu'
    for letra in string:
        if letra in vogais:
            return letra


def acha_consoante(string):
    vogais = 'AaEeIiOoUu'
    for letra in string:
        if letra not in vogais:
            return letra


def acha_numero(string):
    numeros = '(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)'
    for digito in string:
        if digito in numeros:
            return digito


def transforma_em_ASCII(string):
    valores_ASCII = []
    for i in string:
        valores_ASCII.append(ord(i))
    return valores_ASCII


def transforma_em_string(valores_ASCII):
    mensagem_string = ''
    for i in valores_ASCII:
        mensagem_string += chr(i)
    return mensagem_string


def descript_mensagem(operador, string, chave):
    valores_ASCII = transforma_em_ASCII(string)
    discripted = []
    while discripted[i] >= 32 and discripted[i] <= 126:
        if operador == '+':
            for i in valores_ASCII:
                discripted.append(i + chave)
        elif operador == '-':
            for i in valores_ASCII:
                discripted.append(i - chave)
        elif operador == '*':
            for i in valores_ASCII:
                discripted.append(i * chave)

    return transforma_em_string(discripted)


def main():
    operador = input()
    operando1 = input()
    operando2 = input()
    n_linhas = int(input())

    for i in range(n_linhas):
        mensagem = input()

    chave = calcula_chave(operador, operando1, operando2, mensagem)
    print(chave)
    print(descript_mensagem(operador, mensagem, chave))


if __name__ == "__main__":
    main()
