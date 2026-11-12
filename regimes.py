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
        "mimutos_pausa": minutos_pausa,
        "max_sem_pausa_critico": max_sem_pausa,
        "responsavel": responsavel,
        "definido_em": str(date.today()),
    }
    salvar_json(CAMINHO_REGIMES, regimes)
    print(f"Regime da equipe {codigo} salvo.")