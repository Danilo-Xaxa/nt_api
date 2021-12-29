from os import getenv
from pprint import pprint
from fastapi import FastAPI, HTTPException
from utilidades.models import Contato, ContatoUpdate, db
import hubspot
from hubspot.crm.contacts import ApiException, SimplePublicObjectInput


app = FastAPI()

API_KEY = getenv('HUBSPOT_API_KEY')


@app.get("/")
async def root():
    return {"Mensagem": "Olá mundo!"}


@app.get("/crm/v3/objects/contacts/{api_key}")
async def ler_contato(api_key: str = API_KEY, contact: str = None, properties: str = None):
    client = hubspot.Client.create(api_key=api_key)

    try:
        if properties:
            propriedades = properties.split("-")  # precisa ser vírgula?
            propriedades_originais = propriedades.copy()
            if contact and (not 'email' in propriedades):
                propriedades.append('email')
        else:
            propriedades = ['email', 'telefone', 'niver', 'peso']
            propriedades_originais = propriedades.copy()
        
        api_response = client.crm.contacts.basic_api.get_page(limit=50, archived=False, properties=propriedades)  # limite padrão = 10

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
async def criar_contato(api_key: str = API_KEY, contact: str = None):
    client = hubspot.Client.create(api_key=API_KEY)

    properties = {
        "email": "exemplo@gmail.com",
        "telefone": "81 7070-7070",
        "niver": "2021-12-29",
        "peso": 80.0,
    }

    simple_public_object_input = SimplePublicObjectInput(properties=properties)

    try:
        api_response = client.crm.contacts.basic_api.create(simple_public_object_input=simple_public_object_input)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling basic_api->create: %s\n" % e)


@app.put("/crm/v3/objects/contacts/{api_key}")
async def atualizar_contato(api_key: str = API_KEY, contact: str = None):
    pass
