import unittest
from src.db_handler import ContaCorrenteHandler
from src.dto.conta_dto import ContaDTO
from fastapi import HTTPException

INDEX_PRIMEIRA_CONTA = 1
INDEX_SEGUNDA_CONTA = 2


class ContaCorrenteHandlerTestCase(unittest.TestCase):

    def test_insert(self):
        db = ContaCorrenteHandler()
        conta = ContaDTO(banco="abc", conta="def", agencia="ghi")
        db.criar(conta)
        self.assertEqual(len(db.db), 1)

    def test_deposito(self):
        db = ContaCorrenteHandler()
        conta = ContaDTO(banco="abc", conta="def", agencia="ghi")
        db.criar(conta)
        db.criar(conta)
        db.depositar(INDEX_PRIMEIRA_CONTA, 10.5)
        db.depositar(INDEX_SEGUNDA_CONTA, 11.5)
        self.assertEqual(db.busca_saldo(INDEX_PRIMEIRA_CONTA), 10.5)
        self.assertEqual(db.busca_saldo(INDEX_SEGUNDA_CONTA), 11.5)

    def test_saque(self):
        db = ContaCorrenteHandler()
        conta = ContaDTO(banco="abc", conta="def", agencia="ghi")
        db.criar(conta)
        db.depositar(INDEX_PRIMEIRA_CONTA, 10.5)
        db.saque(INDEX_PRIMEIRA_CONTA, 9.5)
        self.assertEqual(db.busca_saldo(INDEX_PRIMEIRA_CONTA), 1)


if __name__ == "__main__":
    unittest.main()
