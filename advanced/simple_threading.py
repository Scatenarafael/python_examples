# Aqui, usamos threading para rodar várias tarefas de entrada/saída simultaneamente, como fazer requisições para diferentes URLs.

# Explicação: Cada thread roda a função tarefa_io, que simula uma operação de I/O.
# As threads são iniciadas simultaneamente e o programa principal aguarda (join) até que ambas terminem.

import threading
import time


# Função que simula uma tarefa de I/O (ex.: requisição web)
def tarefa_io(nome, tempo):
    print(f"Iniciando {nome}")
    time.sleep(tempo)  # Simula espera
    print(f"Finalizando {nome}")


# Criando e iniciando threads
thread1 = threading.Thread(target=tarefa_io, args=("Thread 1", 2))
thread2 = threading.Thread(target=tarefa_io, args=("Thread 2", 3))

# Iniciando as threads
thread1.start()
thread2.start()

# Aguardando a finalização das threads
thread1.join()
thread2.join()
print("Todas as threads finalizaram.")
