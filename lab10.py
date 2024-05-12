from math import floor


def distancia_manhattan(cx, cy, fx, fy):
    return abs(cx - fx) + abs(cy - fy)


def calcula_dano(tipo_flecha, fraqueza, dano_max, cx, cy, fx, fy):
    if tipo_flecha == fraqueza or fraqueza == 'todas':
        dano = abs(dano_max - (distancia_manhattan(cx, cy, fx, fy)))
    else:
        dano = abs(dano_max - distancia_manhattan(cx, cy, fx, fy)) // 2

    return dano


def calcular_recuperacao(hp_aloy, hp_aloy_max):
    recuperacao = floor(0.5 * hp_aloy_max)
    
    if hp_aloy + recuperacao > hp_aloy_max:
        recuperacao = hp_aloy
    else:
        recuperacao += hp_aloy
    
    return recuperacao


def main():
    hp_max_aloy = int(input())
    tipos_flecha = list(input().split(' '))
    dicionario_flechas = {}
    num_mosntros = int(input())
    flechas_utilizadas = {}
    partes_maquina = {}
    
    combate = -1
    lista_maquinas_derrotadas = []
    maquinas_derrotadas_total = 0
    hp_aloy = hp_max_aloy
    
    for i in range(0, len(tipos_flecha), 2):
        chave = tipos_flecha[i]
        valor = int(tipos_flecha[i + 1])
        dicionario_flechas[chave] = valor

    while True:
        qtd_maquinas = int(input())
        
        for j in range(qtd_maquinas):
            hp_maquina, pontos_ataque, qtd_partes = map(int, input().split())
            partes_maquina[j] = {'hp_maquina': hp_maquina, 'pontos_ataque': pontos_ataque, 'partes': {}}

            for k in range(qtd_partes):
                parte_corpo, fraqueza, dano_max, cx, cy = input().split(', ')
                dano_max, cx, cy = int(dano_max), int(cx), int(cy)
                partes_maquina[j]['partes'][parte_corpo] = {'fraqueza': fraqueza, 'dano_max': dano_max, 'cx': cx, 'cy': cy}
                partes_maquina[j]['partes'][parte_corpo]['acertos_criticos'] = {'cx': cx, 'cy': cy, 'acertos': 0}
        
        copia_dicionario_flechas = dicionario_flechas.copy()
        maquinas_derrotadas_combate = 0
        flechas_disparadas = 0 
        
        while True:
            alvo, parte_corpo, tipo_flecha, fx, fy = input().split(', ')
            alvo, fx, fy = int(alvo), int(fx), int(fy)
            maquina_atual = partes_maquina[alvo]
            parte_atual = maquina_atual['partes'][parte_corpo]
            fraqueza = parte_atual['fraqueza']
            dano_max = parte_atual['dano_max']
            cx = parte_atual['cx']
            cy = parte_atual['cy']
            
            if fx == cx and fy == cy:
                parte_atual['acertos_criticos']['acertos'] += 1
            
            dano = calcula_dano(tipo_flecha, fraqueza, dano_max, cx, cy, fx, fy)
            maquina_atual['hp_maquina'] = max(0, maquina_atual['hp_maquina'] - dano)
            flechas_utilizadas[tipo_flecha] = flechas_utilizadas.get(tipo_flecha, 0) + 1
            copia_dicionario_flechas[tipo_flecha] = max(0, copia_dicionario_flechas[tipo_flecha] - 1)
            flechas_disparadas += 1

            if flechas_disparadas % 3 == 0:
                for maquina in partes_maquina.values():
                    if maquina['hp_maquina'] > 0:
                        hp_aloy = max(0, hp_aloy - maquina['pontos_ataque'])
            
            if maquina_atual['hp_maquina'] == 0:
                maquinas_derrotadas_combate += 1
                maquinas_derrotadas_total += 1
                lista_maquinas_derrotadas.append(alvo)
            
            if maquinas_derrotadas_combate == qtd_maquinas or hp_aloy == 0 or all(qtd == 0 for qtd in copia_dicionario_flechas.values()):
                break
        
        hp_apos_combate = hp_aloy
        
        if hp_aloy > 0: 
            hp_aloy = calcular_recuperacao(hp_aloy, hp_max_aloy)

        combate += 1
        
        print(f"Combate {combate}, vida = {hp_max_aloy}")
        
        for l in lista_maquinas_derrotadas:
            print(f"Máquina {l} derrotada")       
        
        print(f"Vida após o combate = {hp_apos_combate}")
        
        if hp_aloy > 0: 
            if not all(qtd == 0 for qtd in copia_dicionario_flechas.values()):
                print("Flechas utilizadas:")
            
                for flecha in dicionario_flechas.keys():
                    quantidade = flechas_utilizadas.get(flecha, 0)
                    if quantidade > 0:
                        quantidade_total = dicionario_flechas.get(flecha, 0)
                        print(f"- {flecha}: {quantidade}/{quantidade_total}")
            
            criticos_impressos = False
            for alvo, maquina in partes_maquina.items():
                dano_critico = False

                for parte_corpo, parte_info in maquina['partes'].items():
                    acertos_criticos = parte_info['acertos_criticos']
                    if acertos_criticos['acertos'] > 0 and not criticos_impressos:
                        print('Críticos acertados:')
                        criticos_impressos = True
            
                    if acertos_criticos['acertos'] > 0:
                        if not dano_critico:
                            print(f"Máquina {alvo}:")
                            dano_critico = True
                        
                        print(f"- {(acertos_criticos['cx'], acertos_criticos['cy'])}: {acertos_criticos['acertos']}x")
        
        flechas_utilizadas.clear()
        lista_maquinas_derrotadas.clear()
        
        if hp_aloy == 0 or maquinas_derrotadas_total == num_mosntros or all(qtd == 0 for qtd in copia_dicionario_flechas.values()):
            break

    if hp_aloy == 0:
        print("Aloy foi derrotada em combate e não retornará a tribo.")
    elif all(qtd == 0 for qtd in copia_dicionario_flechas.values()):
        print("Aloy ficou sem flechas e recomeçará sua missão mais preparada.")
    else:
        print("Aloy provou seu valor e voltou para sua tribo.")


if __name__ == "__main__":
    main()
