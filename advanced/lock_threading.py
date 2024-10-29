# Quando várias threads ou processos acessam e modificam dados compartilhados, problemas de concorrência podem ocorrer,
# como a condição de corrida (race condition).
# Em Python, threading fornece locks para resolver esses problemas.
# No caso de multiprocessing, temos Queues para compartilhar dados com segurança entre processos.


# Explicação: Cada thread incrementa a variável contador.
# O uso de lock garante que apenas uma thread acesse contador por vez, evitando condições de corrida.

import threading

# Recurso compartilhado
contador = 0
lock = threading.Lock()


def incrementar():
    global contador
    with lock:  # Usando o lock para garantir acesso exclusivo
        for _ in range(10000000):
            contador += 1


# Criando threads
threads = [threading.Thread(target=incrementar) for _ in range(5)]

# Iniciando threads
for thread in threads:
    thread.start()
    print("starting thread >> ", thread.native_id)

# Aguardando finalização
for thread in threads:
    thread.join()
    print("thread finished...", thread.native_id)

print(f"Contador final: {contador}")
