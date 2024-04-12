class Conta:
    def __init__(self, banco: str, agencia: str, conta: str):
        self.banco = banco
        self.agencia = agencia
        self.conta = conta

    def depositar(self, valor: float):
        raise Exception("Método não implementado")

    def sacar(self, valor: float):
        raise Exception("Método não implementado")
