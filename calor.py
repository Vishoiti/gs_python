import math

LIMITES_IC = (27.0, 32.0, 41.0)

ESTADOS = ("NORMAL", "ATENCAO", "CRITICO", "PERIGO")

def nivel_por_indice(ic):
    if ic >= LIMITES_IC[2]:
        return "PERIGO"
    elif ic >= LIMITES_IC[1]:
        return "CRITICO"
    elif ic >= LIMITES_IC[0]:
        return "ATENCAO"
    else:
        return "NORMAL"


def acao_do_estado(estado):
    match estado:
        case "NORMAL":
            return "Trabalho normal."
        case "ATENCAO":
            return "Água e sombra sempre que possível."
        case "CRITICO":
            return "Pausa na sombra na próxima parada da rota."
        case "PERIGO":
            return "Suspender o trabalho pesado até o calor baixar."
        case _:
            return "Estado desconhecido: confira a leitura."