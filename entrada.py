def ler_float(mensagem, minimo, maximo):
    while True:
        try:
            valor = float(input(mensagem).replace(",", "."))
        except ValueError:
            print("Digite um número, por exemplo 37.4.")
            continue
        if minimo <= valor <= maximo:
            return valor
        print(f"O valor precisa estar entre {minimo} e {maximo}.")


def ler_inteiro(mensagem, minimo, maximo):
    while True:
        try:
            valor = int(input(mensagem))
        except ValueError:
            print("Digite um número inteiro, por exemplo 3.")
            continue
        if minimo <= valor <= maximo:
            return valor
        print(f"O valor precisa estar entre {minimo} e {maximo}.")


def ler_opcao(mensagem, opcoes):
    while True:
        valor = input(mensagem).strip().lower()
        if valor in opcoes:
            return valor
        print(f"Opção inválida. Escolha entre: {', '.join(opcoes)}.")


def confirmar(mensagem):
    resposta = ler_opcao(f"{mensagem} (s/n): ", ("s", "n"))
    return resposta == "s"