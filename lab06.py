from typing import Any


def verifica_len_0(v1: list[int], v2: list[int]) -> None:
    while len(v1) > len(v2):
        v2.append(0)

    while len(v2) > len(v1):
        v1.append(0)


def verifica_len_1(v1: list[int], v2: list[int]) -> None:
    while len(v1) > len(v2):
        v2.append(1)

    while len(v2) > len(v1):
        v1.append(1)


def soma_vetores(v1: list[int], v2: list[int]) -> list[int]:
    verifica_len_0(v1, v2)

    for i in range(len(v1)):
        v1[i] += v2[i]
    return v1


def subtrai_vetores(v1: list[int], v2: list[int]) -> list[int]:
    verifica_len_0(v1, v2)

    for i in range(len(v1)):
        v1[i] -= v2[i]
    return v1


def multiplica_vetores(v1: list[int], v2: list[int]) -> list[int]:
    verifica_len_1(v1, v2)

    for i in range(len(v1)):
        v1[i] *= v2[i]
    return v1


def divide_vetores(v1: list[int], v2: list[int]) -> list[int]:
    while len(v2) > len(v1):
        v1.append(0)
    while len(v1) > len(v2):
        v2.append(1)

    for i in range(len(v1)):
        v1[i] //= v2[i]
    return v1


def multiplicacao_escalar(v1: list[int], n: int) -> list[int]:
    for i in range(len(v1)):
        v1[i] *= n
    return v1


def n_duplicacao(v1: list[int], n: int) -> list[int]:
    if n == 0:
        v1 = []
        return v1
    else:
        v1[:] *= n
        return v1


def soma_elementos(v1: list[int]) -> int:
    soma = 0
    for x in v1:
        soma += x
    v1.clear()
    v1.append(soma)
    return soma


def produto_interno(v1: list[int], v2: list[int]) -> int:
    multiplica_vetores(v1, v2)
    return soma_elementos(v1)


def multiplica_todos(v1: list[int], v2: list[int]) -> list[int]:
    for i in range(len(v1)):
        aux = 0
        for j in v2:
            aux += v1[i] * j
        v1[i] = aux
    return v1


def correlacao_cruzada(v1: list[int], m: list[int]) -> list[int]:
    for i in range(len(v1) - len(m) + 1):
        soma = 0
        for j in range(len(m)):
            soma += v1[i+j] * m[j]
        v1[i] = soma
    del v1[len(v1) - len(m) + 1:]
    return v1


def main() -> Any:
    v1 = list(map(int, input().split(',')))
    comando = input()

    while comando != 'fim':
        if comando == 'soma_vetores':
            v2 = list(map(int, input().split(',')))
            print(soma_vetores(v1, v2))

        elif comando == 'subtrai_vetores':
            v2 = list(map(int, input().split(',')))
            print(subtrai_vetores(v1, v2))

        elif comando == 'multiplica_vetores':
            v2 = list(map(int, input().split(',')))
            print(multiplica_vetores(v1, v2))

        elif comando == 'divide_vetores':
            v2 = list(map(int, input().split(',')))
            print(divide_vetores(v1, v2))

        elif comando == 'multiplicacao_escalar':
            n = int(input())
            print(multiplicacao_escalar(v1, n))

        elif comando == 'n_duplicacao':
            n = int(input())
            print(n_duplicacao(v1, n))

        elif comando == 'soma_elementos':
            print('[{}]'.format(soma_elementos(v1)))

        elif comando == 'produto_interno':
            v2 = list(map(int, input().split(',')))
            print('[{}]'.format(produto_interno(v1, v2)))

        elif comando == 'multiplica_todos':
            v2 = list(map(int, input().split(',')))
            print(multiplica_todos(v1, v2))

        elif comando == 'correlacao_cruzada':
            m = list(map(int, input().split(',')))
            print(correlacao_cruzada(v1, m))

        comando = input()


if __name__ == "__main__":
    main()
