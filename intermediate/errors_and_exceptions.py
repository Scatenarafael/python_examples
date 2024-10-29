def ler_arquivo(nome_arquivo):
    try:
        arquivo = open(nome_arquivo, "r")
        conteudo = arquivo.read()
        print(conteudo)
    except FileNotFoundError:
        print("Erro: arquivo não encontrado.")
    finally:
        if "arquivo" in locals():
            arquivo.close()
            print("Arquivo fechado.")


class IdadeInvalidaError(Exception):
    def __init__(self, idade, message="Idade inválida para o acesso."):
        self.idade = idade
        self.message = message
        super().__init__(self.message)


def verificar_idade(idade):
    try:
        if idade < 18:
            raise IdadeInvalidaError(idade)
    except IdadeInvalidaError as e:
        print(f"Erro: {e.message} (idade fornecida: {e.idade})")
    else:
        print("Acesso permitido!")


def safe_cast(value):
    try:
        number = int(value)
    except ValueError:
        print("Erro: o valor deve ser um número inteiro.")
    except TypeError:
        print("Erro: o valor fornecido não é válido.")
    else:
        print(f"Conversão bem-sucedida: {number}")
        return number


def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Erro: divisão por zero não é permitida.")
        return None
    else:
        print("Divisão realizada com sucesso!")
        return result
    finally:
        print("Operação concluída.")


print(safe_divide(10, 2))  # Saída: 5.0
print(safe_divide(10, 0))  # Saída: Erro: divisão por zero não é permitida.


def main():
    print(
        "safe_divide >> numerator: 100, denominator: 10, result >>>> ",
        safe_divide(100, 10),
    )
    safe_divide(100, 0)

    safe_cast("abc")  # Saída: Erro: o valor deve ser um número inteiro.
    safe_cast(None)  # Saída: Erro: o valor fornecido não é válido.
    safe_cast("123")  # Saída: Conversão bem-sucedida: 123

    verificar_idade(
        15
    )  # Saída: Erro: Idade inválida para o acesso. (idade fornecida: 15)
    verificar_idade(20)  # Saída: Acesso permitido!
    ler_arquivo(
        "arquivo_inexistente.txt"
    )  # Saída: Erro: arquivo não encontrado. Arquivo fechado.


if __name__ == "__main__":
    main()
