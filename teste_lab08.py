def acha_maior(dicionario):
    return max(dicionario, key=dicionario.get)


def main():

    categorias = {
        'filme_que_causou_mais_bocejos': [],
        'filme_que_foi_mais_pausado': [],
        'filme_que_mais_revirou_olhos': [],
        'filme_que_não_gerou_discussão_nas_redes_sociais': [],
        'enredo_mais_sem_noção': []
    }

    qtd_indicados = int(input())
    filmes = []
    for i in range(qtd_indicados):
        filmes.append(input())

    qtd_avaliacoes = int(input())
    avaliacoes = []

    for i in range(qtd_avaliacoes):
        avaliacoes.append(input().split(', '))
        filme = avaliacoes[i][2]
        nota = int(avaliacoes[i][-1])
        
        if avaliacoes[i][1] == 'filme que causou mais bocejos':
            categorias['filme_que_causou_mais_bocejos'] = ((filme, nota))
        elif avaliacoes[i][1] == 'filme que foi mais pausado':
            categorias['filme_que_foi_mais_pausado'].append((filme, nota))
        elif avaliacoes[i][1] == 'filme que mais revirou olhos':
            categorias['filme_que_mais_revirou_olhos'].append((filme, nota))
        elif avaliacoes[i][1] == 'filme que não gerou discussão nas redes sociais':
            categorias['filme_que_não_gerou_discussão_nas_redes_sociais'].append((filme, nota))
        elif avaliacoes[i][1] == 'enredo mais sem noção':
            categorias['enredo_mais_sem_noção'].append((filme, nota))
    
    # print('\n#### abacaxi de ouro ####\n')
    # print('categorias simples')
    # print('categoria: filme que causou mais bocejos')
    # print('-', acha_maior(categorias['filme_que_causou_mais_bocejos']))
    # print('categoria: filme que foi mais pausado')
    # print('-', acha_maior(categorias['filme_que_foi_mais_pausado']))
    # print('categoria: filme que mais revirou olhos')
    # print('-', acha_maior(categorias['filme_que_mais_revirou_olhos']))
    # print('categoria: filme que não gerou discussão nas redes sociais')
    # print('-', acha_maior(categorias['filme_que_não_gerou_discussão_nas_redes_sociais']))
    # print('categoria: enredo mais sem noção')
    # print('-', acha_maior(categorias['enredo_mais_sem_noção']),'\n')
    print(categorias)



if __name__ == "__main__":
    main()
