def reverter(lista, i, j):
    i = min(i, len(lista)-1)
    j = min(j, len(lista)-1)
    if i >= len(lista) or i >= j:
        return lista
    lista[i:j+1] = lista[i:j+1][::-1]
    return lista


def transpor(lista, i, j, k):
    i = min(i, len(lista)-1)
    j = min(j, len(lista)-1)
    k = min(k, len(lista)-1)
    if i >= len(lista) or j >= len(lista):
        return lista
    sequencia1 = lista[i:j+1]
    sequencia2 = lista[j+1:k+1]
    lista[i:j+1] = sequencia2
    lista[j+1:k+1] = sequencia1
    return lista


def concatenar(lista, g):
    g = list(g)
    lista.extend(g)
    return lista


def combinar(lista, g, j):
    for letras in g:
        lista.insert(j, letras)
        j += 1
    return lista


def remover(lista, i, j):
    i = min(i, len(lista)-1)
    j = min(j, len(lista)-1)
    if i >= len(lista) or i > j:
        return lista
    del lista[i:j+1]
    return lista


def transpor_e_reverter(lista, i, j, k):
    i = min(i, len(lista)-1)
    j = min(j, len(lista)-1)
    k = min(k, len(lista)-1)
    if i >= len(lista) or j >= len(lista):
        return lista
    transpor(lista, i, j, k)
    reverter(lista, i, k)
    return lista


def buscar(lista, g):
    string = ""
    for i in lista:
        string += i

    lista_unica = string
    return print(lista_unica.count(g))


def buscar_bidirecional(lista, g):
    count = 0
    for i in range(len(lista)-len(g)+1):
        if lista[i:i+len(g)] == list(g):
            count += 1
        if lista[i:i+len(g)] == list(g[::-1]):
            count += 1
    return print(count)


def mostrar(lista):
    return print(*lista, sep='')


def converte_int(lista):
    for i in range(1, len(lista)):
        lista[i] = int(lista[i])
    return lista

def main():
    genoma = list(input())
    comando = list(input().split())

    while comando[0] != 'sair':
        if comando[0] == 'reverter':
            converte_int(comando)
            reverter(genoma, comando[1], comando[2])

        elif comando[0] == 'transpor':
            converte_int(comando)
            transpor(genoma, comando[1], comando[2], comando[3])

        elif comando[0] == 'concatenar':
            concatenar(genoma, comando[1])

        elif comando[0] == 'combinar':
            comando[2] = int(comando[2])
            combinar(genoma, comando[1], comando[2])

        elif comando[0] == 'remover':
            converte_int(comando)
            remover(genoma, comando[1], comando[2])

        elif comando[0] == 'transpor_e_reverter':
            converte_int(comando)
            transpor_e_reverter(genoma, comando[1], comando[2], comando[3])

        elif comando[0] == 'buscar':
            buscar(genoma, comando[1])

        elif comando[0] == 'buscar_bidirecional':
            buscar_bidirecional(genoma, comando[1])

        elif comando[0] == 'mostrar':
            mostrar(genoma)

        comando = list(input().split())


if __name__ == "__main__":
    main()
