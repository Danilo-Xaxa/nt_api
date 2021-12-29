from pydantic import BaseModel
from typing import Optional
from typing import List
from models import Contato, ContatoUpdate


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

db: List[Contato] = [
    Contato(
        email="icaroxaxa01@gmail.com",
        telefone="81 99999-9999",
        aniversario="04/07",
        peso=50.0
    ),
    Contato(
        email="sullivanxaxa@gmail.com",
        telefone="81 88888-8888",
        aniversario="24/11",
        peso=100.0,
    ),
]
