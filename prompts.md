# Uso de IA · Pausa Certa (Python)

Documento exigido na disciplina *Computational Thinking with Python* sobre como ferramentas de Inteligência Artificial foram usadas no desenvolvimento do projeto.

## 1. Ferramentas de IA utilizadas e finalidades

| Ferramenta | Finalidade |
|---|---|
| **Claude (Anthropic)** | Guia de desenvolvimento passo a passo: divisão do projeto em etapas, explicação dos conceitos, sugestão de código para cada função, revisão do código enviado, diagnóstico de erros e sugestão de mensagens de commit. Também ajudou a redigir o `README.md` e este arquivo. |

A IA foi usada como **copiloto**: cada trecho foi digitado e testado pelo integrante responsável, não colado em bloco, e o código foi explicado antes de ser escrito.

## 2. Prompts utilizados

Estão listados os prompts mais relevantes enviados ao Claude, separados por tema. Alguns foram acompanhados de prints de tela. Os prompts da seção 2.1 nasceram de uma revisão do código feita pelo integrante responsável, que anotou as partes que menos dominava.

### 2.1 Dúvidas de conceito e de organização

1. > "claude, meu projeto de python hoje tem um arquivo só com os menus (subalgoritmo.py) e mais uns arquivos de funções. como posso organizar um projeto em vários arquivos de formas diferentes, sem depender de um arquivo só pra tudo? quais critérios eu uso pra decidir o que vai em cada arquivo?"

   *Aprendido:* organizar por assunto e por camada (dados, regras e interface), manter o `main.py` enxuto e evitar importação circular. Resultou na divisão `subalgoritmo.py` (exibição dos menus) e `submenus.py` (execução).

2. > "como eu importo funções de um arquivo pra usar em outro arquivo no python? quais são as formas de fazer o import e quando eu uso cada uma?"

   *Aprendido:* diferença entre `import modulo` e `from modulo import funcao`, e por que evitar `import *`.

3. > "no meu calor.py eu uso a biblioteca math nas fórmulas do índice de calor e do bulbo úmido. quais outras funções do math eu poderia usar pra facilitar contas parecidas? e por que usar o math em vez de fazer na mão?"

   *Aprendido:* funções do `math` (`sqrt`, `atan`, `exp`, `log`, `sin`, `cos`) e a diferença para as funções nativas (`abs`, `round`, `min`, `max`).

4. > "no calculadora.py e no equipes.py eu formatei textos com f-string, tipo `.1f` pra casas decimais e `:<10` pra alinhar colunas. me explica como funciona essa formatação e quais outras opções eu tenho pra alinhar e arredondar valores na tela?"

   *Aprendido:* formatos `:.1f`, `:<10`, `:>10`, `:^10` e `:02d`, usados nas tabelas de equipes, regimes e turnos.

5. > "como posso converter minutos em texto no python, tipo 400 minutos virar 6h40? quero entender o que faz a divisão inteira e o resto da divisão nessa conta, e porque o `:02d` completa com zero."

   *Aprendido:* `//` dá as horas, `%` dá os minutos restantes, e `:02d` completa com zero. Usado em `formatar_horas()`, no `relatorio.py`.

6. > "qual seria uma forma de montar um relatório inteligente pro meu programa usando os dados que eu já guardo nos JSON (equipes, regimes, turnos e leituras)? me dá ideias de informações úteis pra mostrar, sem identificar trabalhadores individuais."

   *Aprendido:* ideias como horário de pico, comparação de turnos e melhor janela de trabalho. O relatório atual mostra o tempo em cada estado e as pausas realizadas × recomendadas.

7. > "como eu passo horários no formato HH:MM pra minutos no python pra poder somar e subtrair? quais cuidados eu preciso ter com formato errado, tipo letras ou horário que não existe?"

    *Aprendido:* `split(":")`, conversão com `int()` e validação separada de horas e minutos. Usado em `hora_para_minutos()` e `ler_hora()`.

8. > "quais comandos do módulo datetime eu posso usar pra criar uma função que lê uma data digitada e só aceita se ela for válida? quero entender como o python reconhece datas que não existem, tipo 30 de fevereiro."

    *Aprendido:* `datetime.strptime` com `%Y-%m-%d` recusa datas inexistentes, e `date.today()` devolve a data de hoje. Usado em `ler_data()`.

9. > "como eu registro as informações de várias variáveis juntas em um dicionário, tipo equipe, data, início e fim de um turno? quando eu uso lista e quando eu uso dicionário, e como esse dado vira JSON depois?"

    *Aprendido:* lista de dicionários para vários registros, conversão de tipos no `json.dump` e o cuidado com as chaves, que são texto. Usado no registro de turnos.

### 2.2 Decisões e correção de erros

10. > "no 12:75 o sistema retorna o horário como certo, ficou concluido e registrado sendo que nao existe esse horário"

    *Resultado:* a validação passou a conferir horas (0 a 23) e minutos (0 a 59) separadamente.

11. > "eu dei enter para registrar hoje o turno e registrar leitura e apareceu que não existe turno nessa data"

    *Resultado:* após enviar o código e o JSON, a causa foi o `return None` do `buscar_turno()` dentro do `for`.

