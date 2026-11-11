from entrada import ler_inteiro


def exibir_menu():
    print("""
        \n-------------- PAUSA CERTA | Segurança do trabalho --------------
        0 - SAIR
        1 - Calcular estresse térmico agora
        """)


def escolha(maximo):
    return ler_inteiro("Escolha: ", 0, maximo)


if __name__ == "__main__":
    exibir_menu()
    print(f"Você escolheu: {escolha(1)}")