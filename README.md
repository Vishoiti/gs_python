<p align="center">
  <img src="logo/pausacerta-logo.svg" alt="Logo Pausa Certa" width="420">
</p>

<p align="center"><em>A pausa na hora certa, para quem corre atrás do caminhão.</em></p>

## Ficha da CitizenTech

| | |
|---|---|
| **Nome da CitizenTech** | Pausa Certa |
| **Cidade e bairro** | São Paulo (SP). Rota de exemplo: Paraisópolis e Morumbi |
| **Cidadão beneficiado** | Gari da coleta de lixo de empresa contratada pela prefeitura, que corre atrás do caminhão e ergue sacos ao sol, com o calor mais forte por volta do meio-dia |
| **Problema, em uma frase** | Os garis da coleta trabalham sob calor forte sem pausas além do intervalo obrigatório, porque não há um sinal objetivo de quando parar e eles têm receio de "perder tempo" diante da chefia |
| **Como funciona** | Uma estação com ESP32 no caminhão mede o calor (ar, umidade, globo negro e sol), calcula o índice de calor e acende um semáforo na traseira, visível para os coletores, com a ação no display da cabine ("PAUSA NA SOMBRA"). O botão de pausa registra as pausas da equipe e o sensor do galão avisa a reposição de água antes de acabar. Tudo funciona sem internet e sincroniza na garagem. A empresa acompanha cada equipe num painel web e recebe um relatório semanal |
| **O que cada parte faz** | **Python:** calculadora de estresse térmico, regime de pausas da empresa e relatório por equipe. **Matemática:** modelos do índice de calor e do aquecimento do globo, com derivada e limites. **Edge:** estação ESP32 com sensores, semáforo, LCD e envio MQTT para o FIWARE. **Front-end:** painel React para o encarregado, com estado das equipes e pontos de apoio. **STXD:** requisitos, regras de negócio e protótipo a partir de entrevistas com dois garis. **Pitch:** história do Sandro e do Jackson, impacto e modelo de negócio. **Web:** CRUD de equipes, regimes e pontos de apoio, previsão do tempo (Open-Meteo), CEP (ViaCEP) e dados do Orion |
| **Link do repositório** | [github.com/Vishoiti/gs_python](https://github.com/Vishoiti/gs_python) |
| **Indicador de impacto** | Pausas recomendadas × pausas realizadas por equipe e por turno; minutos em estado CRÍTICO ou PERIGO sem pausa; rotas concluídas por turno antes e depois das pausas organizadas |
| **ODS conectados** | ODS 8 (8.8, trabalho seguro) · ODS 3 (3.9 e 3.d, saúde) · ODS 13 (13.1, adaptação ao clima) · ODS 10 (redução das desigualdades) |

*As falas e os primeiros nomes do Sandro e do Jackson (garis da coleta, entrevistados em 9/11/2026) são usados com autorização deles. Sobrenome, empresa e local não são divulgados.*

*Este repositório contém a parte de **Python**. A rota (Paraisópolis e Morumbi) é um exemplo do projeto, e todas as leituras de calor do programa são simuladas.*

# Pausa Certa · Computational Thinking with Python

Aplicação de terminal em Python que funciona como o "cérebro" do projeto **Pausa Certa**: classifica o estresse térmico, organiza o regime de pausas definido pela empresa e gera relatórios por equipe para a segurança do trabalho na coleta de lixo.

Projeto da Global Solution 2026.2 (FIAP · CitizenTech), Problema 4: *trabalhadores ao ar livre sem controle de pausa no calor*.

## O problema

Garis da coleta de lixo trabalham sob sol forte, com o calor mais intenso entre 11h e 15h, e quase não param além do intervalo obrigatório. Não existe um sinal objetivo de quando pausar, e há receio de "perder tempo" diante da chefia, já que a coleta é por rota. A pausa acaba dependendo da boa vontade de cada um.

Em entrevistas feitas pelo grupo com coletores, o desejo apareceu de forma clara:

> "A hora da pausa ia ajudar muito, ainda mais se fossem várias pausas no dia, mesmo que curtas." — Jackson, coletor

O problema é global: segundo a OIT (relatório de 2024), cerca de 2,41 bilhões de trabalhadores (71% da força de trabalho mundial) estão expostos a calor excessivo, e 18.970 mortes por ano são atribuídas ao calor no trabalho. *Fonte: ONU Brasil/OIT.*

**ODS relacionados:** 8 (8.8), 3 (3.9 e 3.d), 13 (13.1) e 10.

## O que o programa faz

O programa abre um menu com cinco opções:

| Opção | Funcionalidade |
|---|---|
| 1 | **Calculadora de estresse térmico:** a partir de temperatura, umidade e temperatura de globo, calcula índice de calor, bulbo úmido e IBUTG estimado, e mostra o estado (NORMAL, ATENCAO, CRITICO ou PERIGO) com a ação recomendada. |
| 2 | **Equipes e regimes de pausa:** cadastro, listagem, edição e exclusão de equipes (com confirmação), e definição do regime de pausa de cada uma, com responsável e data. |
| 3 | **Turnos e pausas:** registro de turnos, pausas realizadas e leituras de calor, e listagem dos turnos de uma equipe. |
| 4 | **Relatório por equipe:** tempo em cada estado, pausas realizadas × recomendadas e duração das rotas, exibido na tela e salvo opcionalmente em `relatorio_AAAA-MM-DD.txt`. |
| 5 | **Sinais de alerta do calor:** cartão de orientação com sintomas e o que fazer. |

### Estados do sistema

| Estado | Índice de calor | Mensagem |
|---|---|---|
| NORMAL | abaixo de 27 °C | Trabalho normal |
| ATENCAO | 27 a 32 °C | Água e sombra |
| CRITICO | 32 a 41 °C | Pausa na sombra (na próxima parada da rota) |
| PERIGO | 41 °C ou mais | Suspender trabalho pesado |

As faixas são as do índice de calor da NOAA, usadas como **triagem**.

## Como executar

Requisitos: **Python 3.10 ou mais novo** (o programa usa `match/case`). Nenhuma biblioteca externa é necessária, só a biblioteca padrão (`json`, `math`, `datetime`, `os`).

```bash
python main.py
```

Os arquivos da pasta `dados/` são criados automaticamente na primeira gravação, então o programa roda mesmo numa pasta limpa.

**Teste rápido:** na opção 1, informe temperatura `34,2`, umidade `46` e globo `47,5`. O resultado esperado é índice de calor **37,5 °C**, bulbo úmido **25,1 °C**, IBUTG estimado **30,5 °C** e estado **CRITICO**.

## Estrutura dos arquivos

```
gs_python/
├── main.py            # menu principal
├── subalgoritmo.py    # exibição dos menus e leitura da escolha
├── submenus.py        # submenus de equipes e de turnos
├── calor.py           # índice de calor, bulbo úmido, IBUTG e estados
├── calculadora.py     # opção 1: calculadora de estresse térmico
├── equipes.py         # CRUD de equipes
├── regimes.py         # regime de pausa de cada equipe
├── turnos.py          # turnos, pausas, leituras e cumprimento
├── relatorio.py       # opção 4: relatório por equipe
├── cartao.py          # opção 5: sinais de alerta
├── entrada.py         # leitura e validação de entradas
├── arquivos.py        # leitura e gravação de JSON
├── prompt.md          # uso de IA no desenvolvimento
└── README.md
```

A pasta `dados/` (com `equipes.json`, `regimes.json` e `turnos.json`) **não vem no repositório**: ela é criada automaticamente na primeira gravação. Os relatórios salvos pela opção 4 ficam em `relatorio_AAAA-MM-DD.txt`.

## Conceitos de programação aplicados

| Requisito | Onde aparece |
|---|---|
| Menu de opções | `main()` e submenus, com `while True` |
| Validação de entradas | `ler_float()`, `ler_inteiro()`, `ler_opcao()`, `ler_hora()`, `ler_data()` |
| Tratamento de exceções | `try/except` com `ValueError`, `FileNotFoundError` e `json.JSONDecodeError` |
| `if/elif/else` e `match/case` | `nivel_por_indice()`, `acao_do_estado()` e os menus |
| `while` e `for` | menus, validações, listagens e somas do relatório |
| Funções com parâmetros e retorno | `indice_calor()`, `bulbo_umido()`, `cumprimento()`, entre outras |
| Listas, tuplas e dicionários | equipes (lista de dicionários), limites e estados (tuplas), regimes (dicionário) |
| Persistência em JSON | `equipes.json`, `regimes.json` e `turnos.json` |

## Decisões e limites

- O índice de calor da NOAA é usado como **triagem**. O IBUTG é uma **estimativa**, e não substitui a medição prevista na NHO 06 da Fundacentro.
- Os números do regime de pausa (minutos de pausa e máximo sem pausa) são **preenchidos pela empresa**. O programa não inventa valores da norma e nunca diz "insalubre" ou "dentro da norma".
- A pausa **nunca é negada nem bloqueada**: o programa apenas registra e informa. Na coleta, ela é recomendada na próxima parada natural da rota.
- Relatórios são **por equipe, nunca por pessoa**, para que o sistema não seja usado para punir quem para. Equipes são identificadas por código.
- Os minutos em cada estado são **estimados** pelas leituras: cada leitura vale até a próxima, e a última vale até o fim do turno.
- Turnos que passam da meia-noite não são aceitos nesta versão.
- Todos os dados são simulados, sem informações pessoais reais.

## Integrantes

| Nome | RM |
|---|---|
| Vinícius Shoiti Rios Honda | RM569744 |
| Enzo Borgo Pereira | RM572529 |
| Raphael Mascarenhas Lima | RM572313 |
| Guilherme Pimentel Vilela | RM569177 |
| Vinícius Campestrini Rodado | RM570703 |