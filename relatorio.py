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


def formatar_horas(minutos):
    return f"{minutos // 60}h{minutos % 60:02d}"    # Converte minutos em texto "XhYY"


def exibir_relatorio(relatorio):
    print(f"\n--- Relatório da equipe {relatorio['equipe']} ---")
    if relatorio["turnos"] == 0:
        print("Nenhum turno registrado para esta equipe.")
        return

    print(
        f"""Turnos registrados: {relatorio['turnos']}
            Duração total das rotas: {formatar_horas(relatorio['duracao_total'])}
            \nTempo em cada estado (estimado pelas leituras):
            NORMAL: {formatar_horas(relatorio['minutos_normal'])}
            ATENCAO: {formatar_horas(relatorio['minutos_atencao'])}
            CRITICO: {formatar_horas(relatorio['minutos_critico'])}
            PERIGO: {formatar_horas(relatorio['minutos_perigo'])}
            \nPausas:
            Pausas realizadas: {relatorio['pausas_realizadas']}
            Tempo total em pausa: {relatorio['minutos_em_pausa']} min
""")
    if relatorio["tem_regime"]:
        recomendadas = relatorio["pausas_recomendadas"]
        realizadas = relatorio["pausas_realizadas"]
        print(f"Pausas recomendadas: {recomendadas}")
        if recomendadas == 0:
            print("  Situação: nenhuma pausa era devida")
        elif realizadas >= recomendadas:
            print(f" Situação: todas as pausas recomendadas foram feitas.")   
        else:
            faltaram = recomendadas - realizadas
            print(f"  Situação: {realizadas} de {recomendadas} feitas ({faltaram} a menos).")
        print("\nComo ler: as pausas recomendadas são estimadas pelo tempo em")
        print(" CRITICO/PERIGO e pelo limite sem pausa que a empresa definiu.")
    else:
        print(" Esta equipe não tem regime de pausa definido.")