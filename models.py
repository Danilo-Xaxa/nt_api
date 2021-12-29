from pydantic import BaseModel
from typing import Optional


class Contato(BaseModel):
    email: str
    telefone: str
    aniversario: str
    peso: float

class ContatoUpdate(BaseModel):
    email: Optional[str]
    telefone: Optional[str]
    aniversario: Optional[str]
    peso: Optional[float]
