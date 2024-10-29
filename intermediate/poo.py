class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, percentual):
        self.preco *= 1 - percentual / 100

    def __str__(self):
        return f"Produto(nome={self.nome}, preco=R${self.preco:.2f})"

    def __repr__(self):
        return f"Produto('{self.nome}', {self.preco})"


class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        raise NotImplementedError("Subclasses devem implementar este método")


class Cachorro(Animal):
    def falar(self):
        return "Au Au!"


class Gato(Animal):
    def falar(self):
        return "Miau!"


class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo  # Atributo privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depositado: R${valor}")

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Sacado: R${valor}")
        else:
            print("Saldo insuficiente.")

    def mostrar_saldo(self):
        print(f"Saldo de {self.titular}: R${self.__saldo}")


class Carro:
    # Construtor da classe
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def mostrar_detalhes(self):
        print(f"{self.marca} {self.modelo} ({self.ano})")


def main():
    # Criando um objeto
    carro1 = Carro("Toyota", "Corolla", 2020)
    carro1.mostrar_detalhes()  # Saída: Toyota Corolla (2020)

    # Criando um objeto e manipulando saldo
    conta = ContaBancaria("Alice", 1000)
    conta.depositar(200)  # Depositado: R$200
    conta.sacar(500)  # Sacado: R$500
    conta.mostrar_saldo()  # Saldo de Alice: R$700
    # Acessar __saldo diretamente resultaria em erro

    # Uso do polimorfismo
    animais = [Cachorro("Rex"), Gato("Felix")]

    for animal in animais:
        print(f"{animal.nome} diz: {animal.falar()}")

    # Criando e manipulando o produto
    produto = Produto("Notebook", 3000)
    print(produto)  # Saída: Produto(nome=Notebook, preco=R$3000.00)
    produto.aplicar_desconto(10)
    print(produto)  # Saída: Produto(nome=Notebook, preco=R$2700.00)
    print(repr(produto))  # Saída: Produto('Notebook', 2700.0)


if __name__ == "__main__":
    main()
