# Sim, é possível executar várias threads dentro de um processo do multiprocessing em Python.
# No entanto, o uso de threads dentro de processos para melhorar a performance tem suas nuances.
# Quando o uso de Threads dentro de Processos ajuda na Performance

# Operações de I/O: Se uma função de processamento precisa realizar operações de entrada e saída (como acessar arquivos,
# banco de dados ou fazer chamadas de rede), as threads dentro de processos podem ser vantajosas,
# pois threads podem executar tarefas de I/O enquanto aguardam respostas, aumentando o desempenho.

# GIL (Global Interpreter Lock): Em Python, o GIL impede que múltiplas threads rodem simultaneamente no mesmo processo em tarefas de CPU.
# Com o multiprocessing, criamos múltiplos processos que não compartilham o GIL.
# Isso permite que cada processo execute suas próprias threads para tarefas de I/O sem ser bloqueado pelo GIL.

# No entanto, se o objetivo for melhorar o desempenho de operações intensivas de CPU,
# adicionar threads dentro de processos geralmente não traz ganhos, pois cada thread será limitada pelo GIL.
# Nesses casos, usar somente multiprocessing para paralelismo real geralmente é mais eficiente.

# No exemplo abaixo, cada processo roda uma tarefa que executa várias chamadas de I/O simuladas em threads.


import multiprocessing
import threading
import time


# Função simulando uma tarefa de I/O
def tarefa_io(thread_id):
    print(f"Thread {thread_id} iniciando I/O.")
    time.sleep(2)  # Simula tempo de I/O
    print(f"Thread {thread_id} finalizou I/O.")


# Função que cria várias threads dentro de um processo
def processo_com_threads(n_threads):
    threads = []
    for i in range(n_threads):
        thread = threading.Thread(target=tarefa_io, args=(i,))
        thread.start()
        threads.append(thread)

    # Aguarda a finalização de todas as threads
    for thread in threads:
        thread.join()
    print("Todas as threads no processo finalizaram.")


# Número de processos e threads por processo
n_processos = 3
n_threads_por_processo = 4

# Criando e iniciando os processos com threads internas
processos = []
for _ in range(n_processos):
    processo = multiprocessing.Process(
        target=processo_com_threads, args=(n_threads_por_processo,)
    )
    processo.start()
    processos.append(processo)

# Aguardando a finalização dos processos
for processo in processos:
    processo.join()

print("Todos os processos finalizaram.")
