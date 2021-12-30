from fastapi import FastAPI, HTTPException, Request
import hubspot
from hubspot.crm.contacts import ApiException, SimplePublicObjectInput
import requests
from os import getenv


app = FastAPI()

API_KEY = getenv('HUBSPOT_API_KEY')


@app.get("/")
async def index():
    return {"Olá!": "Sejam bem-vindos à NT API"}


@app.get("/crm/v3/objects/contacts/{api_key}")
async def ler_contatos(api_key: str = API_KEY, contact: str = None, properties: str = None):
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
async def criar_contato(api_key: str = API_KEY, request: Request = None):
    client = hubspot.Client.create(api_key=api_key)

    try:
        properties = await request.json()
    except Exception as e:
        return HTTPException(status_code=400, detail="Erro no JSON")

    todos_contatos = await ler_contatos(api_key=api_key)
    if [contato for contato in todos_contatos if contato['email'] == properties['email']]:
        if not dict(properties).keys() >= {'email', 'telefone', 'niver', 'peso'}:
            return HTTPException(status_code=400, detail="Propriedade não informada para criar contato")
        return await atualizar_contato(api_key=api_key, request=request, contact=dict(properties)['email'])

    try:
        simple_public_object_input = SimplePublicObjectInput(properties=properties)
        api_response = client.crm.contacts.basic_api.create(simple_public_object_input=simple_public_object_input)
        return properties
    except ApiException as e:
        print("Exception when calling basic_api->create: %s\n" % e)
        return HTTPException(status_code=500, detail="Erro ao criar contato")


@app.put("/crm/v3/objects/contacts/{api_key}/{contact}")
async def atualizar_contato(api_key: str = API_KEY, contact: str = None, request: Request = None):
    if not contact:
        return HTTPException(status_code=400, detail="Contato não informado")

    client = hubspot.Client.create(api_key=api_key)

    try:
        properties = await request.json()
    except Exception as e:
        return HTTPException(status_code=400, detail="Erro no JSON")

    todos_contatos = await ler_contatos(api_key=api_key)

    if not [contato for contato in todos_contatos if contato['email'] == contact]:
        if not dict(properties).keys() >= {'email', 'telefone', 'niver', 'peso'}:
            return HTTPException(status_code=400, detail="Propriedade não informada para criar contato")
        return await criar_contato(api_key=api_key, request=request)

    resposta = requests.get(f"https://api.hubapi.com/contacts/v1/contact/emails/batch/?email={contact}&hapikey={api_key}").json()
    contact_id = [*resposta][0]

    try:
        simple_public_object_input = SimplePublicObjectInput(properties=properties)
        api_response = client.crm.contacts.basic_api.update(contact_id=contact_id, simple_public_object_input=simple_public_object_input)
        return properties
    except ApiException as e:
        print("Exception when calling basic_api->update: %s\n" % e)
        return HTTPException(status_code=500, detail="Erro ao atualizar contato")
