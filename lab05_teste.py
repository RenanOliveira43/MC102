
"""""
def transpor(lista, i, j, k):
    sequencia1 = lista[i:j+1]
    sequencia2 = lista[j+1:k+1]
    lista[i:j+1] = sequencia2
    lista[j+1:k+1] = sequencia1
    return lista

def reverter(lista, i, j): # funciona 
    lista[i:j+1] = lista[i:j+1][::-1] 
    return lista

def transpor_e_reverter(lista, i, j, k):
    transpor(lista, i, j, k)
    reverter(lista, i, k)
    return lista

def buscar(lista, g): #arrumar
    string = ""
    for i in lista:
        string += i
    lista_unica = string

    qtd_repetições = lista_unica.count(g)
    return qtd_repetições


def reverter(lista, i, j): # funciona 
    lista[i:j+1] = lista[i:j+1][::-1] 
    return lista

def buscar_bidirecional(lista, g):
    count = 0
    for i in g:
        count += lista.count(i)

    g_invertido = g[::-1]
    for i in g_invertido:
        count += lista.count(i)

    return count



genoma = list(input())
print(buscar_bidirecional(genoma, 'AG'))
#ATCGTAGTG



def buscar_bidirecional(lista, g):  # arrumar
    g = list(g)
    for i in g:
        lista.count(i)
    return print(lista.count(i))



#CTCGTAAGCTGA
#CTAGCTCGTAGA
#print(transpor(genoma, 2, 5, 9))
#print(combinar(genoma, 'CTAG', 3))
#print(concatenar(genoma, 'TG'))
#print(remover(genoma, 2, 4))
#print(buscar(genoma, 'TCGA'))


    def transpor(lista, i, j, k): # arrumar
    lista[i:j+1] = lista[i:j+1][j:k+1]
    lista[j:k+1] = lista[j:k+1][i:j+1] 
    return lista


"""
def reverter(lista, i, j):
    lista[i:j+1] = lista[i:j+1][::-1]
    return lista


def transpor(lista, i, j, k):
    seguencia1 = lista[i:j+1]
    sequencia2 = lista[j+1:k+1]
    lista[i:k+1] = sequencia2 + seguencia1
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
    if i > len(lista):
        return lista
    else:
        del lista[i:j+1]
        return lista


def transpor_e_reverter(lista, i, j, k):
    transpor(lista, i, j, k)
    reverter(lista, i, k)
    return lista


def buscar(lista, g):
    unificado = ""
    for i in lista:
        unificado += i
    lista_unificada = unificado
    return lista_unificada.count(g)


def buscar_bidirecional(lista, g):
    return buscar(lista, g) + buscar(reverter(lista, 0, len(lista)), g) 


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
            print(buscar(genoma, comando[1]))

        elif comando[0] == 'buscar_bidirecional':
            print(buscar_bidirecional(genoma, comando[1]))

        elif comando[0] == 'mostrar':
            mostrar(genoma)

        comando = list(input().split())


if __name__ == "__main__":
    main()

"""
def buscar(lista, g):
    unificado = ""
    for i in lista:
        unificado += i
    lista_unificada = unificado
    return print(lista_unificada.count(g))

def busca_bidirecional(lista, g):
    g_invertido = g[::-1]
    return print(buscar(lista, g) + buscar(lista, g_invertido))



def buscar_bidirecional(lista, g):
    z = buscar(lista, g)
    y = buscar(reverter(0, len(lista)), g)
    return z + y

"""



def buscar_bidirecional(lista, g):
    count = 0
    for i in range(len(lista)):
        if lista[i:i+len(g)] == list(g):
            count += 1
        if lista[i:i+len(g)] == list(g[::-1]):
            count += 1
    return print(count)





















