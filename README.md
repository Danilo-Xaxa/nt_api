# [NT API](https://danilo-xaxa.github.io/nt_api/)

<img alt="Print do Index" src="https://github.com/Danilo-Xaxa/nt_api/blob/main/screenshot.png"/>

Depois de estudar desenvolvimento de APIs Rest com o framework FastAPI, criei uma conta e um app no [Hubspot](https://www.hubspot.com/)

Então, construi a API com três endpoints:
- Ler dados de contatos (GET)
- Criar um novo contato (POST)
- Atualizar um contato (PUT)

Os três funcionam de forma integrada, a API é capaz de redirecionar para outro endpoint de acordo com os inputs do usuário

Por si só, a API funciona perfeitamente recebendo path/query parameters e/ou inputs JSON (body) e retornando outro JSON (executando algo antes também, se esse for o caso)

Para testar a API sozinha, é necessário instalar o FastAPI e o Uvicorn via pip (Python):
- pip install fastapi
- pip install uvicorn

Com os arquivos do repositório já baixados, é preciso entrar no diretório certo (/nt_api)

Após isso, para rodar o servidor, usa-se o comando "uvicorn nt_api:app". O "nt_api" se refere ao arquivo nt_api.py, que contém a API inteira

Com o servidor rodando na porta 8000, essas são as possibilidades:
* GET:
    * padrão: http://127.0.0.1:8000/crm/v3/objects/contacts/{api_key_aqui}
    * com properties: http://127.0.0.1:8000/crm/v3/objects/contacts/{api_key_aqui}?properties=telefone-peso
    * com contact: http://127.0.0.1:8000/crm/v3/objects/contacts/{api_key_aqui}?contact=exemplo@gmail.com
    * com properties e contact: http://127.0.0.1:8000/crm/v3/objects/contacts/{api_key_aqui}?properties=telefone-peso&contact=exemplo@gmail.com

- POST:
    * http://127.0.0.1:8000/crm/v3/objects/contacts/{api_key_aqui} ->
    body: {
        json_aqui
    }

- PUT:
    * http://127.0.0.1:8000/crm/v3/objects/contacts/{api_key_aqui}/exemplo@gmail.com ->
    body: {
        json_aqui
    }
