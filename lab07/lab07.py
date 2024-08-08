def calcula_chave(operador, operando1, operando2, string):
    if operando1 == 'vogal':
        operando1 = acha_vogal(string)
    elif operando2 == 'vogal':
        operando2 = acha_vogal(string)

    if operando1 == 'numero':
        operando1 = acha_numero(string)
    elif operando2 == 'numero':
        operando2 = acha_numero(string)

    if operando1 == 'consoante':
        operando1 = acha_consoante(string)
    elif operando2 == 'consoante':
        operando2 = acha_consoante(string)

    indice1 = string.find(operando1)
    indice2 = string.find(operando2, indice1)

    if operador == '+':
        chave = indice1 + indice2
    elif operador == '-':
        chave = indice1 - indice2
    elif operador == '*':
        chave = indice1 * indice2

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


def acha_numero(lista):
    numeros = '0123456789'
    for digito in lista:
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


def descripta_mensagem(string, chave):
    valores_ASCII = transforma_em_ASCII(string)
    discripted = []
    for i in valores_ASCII:
        if i == 10:
            discripted.append(10)
        else:
            soma_chave = i + chave
            while soma_chave < 32:
                soma_chave += 95
            while soma_chave > 126:
                soma_chave -= 95
            discripted.append(soma_chave)

    return transforma_em_string(discripted)


def main():
    operador = input()
    operando1 = input()
    operando2 = input()
    n_linhas = int(input())

    mensagem = ''
    mensagem_espaco = ''

    for i in range(n_linhas):
        entrada = input()
        mensagem_espaco += entrada + '\n'
        mensagem += entrada

    chave = calcula_chave(operador, operando1, operando2, mensagem)
    print(chave)
    print(descripta_mensagem(mensagem_espaco, chave))


if __name__ == "__main__":
    main()
