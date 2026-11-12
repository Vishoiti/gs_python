from arquivos import ler_json, salvar_json
from entrada import ler_inteiro, ler_opcao, confirmar
from equipes import CAMINHO_EQUIPES, buscar_equipe

CAMINHO_TURNOS = "dados/turnos.json"


def hora_para_minutos(hora):
    partes = hora.split(":")
    return int(partes[0]) * 60 + int(partes[1])


def ler_hora(mensagem):
    while True:
        texto = input(mensagem).strip()
        try:
            partes = texto.split(":")
            horas = int(partes[0])
            minutos = int(partes[1])
        except (ValueError, IndexError):
            print("Digite o horário no formato HH:MM, por exemplo 09:10.")
            continue
        if len(texto) == 5 and 0 <= horas <= 23 and 0 <= minutos <= 59:
            return texto
        print("Horário inválido. Use HH:MM, entre 00:00 e 23:59.")


if __name__ == "__main__":
    print(hora_para_minutos("09:10"))
    print(ler_hora("Horário: "))        