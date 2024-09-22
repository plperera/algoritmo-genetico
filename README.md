# Desafio - Algoritmos Genéticos

## Descrição do Projeto

Este projeto implementa algoritmos evolutivos para resolver dois problemas distintos: a **minimização de funções matemáticas** e o **problema da mochila**. Esses algoritmos são baseados em técnicas genéticas que simulam a evolução para encontrar soluções aproximadas para problemas complexos.

### 1. Arquivo: `minimizacao.py`

Este script utiliza um algoritmo evolutivo para minimizar uma função matemática. O objetivo é encontrar o valor de `x` que minimiza a função `f(x) = x^3 - 6x + 14`.

#### Principais Funções:
- `objetivo(x)`: Calcula o valor da função para um dado `x`.
- `conversao_binario_para_real(bits_binarios, limite_inferior, limite_superior)`: Converte uma representação binária em um número real dentro de um intervalo definido.
- `criar_populacao(tamanho, num_bits)`: Gera uma população inicial de indivíduos representados em binário.
- `avaliar_populacao(populacao, limite_inferior, limite_superior)`: Avalia a aptidão de cada indivíduo na população com base na função objetivo.
- `torneio_selecao(populacao, aptidoes)`: Seleciona um indivíduo da população utilizando o método de torneio.
- `recombinar(pai_a, pai_b, cortes)`: Realiza a recombinação genética entre dois indivíduos (pais) gerando dois novos indivíduos (filhos).
- `aplicar_mutacao(individuo, chance_mutacao)`: Aplica mutações aleatórias em um indivíduo.
- `algoritmo_evolutivo(...)`: Implementa o ciclo completo do algoritmo evolutivo, incluindo seleção, recombinação, mutação e elitismo.

#### Execução:
Basta rodar o script diretamente. Ele busca minimizar a função em um intervalo de [-10, 10] com uma população de 10 indivíduos ao longo de 100 gerações. No final, imprime a melhor solução encontrada.

Comando para execução:
```bash
python minimizacao.py
```

---

### 2. Arquivo: `mochila.py`

Este script resolve o famoso **problema da mochila**, onde o objetivo é maximizar o valor de itens selecionados dentro de um limite de peso.

#### Principais Funções:
- `gerar_populacao_inicial(tam_populacao, qtd_itens)`: Gera uma população inicial de soluções possíveis para o problema da mochila.
- `avaliar_cromossomo(cromossomo, itens, limite_peso)`: Calcula o valor e o peso total de uma solução (cromossomo). Se a solução exceder o limite de peso, ela é penalizada.
- `roleta_selecao(populacao, pontuacoes)`: Seleciona indivíduos utilizando o método da roleta.
- `recombinacao(pai_a, pai_b)`: Faz a recombinação de dois cromossomos (soluções).
- `aplicar_mutacao(cromossomo, chance_mutacao)`: Aplica mutações aleatórias em um cromossomo.
- `resolver_problema_genetico(itens, limite_peso, tam_populacao, qtd_geracoes)`: Executa o algoritmo genético completo, evoluindo a população para encontrar a melhor solução para o problema da mochila.

#### Execução:
Basta rodar o script diretamente. Ele resolve o problema da mochila para 10 itens com diferentes valores e pesos, utilizando uma população inicial de 150 indivíduos e evoluindo por 50 gerações.

Comando para execução:
```bash
python mochila.py
```

---

## Requisitos

- Python 3.x
- Biblioteca `random` e `math` (já inclusas no Python)

## Como Executar

1. Faça o download ou clone o repositório.
2. Navegue até o diretório onde os scripts estão salvos.
3. Execute qualquer um dos scripts diretamente usando Python. Por exemplo:
   ```bash
   python minimizacao.py
   ```

## Personalização

- **Parâmetros do Algoritmo Genético**: Tanto o arquivo `minimizacao.py` quanto o `mochila.py` permitem ajustar diversos parâmetros como o tamanho da população, número de gerações, taxa de mutação, entre outros, para diferentes experimentos.
- **Função Objetivo**: No arquivo `minimizacao.py`, você pode alterar a função objetivo para minimizar outras expressões matemáticas.
