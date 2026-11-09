def exibir_menu():
    print("""
        0 - SAIR
        """)        

def ler_inteiro(mensagem: str, minimo: int, maximo: int) -> int: 
    while True:
        try:
            valor = int(input(mensagem))
            if minimo <= valor <= maximo:
                return valor
            print(f"Digite um número entre {minimo} e {maximo}.")
        except ValueError:
            print("Entrada inválida. Digite apenas números.")

def escolha():
    return ler_inteiro("Escolha: ", 0, 0)