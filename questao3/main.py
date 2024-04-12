from fastapi import FastAPI
from starlette import status

from src.db_handler import ContaCorrenteHandler
from src.dto.conta_dto import ContaDTO

app = FastAPI()

db = ContaCorrenteHandler()


@app.post("/contas/", status_code=status.HTTP_201_CREATED)
async def cadastra_conta(conta: ContaDTO):
    id = db.criar(conta)
    return {"id": id}


@app.put("/contas/{id}/credito")
async def creditar_conta(id: int, valor: float):
    db.saque(id, valor)


@app.put("/contas/{id}/debito")
async def debitar_conta(id: int, valor: float):
    db.depositar(id, valor)


@app.get("/contas/{id}/saldo")
async def consulta_saldo_conta(id: int):
    return {"valor": db.busca_saldo(id)}
