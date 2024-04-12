from pydantic import BaseModel


class ContaDTO(BaseModel):
    banco: str
    agencia: str
    conta: str
