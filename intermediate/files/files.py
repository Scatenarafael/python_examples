import csv
import json
import os
import pickle


def write_read_serializeble_file():
    # Objeto complexo para serializar
    dados = {
        "nome": "Alice",
        "idade": 30,
        "cidade": "São Paulo",
        "habilidades": ["Python", "Machine Learning"],
    }

    # Serializando dados com pickle
    with open(
        f"{os.path.dirname(os.path.realpath(__file__))}/dados.pkl", "wb"
    ) as pklfile:
        pickle.dump(dados, pklfile)

    # Carregando dados serializados com pickle
    with open(
        f"{os.path.dirname(os.path.realpath(__file__))}/dados.pkl", "rb"
    ) as pklfile:
        dados_carregados = pickle.load(pklfile)
        print(dados_carregados)


def write_read_json_file():
    dados = {
        "nome": "Alice",
        "idade": 30,
        "cidade": "São Paulo",
        "habilidades": ["Python", "Machine Learning"],
    }

    # Serializando dados em JSON e salvando em um arquivo
    with open(
        f"{os.path.dirname(os.path.realpath(__file__))}/dados.json", "w"
    ) as jsonfile:
        json.dump(dados, jsonfile)

    # Lendo e desserializando dados JSON de um arquivo
    with open(
        f"{os.path.dirname(os.path.realpath(__file__))}/dados.json", "r"
    ) as jsonfile:
        dados_carregados = json.load(jsonfile)
        print(dados_carregados)


def write_read_csv_file():
    # Escrita em um arquivo CSV
    with open(
        f"{os.path.dirname(os.path.realpath(__file__))}/exemplo.csv",
        "w",
        newline="",
    ) as csvfile:
        escritor = csv.writer(csvfile)
        escritor.writerow(["Nome", "Idade", "Cidade"])
        escritor.writerow(["Alice", 30, "São Paulo"])
        escritor.writerow(["Bob", 25, "Rio de Janeiro"])

    # Leitura do arquivo CSV
    with open(
        f"{os.path.dirname(os.path.realpath(__file__))}/exemplo.csv", "r"
    ) as csvfile:
        leitor = csv.reader(csvfile)
        for linha in leitor:
            print(linha)


def write_read_files():
    # Escrita em um arquivo de texto
    print(f"{os.path.dirname(os.path.realpath(__file__))}/exemplo.txt")
    with open(
        f"{os.path.dirname(os.path.realpath(__file__))}/exemplo.txt", "w"
    ) as arquivo:
        arquivo.write("Linha 1\n")
        arquivo.write("Linha 2\n")
        arquivo.write("Linha 3\n")

    # Leitura do arquivo de texto
    with open(
        f"{os.path.dirname(os.path.realpath(__file__))}/exemplo.txt", "r"
    ) as arquivo:
        conteudo = arquivo.read()
        print(conteudo)


def main():
    write_read_files()
    write_read_csv_file()
    write_read_json_file()
    write_read_serializeble_file()


if __name__ == "__main__":
    main()
