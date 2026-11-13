from arquivos import ler_json
from equipes import CAMINHO_REGIMES
from turnos import CAMINHO_TURNOS, cumprimento, minutos_em_estado


def calcular_relatorio(codigo):
    turnos = ler_json(CAMINHO_TURNOS, [])
    regimes = ler_json(CAMINHO_REGIMES, {})
    regime = regimes.get(codigo)

    relatorio = {
        "equipe": codigo,
        "turnos": 0,
        "duracao_total": 0,
        "minutos_em_pausa": 0,
        "pausas_realizadas": 0,
        "pausas_recomendadas": 0,
        "minutos_normal": 0,
        "minutos_atencao": 0,
        "minutos_critico": 0,
        "minutos_perigo": 0,
        "tem_regime": regime is not None,
    }

    for turno in turnos:
        if turno["equipe"] != codigo:
            continue
        dados = cumprimento(turno, regime)
        relatorio["turnos"] += 1
        relatorio["duracao_total"] += dados["duracao_rota"]
        relatorio["minutos_em_pausa"] += dados["minutos_em_pausa"]
        relatorio["pausas_realizadas"] += dados["pausas_realizadas"]
        if dados["pausas_recomendadas"] is not None:
            relatorio["pausas_recomendadas"] += dados["pausas_recomendadas"]
        relatorio["minutos_normal"] += minutos_em_estado(turno, ("NORMAL",))
        relatorio["minutos_atencao"] += minutos_em_estado(turno, ("ATENCAO",))
        relatorio["minutos_critico"] += minutos_em_estado(turno, ("CRITICO",))
        relatorio["minutos_perigo"] += minutos_em_estado(turno, ("PERIGO",))
    return relatorio