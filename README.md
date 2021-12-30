# NT API

<img src="https://github.com/Danilo-Xaxa/nt_api/blob/main/screenshot.png"/>

Comecei o projeto estudando o framework FastAPI por [esse vídeo](https://www.youtube.com/watch?v=GN6ICac3OXY) do canal AmigosCode

Depois de entender como uma API Rest pode ser desenvolvida, criei uma conta e um app no [Hubspot](https://www.hubspot.com/)

Então decidi construir a API com três endpoints:
- Ler dados de contatos (GET)
- Criar um novo contato (POST)
- Atualizar um contato (PUT)

Os três funcionam de forma integrada, a API é capaz de redirecionar para outro endpoint de acordo com o input do usuário

Por si só, a API já funciona perfeitamente recebendo inputs JSON (body) e retornando outro JSON (executando algo antes também, se for o caso)

Para testar a API sozinha, é importante instalar o FastAPI e o Uvicorn:
- pip install fastapi
- pip install uvicorn

Com os arquivos do repositório já baixados, só precisa entrar no diretório certo (/nt_api)

Após isso, para rodar o servidor, usa-se o comando "uvicorn nt_api:app". O "nt_api" se refere ao arquivo nt_api.py, que contém a API inteira

Com o servidor rodando, essas são as possibilidades:
* GET:
    * padrão: http://127.0.0.1:8000/crm/v3/objects/contacts/api_key_aqui
    * com properties: http://127.0.0.1:8000/crm/v3/objects/contacts/api_key_aqui?properties=telefone-peso
    * com contact: http://127.0.0.1:8000/crm/v3/objects/contacts/api_key_aqui?contact=julian@gmail.com
    * com properties e contact: http://127.0.0.1:8000/crm/v3/objects/contacts/api_key_aqui?properties=telefone-peso&contact=julian@gmail.com

- POST:
    * http://127.0.0.1:8000/crm/v3/objects/contacts/api_key_aqui
    body: {
        seu json aqui
    }

- PUT:
    * http://127.0.0.1:8000/crm/v3/objects/contacts/api_key_aqui/julian@gmail.com
    body: {
        seu json aqui
    }

O front-end também já está pronto, mas ele não está integrado com a API ainda.