12. > "Preciso realizar essa função sem o uso do lambda, pois ainda não foi visto na matéria, teria outra forma de trocar a função?"

    *Resultado:* o `lambda` foi trocado pela função comum `horario_da_leitura()`, por não ter sido visto na disciplina.

13. > "A forma como o resultado aparece em % não fica visivelmente intuitivo e simples, me dê diferentes opções do resultado aparecer"

    *Resultado:* o relatório passou a mostrar "2 de 22 feitas (20 a menos)", em tom neutro.

## 3. Funcionalidades desenvolvidas, sugeridas ou modificadas com auxílio da IA

| Módulo | O que a IA fez | O que o grupo decidiu ou alterou |
|---|---|---|
| `calor.py` | Sugeriu as fórmulas (índice de calor da NOAA, bulbo úmido de Stull, IBUTG estimado), a classificação por estados e o `match/case` das ações. | Digitou as fórmulas, rodou o caso de referência e reorganizou o formato. |
| `entrada.py` | Sugeriu `ler_float`, `ler_inteiro`, `ler_opcao` e `confirmar`, com `while` e `try/except`. | Criou o arquivo sem aproveitar o `ler_inteiro` antigo e testou cada caso. |
| `arquivos.py` | Sugeriu `ler_json` e `salvar_json`, e depois a criação automática da pasta `dados/`. | Testou com e sem a pasta. |
| `equipes.py` e `regimes.py` | Sugeriu o CRUD e o regime de pausa, com a remoção do regime junto com a equipe. | Ajustou textos e limites. |
| `turnos.py` | Sugeriu conversão de horários, registro de turno, pausas e leituras, e `cumprimento()`. | Encontrou o furo do `12:75` e removeu o `lambda`. |
| `relatorio.py` | Sugeriu o cálculo por equipe, a separação em `montar`, `exibir` e `salvar`, e a ligação ao menu. | Trocou o percentual por texto ("2 de 22 feitas") e corrigiu o recuo. |
| `cartao.py` | Sugeriu a estrutura com tuplas e o texto genérico de orientação. | Revisou o conteúdo. |
| Menus | Sugeriu `subalgoritmo.py` (exibição), `submenus.py` (execução) e `main.py`. | Escolheu a organização dos arquivos. |
| `README.md` e este arquivo | Redigiu o rascunho. | Revisou, colocou o logo e a ficha da CitizenTech. |

## 4. Como o grupo verificou, testou e ajustou os resultados

- **Teste de referência do guia:** com temperatura 34,2 °C, umidade 46 % e globo 47,5 °C, o programa precisa mostrar índice de calor 37,5 °C, bulbo úmido 25,1 °C, IBUTG estimado 30,5 °C e estado CRITICO. Os valores saíram idênticos, e são os mesmos do contrato de dados do projeto.
- **Teste por etapa:** cada função foi testada separadamente, com entradas válidas e inválidas (letras, campo vazio, número fora do intervalo, horário inexistente, código de equipe inexistente), antes do commit.
- **Conferência dos arquivos JSON:** os `.json` foram abertos no VS Code depois de cada gravação para conferir chaves e acentos.
- **Pasta limpa:** o programa foi executado sem a pasta `dados/` para confirmar que ela é criada sozinha.
- **Commits pequenos:** um commit por unidade testada, o que permitiu voltar a um ponto funcionando quando algo quebrou.

## 5. Análise crítica

**Benefícios**
- A divisão em etapas pequenas, com explicação de cada linha, ajudou o grupo a entender o código e a conseguir explicá-lo.
- A revisão rápida de erros (indentação, `:` faltando, aspas abertas no terminal) economizou tempo.
- A IA lembrou de regras do projeto que seriam fáceis de esquecer: relatórios por equipe (nunca por pessoa), pausa nunca bloqueada e valores do regime definidos pela empresa.

**Limitações e erros da IA**
- Em alguns momentos, a IA sugeriu recursos que podem não ter sido vistos na disciplina (`lambda`, *type hints*) e precisou ser pedida para simplificar.
- Valores esperados em testes foram só aproximados: no ajuste de ar seco do índice de calor, a IA indicou uma faixa de 32 a 33 °C, e o resultado real foi 31,9 °C. O grupo conferiu a fórmula antes de aceitar.
- A IA deu uma orientação inicial sobre importação circular que depois precisou ser corrigida e refinada, quando o grupo propôs juntar menus.
- Ao interpretar um print de tela, a IA apontou uma coluna faltando que dependia da renderização da fonte, e o grupo precisou conferir o código para confirmar.
- Parte do que a IA sugeriu (limites de coletores, minutos de pausa, regra de estimativa dos minutos em CRITICO) são **escolhas do projeto**, e não valores de norma. Isso está declarado no `README.md`.

**Dificuldades**
- Erros de digitação em dados e chaves JSON (`mimutos_pausa`) que a IA só conseguiu apontar depois de ver o arquivo.
- Falhas de recuo e de Git (aspas abertas no commit, remoção de arquivo fora do commit, comando rodado na pasta errada), resolvidas com a explicação da IA e conferência no terminal.

**Reflexão**
A IA funcionou melhor como professora e revisora do que como autora do código: o que mais valeu foi entender o motivo de cada linha e testar. Todo o código entregue foi digitado, testado e entendido pelo grupo.