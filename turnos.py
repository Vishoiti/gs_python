from datetime import date, datetime
from arquivos import ler_json, salvar_json
from entrada import ler_float, ler_inteiro, ler_opcao, confirmar
from equipes import CAMINHO_EQUIPES, buscar_equipe
from calor import indice_calor, nivel_por_indice

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


def buscar_turno(turnos, codigo, data):
    for turno in turnos:
        if turno["equipe"] == codigo and turno["data"] == data:
            return turno
        return None


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


def registrar_pausa():
    print("\n--- Registrar pausa ---")
    turnos = ler_json(CAMINHO_TURNOS, [])
    if len(turnos) == 0:
        print("Nenhum turno registrado.")
        return

    codigo = input("Código da equipe: ").strip().upper()
    data = ler_data("Data do turno (AAAA-MM-DD, Enter para hoje): ")
    turno = buscar_turno(turnos, codigo, data)
    if turno is None:
        print(f"Não há turno da equipe {codigo} em {data}.")
        return

    print(f"Turno de {turno['inicio']} a {turno['fim']}.")
    inicio = ler_hora("Início da pausa (HH:MM): ")
    fim = ler_hora("Fim da pausa (HH:MM): ")

    inicio_min = hora_para_minutos(inicio)
    fim_min = hora_para_minutos(fim)
    if fim_min <= inicio_min:
        print("O fim da pausa precisa ser depois do início.")
        return
    if (inicio_min < hora_para_minutos(turno["inicio"]) or fim_min > hora_para_minutos(turno["fim"])):
        print("A pausa precisa estar dentro do horário do turno.")
        return

    turno["pausas"].append([inicio, fim])
    salvar_json(CAMINHO_TURNOS, turnos)
    print(f"Pausa de {inicio} a {fim} registrada.")


def registrar_leitura():
    print("\n--- Registrar leitura de calor ---")
    turnos = ler_json(CAMINHO_TURNOS, [])
    if len(turnos) == 0:
        print("Nenhum turno registrado.")
        return

    codigo = input("Código da equipe: ").strip().upper()
    data = ler_data("Data do turno (AAAA-MM-DD, Enter para hoje): ")
    turno = buscar_turno(turnos, codigo, data)
    if turno is None:
        print(f"Não há turno da equipe {codigo} em {data}.")
        return

    print(f"Turno de {turno['inicio']} a {turno['fim']}.")
    hora = ler_hora("Horário da leitura (HH:MM): ")
    hora_min = hora_para_minutos(hora)
    if (hora_min < hora_para_minutos(turno["inicio"]) or hora_min > hora_para_minutos(turno["fim"])):
        print("A leitura precisa estar dentro do horário do turno.")
        return

    temperatura = ler_float("Temperatura do ar (°C): ", -20, 50)
    umidade = ler_float("Umidade relativo (%): ", 5, 99)

    ic = indice_calor(temperatura, umidade)
    estado = nivel_por_indice(ic)

    turno["leituras"].append({
        "hora": hora,
        "indiceCalor_c": round(ic, 1),
        "estado": estado,
    })
    salvar_json(CAMINHO_TURNOS, turnos)
    print(f"Leitura das {hora} registrada: {ic:.1f} °C, estado {estado}.")


def exibir_turnos(turnos):
    if len(turnos) == 0:
        print("Nenhum turno encontrado.")
        return

    print(f"{'Data':<12}{'Inicio':<8}{'fim':<8}{'Pausas':<8}{'Leituras'}")
    print("-" * 46)
    for turno in turnos:
        print(f"{turno['data']:<12}{turno['inicio']:<8}{turno['fim']:<8}"
              f"{len(turno['pausas']):<8}{len(turno['leituras'])}")


def listar_turnos():
    print("\n--- Turnos de uma equipe ---")
    turnos = ler_json(CAMINHO_TURNOS, [])
    codigo = input("Código da equipe: ").strip().upper()

    turnos_da_equipe = []
    for turno in turnos:
        if turno["equipe"] == codigo:
            turnos_da_equipe.append(turno)

    print(f"\nEquipe {codigo}")
    exibir_turnos(turnos_da_equipe)