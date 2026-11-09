import os
os.system("cls")

from subalgoritmo import exibir_menu, escolha

while True:
    exibir_menu()
    opcao = escolha()

    match opcao:
        case 0:
            print("Obrigado por usar o programa!")
            break

    