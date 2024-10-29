import re


def main():
    # Padrão para encontrar um número de telefone no formato (XX) XXXX-XXXX
    texto = "Meu telefone é (11) 91234-5678."
    padrao_telefone = r"\(\d{2}\) \d{4,5}-\d{4}"

    # Usando re.search
    resultado = re.search(padrao_telefone, texto)
    if resultado:
        print(
            "Telefone encontrado:", resultado.group()
        )  # Saída: Telefone encontrado: (11) 91234-5678
    else:
        print("Nenhum telefone encontrado.")

    texto = "Os preços são $45.90, $12.99 e $100.00."
    padrao_preco = r"\$\d+\.\d{2}"

    # Encontrando todos os preços no texto
    precos = re.findall(padrao_preco, texto)
    print(
        "Preços encontrados:", precos
    )  # Saída: Preços encontrados: ['$45.90', '$12.99', '$100.00']

    texto = "Hoje é 29/10/2024. Amanhã será 30/10/2024."
    padrao_data = r"\d{2}/\d{2}/\d{4}"

    # Substituindo a data por 'DATA'
    texto_modificado = re.sub(padrao_data, "DATA", texto)
    print(
        "Texto modificado:", texto_modificado
    )  # Saída: Hoje é DATA. Amanhã será DATA.

    texto = "café, chá; suco: refrigerante"
    padrao_separador = r"[,;:]"

    # Separando a string em itens
    bebidas = re.split(padrao_separador, texto)
    print(
        "Lista de bebidas:", bebidas
    )  # Saída: ['café', ' chá', ' suco', ' refrigerante']

    email = "teste@example.com"
    padrao_email = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    # Verificando se o e-mail é válido
    if re.match(padrao_email, email):
        print("E-mail válido.")
    else:
        print("E-mail inválido.")


if __name__ == "__main__":
    main()
