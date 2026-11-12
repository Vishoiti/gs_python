from datetime import date, datetime
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


def ler_data(mensagem):
    while True:
        texto = input(mensagem).strip()
        if texto == "":
            return str(date.today())
        try:
            datetime.strptime(texto, "%Y-%m-%d")
        except ValueError:
            print("Data inválida. Use AAAA-MM-DD, por exemplo 2026-11-12.")
            continue
        return texto


def registrar_turno():
    print("\n--- Registrar turno ---")
    equipes = ler_json(CAMINHO_EQUIPES, [])
    if len(equipes) == 0:
        print("Cadastre uma equipe antes de registrar um turno.")
        return

    codigo = input("Código da equipe: ").strip().upper()
    if buscar_equipe(equipes, codigo) is None:
        print(f"Equipe {codigo} não encontrada.")
        return

    data = ler_data("Data do turno (AAAA-MM-DD, Enter para hoje): ")
    inicio = ler_hora("Início da rota (HH:MM): ")
    fim = ler_hora("Fim da rota (HH:MM): ")
    if hora_para_minutos(fim) <= hora_para_minutos(inicio):
        print("O fim precisa ser depois do início.")
        return

    turnos = ler_json(CAMINHO_TURNOS, [])
    for turno in turnos:
        if turno["equipe"] == codigo and turno["data"] == data:
            print(f"A equipe {codigo} já tem um turno registrado em {data}.")
            return

    turno = {
        "equipe": codigo,
        "data": data,
        "inicio": inicio,
        "fim": fim,
        "pausas": [],
        "leituras": [],
    }
    turnos.append(turno)
    salvar_json(CAMINHO_TURNOS, turnos)
    print(f"Turno da equipe {codigo} em {data} registrado.")