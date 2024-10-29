def dict_tests():
    dados_cliente1 = {
        "Nome": "Renan",
        "Endereco": "Rua Cruzeiro do Sul",
        "Telefone": "982503645",
    }
    dados_cliente2 = {
        "Nome": "Ronaldo",
        "Endereco": "Rua Padre Anchieta do Sul",
        "Telefone": "983313645",
    }

    clientes = [dados_cliente1, dados_cliente2]

    print(clientes)

    clientes.append(
        {"Nome": "John", "Endereço": "Av da saudade", "Telefone": "-"}
    )

    print(clientes)

    print(
        [
            *clientes,
            {"Nome": "Edu", "Endereço": "Av do sabiá", "Telefone": "-"},
        ]
    )


def tuple_tests():
    tuple1 = ("João", "Douglas")
    print(tuple1)
    tuple2 = (*tuple1, "Douglas Alterado")
    print(tuple2)


def list_tests():
    array1 = ["João", "Douglas"]
    print(array1)
    array1[1] = "Douglas Alterado"
    print(array1)


def string_format():
    txt = "For only {price:.2f} dollars!"
    print(txt.format(price=49))


def basic_join():
    lista_de_palavras = ["Ola", "mundo!"]
    stringa_join = " ".join(lista_de_palavras)

    print("basic_join >>> ", stringa_join)


def main():
    basic_join()
    string_format()
    list_tests()
    tuple_tests()
    dict_tests()


if __name__ == "__main__":
    main()
