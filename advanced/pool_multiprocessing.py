# Pool permite aplicar uma função a vários dados em paralelo de maneira eficiente.

# Explicação: Aqui, Pool cria um grupo de processos e distribui cada item de numeros para ser processado pela função calcular_cubo.
# Isso otimiza o uso de vários núcleos da CPU para uma tarefa intensiva.


from multiprocessing import Pool


# Função para calcular o cubo de um número
def calcular_cubo(n):
    return n * n * n


# Usando Pool para mapear a função a uma lista de dados
with Pool(processes=3) as pool:
    numeros = [1, 2, 3, 4, 5]
    resultados = pool.map(calcular_cubo, numeros)

print("Cubos:", resultados)  # Saída: Cubos: [1, 8, 27, 64, 125]
