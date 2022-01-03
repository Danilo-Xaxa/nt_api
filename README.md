# [NT API](https://danilo-xaxa.github.io/nt_api/)

<img alt="Print do Index" src="https://github.com/Danilo-Xaxa/nt_api/blob/main/front/screenshot.png"/>

Depois de estudar desenvolvimento de APIs Rest com o framework FastAPI, criei uma conta e um app no [Hubspot](https://www.hubspot.com/)

Então, construi a API com três endpoints:
- Ler dados de contatos (GET)
- Criar um novo contato (POST)
- Atualizar um contato (PUT)

Os três funcionam de forma integrada, a API é capaz de redirecionar para outro endpoint de acordo com os inputs do usuário

O projeto full-stack já está funcionando. [Esse é o link](https://danilo-xaxa.github.io/nt_api/) para testá-lo. Você precisará ter em mãos sua API Key do Hubspot (você pode entrar em contato comigo para usar a minha, se quiser) e rodar o servidor na porta 8000, utilizando o Uvicorn

Para testar o projeto, é necessário instalar antes o FastAPI e o Uvicorn via pip (Python):
- pip install fastapi
- pip install uvicorn

Após isso, para rodar o servidor, usa-se o comando "uvicorn nt_api:app --reload --port 8000". O "nt_api" se refere ao arquivo nt_api.py, que contém a API inteira

Com o servidor rodando na porta 8000, você pode acessar [essa página](https://danilo-xaxa.github.io/nt_api/) e experimentar a visualização, criação e atualização de contatos no Hubspot. A página é bem simples e intuitiva, ela lida com erros básicos e é responsiva também

Além disso, a API funciona perfeitamente por si só recebendo path/query parameters e/ou inputs JSON (body) e retornando outro JSON (executando algo antes também, se esse for o caso)

Essas são as possibilidades:
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
