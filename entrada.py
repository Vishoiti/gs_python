def ler_float(mensagem, minimo, maximo):
    """Pede um número decimal entre minimo e maximo e repete até ser válido.

    Aceita vírgula ou ponto (34,2 ou 34.2).
    """
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
    """Pede um número inteiro entre minimo e maximo e repete até ser válido."""
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
    """Pede um texto que esteja na tupla opcoes e repete até ser válido.

    Ignora espaços e diferença entre maiúsculas e minúsculas.
    """
    while True:
        valor = input(mensagem).strip().lower()
        if valor in opcoes:
            return valor
        print(f"Opção inválida. Escolha entre: {', '.join(opcoes)}.")


def confirmar(mensagem):
    """Faz uma pergunta de sim ou não e devolve True para sim e False para não."""
    resposta = ler_opcao(f"{mensagem} (s/n): ", ("s", "n"))
    return resposta == "s"