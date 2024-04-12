import unittest
from src.conta_corrente import ContaCorrente
from fastapi import HTTPException


class MyTestCase(unittest.TestCase):
    def test_deposito(self):
        conta_corrente = ContaCorrente("0001", "0001", "0001")  # add assertion here
        conta_corrente.depositar(200.4)
        self.assertEqual(200.4, conta_corrente.get_saldo())

    def test_saque(self):
        conta_corrente = ContaCorrente("0001", "0001", "0001")  # add assertion here
        conta_corrente.depositar(200.4)
        conta_corrente.sacar(199.4)
        self.assertEqual(1, conta_corrente.get_saldo())


if __name__ == "__main__":
    unittest.main()
