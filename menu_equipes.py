from subalgoritmo import exibir_menu_equipes, escolha
from equipes import cadastrar_equipe, listar_equipes, editar_equipe, excluir_equipe
from regimes import definir_regime, listar_regimes


def menu_equipes():
    while True:
        exibir_menu_equipes()
        opcao = escolha(6)

        match opcao:
            case 1:
                cadastrar_equipe()
            case 2:
                listar_equipes()
            case 3:
                editar_equipe()
            case 4:
                excluir_equipe()
            case 5:
                definir_regime()
            case 6:
                listar_regimes()
            case 0:
                break

        input("\nPressione Enter para continuar...")