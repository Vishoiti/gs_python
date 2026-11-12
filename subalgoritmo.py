from entrada import ler_inteiro


def exibir_menu():
    print("""
        \n-------------- PAUSA CERTA | Segurança do trabalho --------------
        0 - SAIR
        1 - Calcular estresse térmico agora
        2 - Equipes e regimes de pausa
        """)


def exibir_menu_equipes():
    print(f"""\n--- Equipes e regimes de pausa ---
                1 - Cadastrar equipe
                2 - Listar equipes
                3 - Editar equipe
                4 - Excluir equipe
                5 - Definir regime de pausa
                6 - Listar regimes
                0 - Voltar
    """)


def escolha(maximo):
    return ler_inteiro("Escolha: ", 0, maximo)