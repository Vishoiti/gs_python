import os
os.system("cls")

from subalgoritmo import exibir_menu, escolha
from calculadora import calcular_estresse_termico
from submenus import menu_equipes, menu_turnos


def main():
    while True:
        exibir_menu()
        opcao = escolha(3)

        match opcao:
            case 0:
                print("Encerrando o Pausa Certa. Até logo!")
                break
            case 1:
                calcular_estresse_termico()
            case 2:
                menu_equipes()