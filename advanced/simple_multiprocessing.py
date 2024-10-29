# No multiprocessing, cada processo é isolado em sua própria memória, o que é vantajoso para tarefas intensivas de CPU.

# Explicação: Cada processo executa tarefa_cpu, que realiza cálculos independentes.
# Como cada processo roda em seu próprio espaço de memória, o multiprocessing permite que ambos rodem em paralelo.


import multiprocessing


# Função que simula uma operação intensiva de CPU (ex.: cálculo)
def tarefa_cpu(n):
    print(f"Iniciando cálculo com n={n}")
    resultado = sum(i * i for i in range(n))
    print(f"Finalizando cálculo com n={n}, resultado: {resultado}")


# Criando e iniciando processos
processo1 = multiprocessing.Process(target=tarefa_cpu, args=(1000000,))
processo2 = multiprocessing.Process(target=tarefa_cpu, args=(2000000,))

# Iniciando os processos
processo1.start()
processo2.start()

# Aguardando a finalização dos processos
processo1.join()
processo2.join()

print("Todos os processos finalizaram.")
