def acha_ganhador(dicionario):
    maior_media = 0

    for filme, notas in dicionario.items():
        media = sum(notas) / len(notas)
        
        if media > maior_media:
            maior_media = media
            ganhador = filme
        if media == maior_media:
            ganhador = filme
    
    return ganhador
   

def categoria_especial_1(dicionario):
    filmes_media = {}

    for categoria, filmes in dicionario.items():
        for filme, notas in filmes.items():
            media = sum(notas) / len(notas)
            if filme in filmes_media:
                filmes_media[filme].append(media)
            else:
                filmes_media[filme] = [media]
    
    return acha_ganhador(filmes_media)
    

def categoria_especial_2(dicionario, lista):
    filme_sem_avaliacao = []
    lista_aux = []
    for categoria, lista_filmes in dicionario.items():
        for filme in lista:
            if filme in lista_filmes:
                lista_aux.append(filme)
    
    for x in lista:
        if x not in lista_aux:
            filme_sem_avaliacao.append(x)
    
    if len(filme_sem_avaliacao) == 0:
        return ['sem ganhadores']
    else:
        return filme_sem_avaliacao


def main():
    categorias = {
        'filme que causou mais bocejos': {},
        'filme que foi mais pausado': {},
        'filme que mais revirou olhos': {},
        'filme que não gerou discussão nas redes sociais': {},
        'enredo mais sem noção': {}
    }

    qtd_indicados = int(input())
    
    filmes_indicados = []
    for j in range(qtd_indicados):
        filmes_indicados.append(input())

    qtd_avaliacoes = int(input())
    avaliacao = [] 

    for i in range(qtd_avaliacoes):
        avaliacao.append(input().split(', '))
        filme = avaliacao[i][2]
        nota = int(avaliacao[i][3])

        if filme in categorias[avaliacao[i][1]]:
            categorias[avaliacao[i][1]][filme].append(nota)
        else:
            categorias[avaliacao[i][1]][filme] = [nota]
    
    print('#### abacaxi de ouro ####\n')
    print('categorias simples')
    print('categoria: filme que causou mais bocejos')
    print('-', acha_ganhador(categorias['filme que causou mais bocejos']))
    print('categoria: filme que foi mais pausado')
    print('-', acha_ganhador(categorias['filme que foi mais pausado']))
    print('categoria: filme que mais revirou olhos')
    print('-', acha_ganhador(categorias['filme que mais revirou olhos']))
    print('categoria: filme que não gerou discussão nas redes sociais')
    print('-', acha_ganhador(categorias['filme que não gerou discussão nas redes sociais']))
    print('categoria: enredo mais sem noção')
    print('-', acha_ganhador(categorias['enredo mais sem noção']))
    print('\ncategorias especiais')
    print('prêmio pior filme do ano')
    pior_filme = categoria_especial_1(categorias)
    print('-', pior_filme)
    print('prêmio não merecia estar aqui')
    resultado = categoria_especial_2(categorias, filmes_indicados)
    print('-', ', '.join(map(str, resultado)))


if __name__ == "__main__":
    main()
