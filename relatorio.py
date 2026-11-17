from arquivos import ler_json
from entrada import confirmar
from equipes import CAMINHO_REGIMES, CAMINHO_EQUIPES, exibir_equipes, buscar_equipe
from turnos import CAMINHO_TURNOS, cumprimento, minutos_em_estado
from datetime import date


def calcular_relatorio(codigo):
    """Soma os números de todos os turnos da equipe e devolve um dicionário."""
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
    """ Converte minutos em texto "XhYY"""
    return f"{minutos // 60}h{minutos % 60:02d}"    


def montar_relatorio(relatorio):
    """Monta o texto do relatório e devolve uma lista de linhas."""
    linhas = [f"\n--- Relatório da equipe {relatorio['equipe']} ---"]
    if relatorio["turnos"] == 0:
        linhas.append("Nenhum turno registrado para esta equipe.")
        return linhas
    
    linhas.append(f"Turnos registrados: {relatorio['turnos']}")
    linhas.append(f"Duração total das rotas: {formatar_horas(relatorio['duracao_total'])}")
    linhas.append("")
    linhas.append("Tempo em cada estado (estimado pelas leituras):")
    linhas.append(f"  NORMAL:  {formatar_horas(relatorio['minutos_normal'])}")
    linhas.append(f"  ATENCAO: {formatar_horas(relatorio['minutos_atencao'])}")
    linhas.append(f"  CRITICO: {formatar_horas(relatorio['minutos_critico'])}")
    linhas.append(f"  PERIGO:  {formatar_horas(relatorio['minutos_perigo'])}")
    linhas.append("")
    linhas.append("Pausas:")
    linhas.append(f"  Pausas realizadas: {relatorio['pausas_realizadas']}")
    linhas.append(f"  Tempo total em pausa: {relatorio['minutos_em_pausa']} min")

    if relatorio["tem_regime"]:
        recomendadas = relatorio["pausas_recomendadas"]
        realizadas = relatorio["pausas_realizadas"]
        linhas.append(f"  Pausas recomendadas: {recomendadas}")
        if recomendadas == 0:
            linhas.append("  Situação: Nenhuma pausa era devida.")
        elif realizadas >= recomendadas:
            linhas.append(f" Situação: Todas as pausas recomendadas foram feitas.")   
        else:
            faltaram = recomendadas - realizadas
            linhas.append(f"  Situação: {realizadas} de {recomendadas} feitas ({faltaram} a menos).")
        linhas.append("\nComo ler: as pausas recomendadas são estimadas pelo tempo em")
        linhas.append("  CRITICO/PERIGO e pelo limite sem pausa que a empresa definiu.")
    else:
        linhas.append("  Esta equipe não tem regime de pausa definido.")
    linhas.append("")
    linhas.append("Obs.: valores estimados; relatório por equipe, sem identificar pessoas.")
    return linhas


def exibir_relatorio(relatorio):
    """Mostra o relatório de uma equipe no terminal."""
    print()
    for linha in montar_relatorio(relatorio):
        print(linha)


def salvar_relatorio(relatorio):
    """Grava o relatório em relatorio_AAAA-MM-DD.txt e devolve o nome do arquivo."""
    nome = f"relatorio_{date.today()}.txt"
    with open(nome, "a", encoding="utf-8") as arquivo:
        for linha in montar_relatorio(relatorio):
            arquivo.write(linha + "\n")
        arquivo.write("\n")
    return nome


def gerar_relatorio():
    """Pede a equipe, mostra o relatório e pergunta se quer salvar em .txt."""
    print("\n--- Relatório por equipe ---")
    equipes = ler_json(CAMINHO_EQUIPES, [])
    if len(equipes) == 0:
        print("Nenhuma equipe cadastrada.")
        return

    exibir_equipes(equipes)
    codigo = input("\nCódigo da equipe: ").strip().upper()
    if buscar_equipe(equipes,codigo) is None:
        print(f"Equipe {codigo} não encontrada.")
        return

    relatorio = calcular_relatorio(codigo)
    exibir_relatorio(relatorio)
    if relatorio["turnos"] > 0 and confirmar("\nSalvar este relatório em arquivo .txt?"):
        print(f"Relatório salvo em {salvar_relatorio(relatorio)}.")