from calor import (indice_calor, bulbo_umido, ibutg_estimado,
                   nivel_por_indice, acao_do_estado)
from entrada import ler_float


def calcular_estresse_termico():
    print("\n--- Calculadora de estresse térmico ---")
    temperatura = ler_float("Temperatura do ar (°C): ", -20, 50)
    umidade = ler_float("Umidade relativa (%): ", 5, 99)
    globo = ler_float("Temperatura de globo (°C): ", -20, 90)

    ic = indice_calor(temperatura, umidade)
    tbu = bulbo_umido(temperatura, umidade)
    ibutg = ibutg_estimado(tbu, globo, temperatura)
    estado = nivel_por_indice(ic)

    print(f"""
        \n--- Resultado ---
        Índice de calor: {ic:.1f} °C
        Bulbo úmido: {tbu:.1f} °C
        IBUTG estimado: {ibutg:.1f} °C
        Estado: {estado}
        Ação: {acao_do_estado(estado)}
        \nAtenção: o IBUTG é uma estimativa e não substitui a medição da NHO 06.""")
    input("\nPressione Enter para voltar ao menu...")    