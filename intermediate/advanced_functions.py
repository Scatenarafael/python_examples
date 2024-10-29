from functools import reduce


def exemplo_args_kwargs(*args, **kwargs):
    print("Argumentos posicionais:", args)
    print("Argumentos nomeados:", kwargs)


def lambda_input(x):
    return x**2


def main():
    exemplo_args_kwargs(1, 2, 3, nome="Alice", idade=30)

    # Lista de tuplas (nome, idade)
    pessoas = [("Alice", 30), ("Bob", 25), ("Carol", 35)]

    # Ordenando pela idade
    pessoas_ordenadas = sorted(pessoas, key=lambda pessoa: pessoa[1])
    print("pessoas_ordenadas >>> ", pessoas_ordenadas)

    numeros = [1, 2, 3, 4, 5]
    quadrados = list(map(lambda_input, numeros))
    print("quadrados >>>> ", quadrados)  # Saída: [1, 4, 9, 16, 25]

    numeros = [1, 2, 3, 4, 5]
    pares = list(filter(lambda x: x % 2 == 0, numeros))
    print(pares)  # Saída: [2, 4]

    numeros = [1, 2, 3, 4, 5]
    soma_total = reduce(lambda x, y: x + y, numeros)
    print(soma_total)  # Saída: 15


if __name__ == "__main__":
    main()
