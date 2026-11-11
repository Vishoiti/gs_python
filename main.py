import os
os.system("cls")

from subalgoritmo import exibir_menu, escolha
from calculadora import calcular_estresse_termico

def main():
    while True:
        exibir_menu()
        opcao = escolha(1)

        match opcao:
            case 0:
                print("Encerrando o Pausa Certa. Até logo!")
                break
            case 1:
                calcular_estresse_termico()


if __name__ == "__main__":
    main()    