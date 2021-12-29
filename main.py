from fastapi import FastAPI, HTTPException
from typing import List
from models import Contato, ContatoUpdate


app = FastAPI()

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


@app.get("/")
async def root():
    return {"Mensagem": "Olá mundo!"}


@app.get("/api/v1/contatos")
async def fetch_contatos():
    return db


@app.post("/api/v1/contatos")
async def registrar_contato(contato: Contato):
    db.append(contato)
    return {"email": contato.email}


@app.delete("/api/v1/contatos/{email_contato}")
async def deletar_contato(email_contato: str):
    for contato in db:
        if contato.email == email_contato:
            db.remove(contato)
            return {"Mensagem": f"Contato com e-mail {email_contato} deletado com sucesso!"}
    raise HTTPException(
        status_code=404,
        detail=f"Contato com e-mail {email_contato} não encontrado!",
     )


@app.put("/api/v1/contatos/{email_contato}")
async def update_contato(email_contato: str, update_contato: ContatoUpdate):
    for contato in db:
        if contato.email == email_contato:
            if update_contato.email != None:
                contato.email = update_contato.email
            if update_contato.telefone != None:
                contato.telefone = update_contato.telefone
            if update_contato.aniversario != None:
                contato.aniversario = update_contato.aniversario
            if update_contato.peso != None:
                contato.peso = update_contato.peso                   
            return contato
    raise HTTPException(
        status_code=404,
        detail=f"Contato com e-mail {email_contato} não encontrado!",
    )
