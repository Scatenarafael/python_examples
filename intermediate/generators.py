# Geradores são uma maneira de criar iteradores de forma mais eficiente,
# especialmente em situações onde os dados podem ser produzidos conforme necessário,
# ao invés de carregá-los todos de uma vez na memória.
# Em Python, geradores são definidos com a palavra-chave yield.
import os


# Gerador para ler um arquivo em blocos de um tamanho especificado
def ler_em_blocos(filepath, tamanho_bloco=1024):
    with open(filepath, "rb") as arquivo:
        while True:
            bloco = arquivo.read(tamanho_bloco)
            if not bloco:
                break
            yield bloco


# Gerador para a sequência de Fibonacci
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# Gerador que produz uma sequência infinita de números a partir de um valor inicial
def gerador_infinito(start=0):
    while True:
        yield start
        start += 1


# Gerador que produz uma sequência de números de 0 a n-1
def meu_gerador(n):
    for i in range(n):
        yield i


def ler_arquivo(nome_arquivo):
    try:
        # Usando o gerador para ler e processar blocos de 1024 bytes
        for bloco in ler_em_blocos("arquivo_grande.bin", tamanho_bloco=1024):
            # Processa cada bloco individualmente
            print(bloco)  # ou qualquer outra operação no bloco
    except FileNotFoundError:
        print("Erro: arquivo não encontrado.")
    finally:
        print("Finalizando...")


def main():
    # Usando o gerador
    for numero in meu_gerador(5):
        print(numero)

    # Usando o gerador infinito
    contador = gerador_infinito(10)
    for _ in range(5):
        print(next(contador))
    # Saída:
    # 10
    # 11
    # 12
    # 13
    # 14

    # Usando o gerador Fibonacci
    fib = fibonacci()
    for _ in range(10):
        print(next(fib))
    # Saída: primeiros 10 números da sequência de Fibonacci
    # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
    ler_arquivo(f"{os.path.dirname(os.path.realpath(__file__))}/exemplo.txt")


if __name__ == "__main__":
    main()
