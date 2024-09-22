import random
import copy

def gerar_populacao_inicial(tam_populacao, qtd_itens):
    return [[random.randint(0, 1) for _ in range(qtd_itens)] for _ in range(tam_populacao)]

def avaliar_cromossomo(cromossomo, itens, limite_peso):
    peso_acumulado = 0
    valor_acumulado = 0
    for idx in range(len(cromossomo)):
        if cromossomo[idx] == 1:
            peso_acumulado += itens[idx][0]
            valor_acumulado += itens[idx][1]
    if peso_acumulado > limite_peso:
        return 0  # Penalidade por excesso de peso
    return valor_acumulado

def roleta_selecao(populacao, pontuacoes):
    total_pontuacao = sum(pontuacoes)
    escolha = random.uniform(0, total_pontuacao)
    soma_atual = 0
    for individuo, pontuacao in zip(populacao, pontuacoes):
        soma_atual += pontuacao
        if soma_atual > escolha:
            return individuo

def recombinacao(pai_a, pai_b):
    corte = random.randint(1, len(pai_a) - 1)
    filho_a = pai_a[:corte] + pai_b[corte:]
    filho_b = pai_b[:corte] + pai_a[corte:]
    return filho_a, filho_b

def aplicar_mutacao(cromossomo, chance_mutacao=0.01):
    for i in range(len(cromossomo)):
        if random.random() < chance_mutacao:
            cromossomo[i] = 1 - cromossomo[i]
    return cromossomo

def resolver_problema_genetico(itens, limite_peso, tam_populacao, qtd_geracoes):
    qtd_itens = len(itens)
    populacao_atual = gerar_populacao_inicial(tam_populacao, qtd_itens)
    melhores_por_geracao = []

    for geracao in range(qtd_geracoes):
        pontuacoes = [avaliar_cromossomo(individuo, itens, limite_peso) for individuo in populacao_atual]
        nova_populacao = []

        for _ in range(tam_populacao // 2):
            pai_a = roleta_selecao(populacao_atual, pontuacoes)
            pai_b = roleta_selecao(populacao_atual, pontuacoes)
            filho_a, filho_b = recombinacao(pai_a, pai_b)
            filho_a = aplicar_mutacao(filho_a)
            filho_b = aplicar_mutacao(filho_b)
            nova_populacao.extend([filho_a, filho_b])

        populacao_atual = nova_populacao
        pontuacoes = [avaliar_cromossomo(individuo, itens, limite_peso) for individuo in populacao_atual]
        melhor_valor = max(pontuacoes)
        melhor_cromossomo = populacao_atual[pontuacoes.index(melhor_valor)]
        melhores_por_geracao.append([melhor_valor, melhor_cromossomo])

        print(f"Geração {geracao+1}: Melhor Valor = {melhor_valor}")

    return melhores_por_geracao

if __name__ == "__main__":
    itens_com_peso_valor = [[2, 10], [4, 30], [6, 300], [8, 10], [8, 30],
                            [8, 300], [12, 50], [25, 75], [50, 100], [100, 400]]
    limite_peso = 100
    tamanho_pop = 150
    geracoes_totais = 50

    melhores_solucoes = resolver_problema_genetico(itens_com_peso_valor, limite_peso, tamanho_pop, geracoes_totais)
    print("\nMelhores soluções por geração:")
    for idx, (valor, cromossomo) in enumerate(melhores_solucoes):
        print(f"Geração {idx + 1}: Valor = {valor}, Cromossomo = {cromossomo}")
