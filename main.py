import os
os.system("cls")

from subalgoritmo import exibir_menu, escolha


def main():
    while True:
        exibir_menu()
        opcao = escolha(1)

        match opcao:
            case 0:
                print("Encerrando o Pausa Certa. Até logo!")
                break
            case 1:
                print("Calculadora de estresse térmico (em construção).")


if __name__ == "__main__":
    main()    