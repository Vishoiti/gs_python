from arquivos import ler_json, salvar_json
from entrada import ler_inteiro, ler_opcao

CAMINHO_EQUIPES = "dados/equipes.json"
TURNOS = ("diurno", "noturno")


def cadastrar_equipe():
    print("\n--- Cadastrar equipe ---")
    equipes = ler_json(CAMINHO_EQUIPES, [])

    codigo = input("Código da equipe (ex.: COL-CAM-07): ").strip().upper()
    if codigo == "":
        print("O código não pode ficar vazio.")
        return

    for equipe in equipes:
        if equipe["codigo"] == codigo:
            print(f"Já existe uma equipe com o código {codigo}.")
            return

    rota = input("Rota: ").strip()
    turno = ler_opcao("Turno (diurno/noturno): ", TURNOS)
    coletores = ler_inteiro("Quantidade de coletores: ", 1, 30)

    equipe = {"codigo": codigo, "rota": rota, "turno": turno, "coletores": coletores}
    equipes.append(equipe)
    salvar_json(CAMINHO_EQUIPES, equipes)
    print(f"Equipe {codigo} cadastrada com sucesso.")


def exibir_equipes(equipes):
    if len(equipes) == 0:
        print("Nenhuma equipe cadastrada.")
        return

    print(f"{'Código':<14}{'Rota':<20}{'Turno':<10}{'Coletores'}")
    print("-" * 52)
    for equipe in equipes:
        print(f"{equipe['codigo']:<14}{equipe['rota']:<20}"
              f"{equipe['turno']:<10}{equipe['coletores']}")


def listar_equipes():
    print("\n--- Equipes cadastradas ---")
    equipes = ler_json(CAMINHO_EQUIPES, [])
    exibir_equipes(equipes)