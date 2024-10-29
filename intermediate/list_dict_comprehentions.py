def main():
    # Quadrados de números pares de 0 a 10
    quadrados_pares = [x**2 for x in range(11) if x % 2 == 0]
    print(quadrados_pares)  # Saída: [0, 4, 16, 36, 64, 100]

    # Produto cartesiano de duas listas
    cores = ["vermelho", "verde"]
    objetos = ["carro", "bicicleta"]
    produtos = [(cor, objeto) for cor in cores for objeto in objetos]
    print(produtos)
    # Saída: [('vermelho', 'carro'), ('vermelho', 'bicicleta'), ('verde', 'carro'), ('verde', 'bicicleta')]

    # Dicionário com números e seus quadrados
    quadrados = {x: x**2 for x in range(6)}
    print(quadrados)  # Saída: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

    # Dicionário com números e seus quadrados, mas apenas para números pares
    quadrados_pares = {x: x**2 for x in range(6) if x % 2 == 0}
    print(quadrados_pares)  # Saída: {0: 0, 2: 4, 4: 16}

    # Conjunto de quadrados únicos para números de 0 a 10
    quadrados_unicos = {x**2 for x in range(11)}
    print(quadrados_unicos)  # Saída: {0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100}

    # Conjunto de letras únicas na string
    frase = "Python comprehension"
    letras_unicas = {letra for letra in frase if letra.isalpha()}
    print(
        letras_unicas
    )  # Saída: {'n', 'o', 'y', 'e', 't', 'c', 'm', 'h', 'P', 'p', 'r'}

    # Dicionário original
    idades = {"Ana": 25, "Pedro": 30, "João": 35}

    # Invertendo chaves e valores
    idades_invertidas = {idade: nome for nome, idade in idades.items()}
    print(idades_invertidas)  # Saída: {25: 'Ana', 30: 'Pedro', 35: 'João'}

    palavra = "compreensao"
    contagem_caracteres = {letra: palavra.count(letra) for letra in palavra}
    print(
        contagem_caracteres
    )  # Saída: {'c': 1, 'o': 1, 'm': 1, 'p': 1, 'r': 1, 'e': 2, 'n': 1, 's': 1, 'a': 1, 'o': 1}

    numeros = range(1, 11)
    paridade = {num: ("par" if num % 2 == 0 else "ímpar") for num in numeros}
    print(paridade)
    # Saída: {1: 'ímpar', 2: 'par', 3: 'ímpar', 4: 'par', 5: 'ímpar', 6: 'par', 7: 'ímpar', 8: 'par', 9: 'ímpar', 10: 'par'}

    alunos = {"Turma A": ["Ana", "Pedro"], "Turma B": ["João", "Maria"]}

    # Dicionário com cada aluno e sua respectiva turma
    aluno_turma = {
        aluno: turma for turma, alunos in alunos.items() for aluno in alunos
    }
    print(
        aluno_turma
    )  # Saída: {'Ana': 'Turma A', 'Pedro': 'Turma A', 'João': 'Turma B', 'Maria': 'Turma B'}

    frase = "Set comprehensions em Python"
    caracteres_unicos = {letra.lower() for letra in frase if letra.isalpha()}
    print(
        caracteres_unicos
    )  # Saída: {'c', 'p', 't', 'n', 'o', 'h', 'r', 's', 'm', 'y', 'e'}

    numeros = range(1, 11)
    quadrados_impares = {x**2 for x in numeros if x % 2 != 0}
    print(quadrados_impares)  # Saída: {1, 9, 25, 49, 81}

    frase = "Python é incrível para compreensão de conjuntos e dicionários"
    palavras = {palavra for palavra in frase.split() if len(palavra) > 3}
    print(palavras)
    # Saída: {'compreensão', 'Python', 'conjuntos', 'dicionários', 'incrível', 'para'}

    numero = 12
    divisores = {i for i in range(1, numero + 1) if numero % i == 0}
    print(divisores)  # Saída: {1, 2, 3, 4, 6, 12}


if __name__ == "__main__":
    main()
