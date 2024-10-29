import time


def medir_tempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"Tempo de execução: {fim - inicio} segundos")
        return resultado

    return wrapper


# Usando o decorador para medir o tempo da função
@medir_tempo
def somar_numeros(n):
    return sum(range(n))


def repetir_vezes(vezes):
    def decorador(func):
        def wrapper(*args, **kwargs):
            for _ in range(vezes):
                func(*args, **kwargs)

        return wrapper

    return decorador


# Decorando a função com um argumento (vezes = 3)
@repetir_vezes(3)
def diga_oi():
    print("Oi!")


# Definindo um decorador que imprime antes e depois da execução de uma função
def meu_decorador(func):
    def wrapper(*args, **kwargs):
        print("Início da execução da função.")
        resultado = func(*args, **kwargs)
        print("Fim da execução da função.")
        return resultado

    return wrapper


# Usando o decorador com a função saudacao
@meu_decorador
def saudacao(nome):
    print(f"Olá, {nome}!")


def main():
    # Chamando a função decorada
    saudacao("Maria")

    # Chamando a função decorada
    diga_oi()

    # Chamando a função decorada
    somar_numeros(100000000)


if __name__ == "__main__":
    main()
