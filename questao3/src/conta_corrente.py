from src.conta import Conta
from fastapi import HTTPException


class ContaCorrente(Conta):
    def __init__(self, banco, agencia, conta):
        super().__init__(banco, agencia, conta)
        self.saldo = 0

    def depositar(self, valor: float):
        self.saldo = self.saldo + valor

    def sacar(self, valor: float):
        if not self.__is_valid_sacar(valor):
            raise HTTPException(
                status_code=400, detail="O valor especificado é maior que o saldo"
            )
        self.saldo = self.saldo - valor

    def __is_valid_sacar(self, valor: float) -> bool:
        return self.saldo >= valor

    def get_saldo(self):
        return self.saldo
