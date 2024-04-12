from src.conta_corrente import ContaCorrente
from src.dto.conta_dto import ContaDTO
from fastapi import HTTPException


class ContaCorrenteHandler:
    def __init__(self):
        self.id = 1
        self.db = list()

    def criar(self, conta_info: ContaDTO):
        conta = ContaCorrente(**conta_info.__dict__)
        id = self.id
        self.db.append({"id": id, "data": conta})
        self.id += 1
        return id

    def procurar_pelo_id(self, id: int):
        conta = next((item for item in self.db if item["id"] == id), None)
        if conta is None:
            raise HTTPException(status_code=400, detail="Conta Não existe no banco")
        return conta["data"], self.db.index(conta)

    def saque(self, account_id: int, valor: float):
        conta, index = self.procurar_pelo_id(account_id)
        self.db[index]["data"].sacar(valor)

    def depositar(self, account_id: int, valor: float):
        conta, index = self.procurar_pelo_id(account_id)
        self.db[index]["data"].depositar(valor)

    def busca_saldo(self, id: int):
        conta, index = self.procurar_pelo_id(id)
        return conta.get_saldo()
