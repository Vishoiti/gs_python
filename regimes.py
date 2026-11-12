from datetime import date

from arquivos import ler_json, salvar_json
from entrada import ler_inteiro, ler_opcao
from equipes import CAMINHO_EQUIPES, buscar_equipe

CAMINHO_REGIMES = "dados/regimes.json"
MODELOS = ("micropausas", "pausa longa")


def definir_regime():
    print("\n--- Definir regime de pausa ---")
    equipes = ler_json(CAMINHO_EQUIPES, [])
    if len(equipes) == 0:
        print("Cadastre uma equipe antes de definir o regime.")
        return

    codigo = input("Código da equipe: ").strip().upper()
    if buscar_equipe(equipes, codigo) is None:
        print(f"Equipe {codigo} não encontrada.")
        return

    modelo = ler_opcao("Modelo (micropausas/pausa longa): ", MODELOS)
    minutos_pausa = ler_inteiro("Minutos de cada pausa: ", 1, 60)
    max_sem_pausa = ler_inteiro("Máximo de minutos sem pausa em CRITICO: ", 10, 240)
    responsavel = input("Responsável pela definição: ").strip()
    if responsavel == "":
        print("O responsável não pode ficar vazio.")
        return

    regimes = ler_json(CAMINHO_REGIMES, {})
    regimes[codigo] = {
        "modelo": modelo,
        "minutos_pausa": minutos_pausa,
        "max_sem_pausa_critico": max_sem_pausa,
        "responsavel": responsavel,
        "definido_em": str(date.today()),
    }
    salvar_json(CAMINHO_REGIMES, regimes)
    print(f"Regime da equipe {codigo} salvo.")


def exibir_regimes(regimes):
    if len(regimes) == 0:
        print("Nenhum regime definido.")
        return

    print(f"{'Equipe':<14}{'Modelo':<13}{'Pausa':<8}{'Max. Crit.':<12}{'Responsável':<18}{'Data'}")
    print("-" * 75)
    for codigo, regime in regimes.items():
        print(f"{codigo:<14}{regime['modelo']:<13}{str(regime['minutos_pausa']) + 'min':<8}"
              f"{str(regime['max_sem_pausa_critico']) + 'min':<12}"
              f"{regime['responsavel']:<18}{regime['definido_em']}")


def listar_regimes():
    print("\n--- Regimes de pausa ---")
    regimes = ler_json(CAMINHO_REGIMES, {})
    exibir_regimes(regimes)
    print("\nObs.: os valores são definidos pela empresa e não correspondem à tabela de nenhuma norma.")


if __name__ == "__main__":
    listar_regimes()