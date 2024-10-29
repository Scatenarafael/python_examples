# Para compartilhar dados entre processos, utilizamos Queue no multiprocessing, que permite comunicação segura entre processos.

# Explicação: Aqui, o processo calcular_quadrado coloca os resultados dos cálculos na Queue.
# O programa principal recupera esses resultados da fila após o término do processo.


import multiprocessing


def calcular_quadrado(numeros, queue: multiprocessing.Queue):
    print("calcular quadrado")
    for n in numeros:
        queue.put(n * n)  # Coloca o resultado na fila


# Lista de números e fila compartilhada
numeros = [1, 2, 3, 4, 5]
queue = multiprocessing.Queue()

# Criando e iniciando o processo
processo = multiprocessing.Process(
    target=calcular_quadrado, args=(numeros, queue)
)
processo.start()
processo.join()

# Obtendo resultados da fila
resultados = []
while not queue.empty():
    print("queue.qsize() >>> ", queue.qsize())
    resultados.append(queue.get())

print("Quadrados:", resultados)  # Saída: Quadrados: [1, 4, 9, 16, 25]
