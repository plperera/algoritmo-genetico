import random
import math

def objetivo(x):
    return x**3 - 6*x + 14

def conversao_binario_para_real(bits_binarios, limite_inferior, limite_superior):
    valor_dec = int(''.join(map(str, bits_binarios)), 2)
    proporcao = (limite_superior - limite_inferior) / (2**len(bits_binarios) - 1)
    return limite_inferior + valor_dec * proporcao

def criar_populacao(tamanho, num_bits):
    return [[random.randint(0, 1) for _ in range(num_bits)] for _ in range(tamanho)]

def avaliar_populacao(populacao, limite_inferior, limite_superior):
    aptidoes = []
    for indiv in populacao:
        valor_real = conversao_binario_para_real(indiv, limite_inferior, limite_superior)
        aptidao = objetivo(valor_real)
        aptidoes.append(aptidao)
    return aptidoes

def torneio_selecao(populacao, aptidoes):
    competidores = random.sample(list(zip(populacao, aptidoes)), 3)
    competidores.sort(key=lambda x: x[1])  # Menor valor de aptidão é melhor
    return competidores[0][0]

def recombinar(pai_a, pai_b, cortes):
    filho_a, filho_b = pai_a[:], pai_b[:]
    if cortes == 1:
        ponto = random.randint(1, len(pai_a) - 1)
        filho_a = pai_a[:ponto] + pai_b[ponto:]
        filho_b = pai_b[:ponto] + pai_a[ponto:]
    elif cortes == 2:
        p1 = random.randint(1, len(pai_a) - 2)
        p2 = random.randint(p1 + 1, len(pai_a) - 1)
        filho_a = pai_a[:p1] + pai_b[p1:p2] + pai_a[p2:]
        filho_b = pai_b[:p1] + pai_a[p1:p2] + pai_b[p2:]
    return filho_a, filho_b

def aplicar_mutacao(individuo, chance_mutacao):
    for idx in range(len(individuo)):
        if random.random() < chance_mutacao:
            individuo[idx] = 1 - individuo[idx]
    return individuo

def algoritmo_evolutivo(limite_inferior, limite_superior, num_bits, tamanho_pop, num_geracoes, chance_mutacao, num_cortes, metodo_selecao, taxa_elitismo):
    populacao_atual = criar_populacao(tamanho_pop, num_bits)
    melhores_resultados = []

    quantidade_elitismo = int(taxa_elitismo * tamanho_pop)
    
    for geracao in range(num_geracoes):
        aptidoes = avaliar_populacao(populacao_atual, limite_inferior, limite_superior)
        nova_populacao = []

        # Elitismo
        populacao_com_aptidao = list(zip(populacao_atual, aptidoes))
        populacao_com_aptidao.sort(key=lambda x: x[1])  # Menor é melhor
        elite = [indiv for indiv, _ in populacao_com_aptidao[:quantidade_elitismo]]
        nova_populacao.extend(elite)

        while len(nova_populacao) < tamanho_pop:
            if metodo_selecao == 'torneio':
                p1 = torneio_selecao(populacao_atual, aptidoes)
                p2 = torneio_selecao(populacao_atual, aptidoes)
            else:
                p1 = torneio_selecao(populacao_atual, aptidoes)
                p2 = torneio_selecao(populacao_atual, aptidoes)
            
            f1, f2 = recombinar(p1, p2, num_cortes)
            f1 = aplicar_mutacao(f1, chance_mutacao)
            f2 = aplicar_mutacao(f2, chance_mutacao)
            nova_populacao.extend([f1, f2])

        populacao_atual = nova_populacao[:tamanho_pop]
        aptidoes = avaliar_populacao(populacao_atual, limite_inferior, limite_superior)
        melhor_aptidao = min(aptidoes)
        melhor_individuo = populacao_atual[aptidoes.index(melhor_aptidao)]
        melhor_valor_real = conversao_binario_para_real(melhor_individuo, limite_inferior, limite_superior)
        melhores_resultados.append((melhor_valor_real, melhor_aptidao))

        print(f"Geração {geracao+1}: x = {melhor_valor_real}, f(x) = {melhor_aptidao}")

    # Retorna o melhor resultado obtido
    melhor_solucao = min(melhores_resultados, key=lambda x: x[1])
    return melhor_solucao

if __name__ == "__main__":
    limite_inferior = -10
    limite_superior = 10
    num_bits = 16  # Precisão
    tamanho_pop = 10
    num_geracoes = 100
    chance_mutacao = 0.01
    num_cortes = 2
    metodo_selecao = 'torneio'
    taxa_elitismo = 0.1  # 10% da população

    melhor_valor, melhor_aptidao = algoritmo_evolutivo(
        limite_inferior, limite_superior, num_bits, tamanho_pop, num_geracoes,
        chance_mutacao, num_cortes, metodo_selecao, taxa_elitismo
    )

    print(f"\nMelhor solução obtida: x = {melhor_valor}, f(x) = {melhor_aptidao}")
