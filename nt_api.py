from fastapi import FastAPI, HTTPException
import hubspot
from hubspot.crm.contacts import ApiException, SimplePublicObjectInput
import requests
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost",
    "http://127.0.0.1",
    "http://127.0.0.1:8000",
    "http://localhost:8000",
    "http://127.0.0.1:8000/",
    "http://localhost:8000/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Contact(BaseModel):
    email: str
    telefone: str
    niver: str
    peso: float

class UpdateContact(BaseModel):
    email: Optional[str] = None
    telefone: Optional[str] = None
    niver: Optional[str] = None
    peso: Optional[float] = None
    

@app.get("/")
async def index():
    return {"Olá!": "Sejam bem-vindos à NT API"}


@app.get("/crm/v3/objects/contacts/{api_key}")
async def ler_contatos(api_key: str, properties: str = None, contact: str = None):
    client = hubspot.Client.create(api_key=api_key)

    try:
        if properties:
            propriedades = properties.split("-")
            propriedades_originais = propriedades.copy()
            if contact and (not 'email' in propriedades):
                propriedades.append('email')
        else:
            propriedades = ['email', 'telefone', 'niver', 'peso']
            propriedades_originais = propriedades.copy()
        
        api_response = client.crm.contacts.basic_api.get_page(limit=50, archived=False, properties=propriedades)

        propriedades_contatos = []
        for resultado in api_response.results:
            propriedades_contatos.append({
                chave: resultado.properties[chave] for chave in propriedades
            })
            
            if contact:
                for propriedades_contato in propriedades_contatos:
                    if propriedades_contato['email'] == contact:
                        return propriedades_contato if propriedades == propriedades_originais else {
                            k : v for k, v in propriedades_contato.items() if k != 'email'
                        }
                        
        return propriedades_contatos

    except ApiException as e:
        print("Exception when calling basic_api->get_page: %s\n" % e)
        return HTTPException(status_code=500, detail="Erro ao buscar contatos")


@app.post("/crm/v3/objects/contacts/{api_key}")
async def criar_contato(api_key: str, body: Contact):
    client = hubspot.Client.create(api_key=api_key)

    try:
        properties = dict(body)
    except Exception as e:
        print(e)
        return HTTPException(status_code=400, detail="Erro no JSON")

    todos_contatos = await ler_contatos(api_key=api_key)
    if [contato for contato in todos_contatos if contato['email'] == properties['email']]:
        if not properties.keys() >= {'email', 'telefone', 'niver', 'peso'}:
            return HTTPException(status_code=400, detail="Propriedade não informada para alterar contato")
        return await atualizar_contato(api_key=api_key, body=body, contact=properties['email'])

    properties['peso'] = str(properties['peso'])
    if properties in todos_contatos:
        return HTTPException(status_code=400, detail="Contato exatamente igual já existe")

    try:
        properties['peso'] = float(properties['peso'])
        simple_public_object_input = SimplePublicObjectInput(properties=properties)
        api_response = client.crm.contacts.basic_api.create(simple_public_object_input=simple_public_object_input)
        return properties
    except ApiException as e:
        print("Exception when calling basic_api->create: %s\n" % e)
        return HTTPException(status_code=500, detail="Erro ao criar contato")


@app.put("/crm/v3/objects/contacts/{api_key}/{contact}")
async def atualizar_contato(api_key: str, body: UpdateContact, contact: str):
    client = hubspot.Client.create(api_key=api_key)

    try:
        properties = dict(body)
    except Exception as e:
        return HTTPException(status_code=400, detail="Erro no JSON")

    todos_contatos = await ler_contatos(api_key=api_key)

    for c in todos_contatos:
        if c['email'] == contact:
            contato_antigo = c
            break

    if 'contato_antigo' not in locals():
        if not properties.keys() >= {'email', 'telefone', 'niver', 'peso'}:
            return HTTPException(status_code=400, detail="Propriedade não informada para criar contato")
        elif properties['email'] != contact:
            return HTTPException(status_code=400, detail="Contato não encontrado")
        return await criar_contato(api_key=api_key, body=body)

    properties['peso'] = str(properties['peso'])
    if properties in todos_contatos:
        return HTTPException(status_code=400, detail="Contato exatamente igual já existe")

    resposta = requests.get(f"https://api.hubapi.com/contacts/v1/contact/emails/batch/?email={contact}&hapikey={api_key}").json()
    contact_id = [*resposta][0]

    if not contact_id:
        return HTTPException(status_code=400, detail="Contato não encontrado")

    properties = {k: v for k, v in properties.items() if v not in [None, 'None']}
    properties = {**contato_antigo, **properties}

    try:
        properties['peso'] = float(properties['peso'])
        simple_public_object_input = SimplePublicObjectInput(properties=properties)
        api_response = client.crm.contacts.basic_api.update(contact_id=contact_id, simple_public_object_input=simple_public_object_input)
        return properties
    except ApiException as e:
        print("Exception when calling basic_api->update: %s\n" % e)
        return HTTPException(status_code=500, detail="Erro ao atualizar contato")
