from datetime import datetime, timedelta, timezone


def main():
    # Data e horário atuais
    agora = datetime.now()
    print("Data e hora atuais:", agora)

    # Data e horário específicos
    data_especifica = datetime(2023, 10, 29, 15, 30, 0)
    print("Data e hora específica:", data_especifica)

    # Formatando data para diferentes padrões
    data = datetime.now()

    # Formatos comuns
    print("Formato completo:", data.strftime("%Y-%m-%d %H:%M:%S"))
    print("Data curta:", data.strftime("%d/%m/%Y"))
    print("Hora apenas:", data.strftime("%H:%M"))

    # Exemplo com dia da semana
    print("Dia da semana:", data.strftime("%A"))

    # Datas específicas
    inicio = datetime(2023, 10, 29)
    fim = datetime(2024, 10, 29)

    # Diferença entre as datas
    diferenca = fim - inicio
    print("Diferença em dias:", diferenca.days)

    # Adicionando e subtraindo tempo com timedelta
    uma_semana = timedelta(weeks=1)
    data_daqui_uma_semana = inicio + uma_semana
    print("Data daqui a uma semana:", data_daqui_uma_semana)

    data1 = datetime(2023, 10, 29)
    data2 = datetime(2024, 10, 29)

    # Comparando datas
    if data1 < data2:
        print("data1 é anterior a data2")
    elif data1 > data2:
        print("data1 é posterior a data2")
    else:
        print("As datas são iguais")

    # Obtenha a data e hora atuais no fuso horário UTC
    agora_utc = datetime.now(timezone.utc)

    # Formate para o padrão ISO 8601 (com sufixo 'Z' indicando UTC)
    print(
        "Formato UTC ISO 8601:", agora_utc.isoformat()
    )  # Ex: 2023-10-29T15:30:00+00:00

    # Alternativamente, formatar manualmente com strftime
    print(
        "Formato UTC com strftime:", agora_utc.strftime("%Y-%m-%d %H:%M:%S %Z")
    )  # Ex: 2023-10-29 15:30:00 UTC


if __name__ == "__main__":
    main()
