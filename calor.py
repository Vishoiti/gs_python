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


def indice_calor(t_c, ur):
    t = t_c * 9 / 5 + 32
    hi = 0.5 * (t + 61.0 + (t - 68.0) * 1.2 + ur * 0.094)

    if (hi + t) / 2 >= 80:
        hi = (-42.379 + 2.04901523 * t + 10.14333127 * ur - 0.22475541 * t * ur - 0.00683783 * t * t - 0.05481717 * ur * ur + 0.00122874 * t * t * ur
            + 0.00085282 * t * ur * ur - 0.00000199 * t * t * ur * ur)

        if ur < 13 and 80 <= t <= 112:
            hi -=((13 - ur) / 4) * math.sqrt((17 - abs(t - 95)) / 17)
        elif ur > 85 and 80 <= t <= 87:
            hi += ((ur - 85) / 10) * ((87 - t) / 5)            

    return (hi - 32) * 5 / 9


def bulbo_umido(t, ur):
    return (t * math.atan(0.151977 * math.sqrt(ur + 8.313659))
             + math.atan(t + ur) - math.atan(ur - 1.676331) + 0.00391838 * ur ** 1.5 * math.atan(0.023101 * ur) - 4.686035)


def ibutg_estimado(tbu, tg, t):
    return 0.7 * tbu + 0.2 * tg + 0.1 * t