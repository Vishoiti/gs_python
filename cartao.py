SINAIS_ALERTA = (
    "Sede intensa e boca seca",
    "Dor de cabeça e tontura",
    "Cãibras nas pernas, braços ou barriga",
    "Náusea ou vômito",
    "Cansaço fora do comum e fraqueza",
    "Pele muito quente e vermelha, com pouco ou nenhum suor",
)

SINAIS_GRAVES = (
    "Confusão mental ou fala enrolada",
    "Desmaio ou perda de consciência",
    "Convulsão",
)

O_QUE_FAZER = (
    "Pare e vá para a sombra ou um local mais fresco",
    "Beba água aos poucos",
    "Avise a equipe e não fique sozinho",
    "Molhe o rosto e o pescoço com água fresca",
    "Só volte ao trabalho quando estiver melhor",
)


def exibir_lista(titulo, itens):
    print(f"\n{titulo}")
    for item in itens:
        print(f" - {item}")


def exibir_cartao_alerta():
    print("\n------ SINAIS DE ALERTA DO CALOR -----")
    exibir_lista("Fique atento se sentir ou notar em um colega:", SINAIS_ALERTA)
    exibir_lista("SINAIS GRAVES (chame socorro imediatamente, ligue 192):", SINAIS_GRAVES)
    exibir_lista("O que fazer:", O_QUE_FAZER)
    print("\nAviso: este cartão é uma orientação geral e não substitui")
    print("a avaliação de um profissional de saúde.")