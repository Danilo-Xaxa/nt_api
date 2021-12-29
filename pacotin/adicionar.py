import json
import requests
from os import getenv


API_KEY = getenv('HUBSPOT_API_KEY')

endpoint = f"https://api.hubapi.com/contacts/v1/contact/?hapikey={API_KEY}"
headers = {}
headers["Content-Type"]="application/json"
data = json.dumps({
  "properties": [
    {
      "property": "email",
      "value": "aaabbb@gmail.com"
    },
    {
      "property": "firstname",
      "value": "aaaa"
    },
    {
      "property": "lastname",
      "value": "bbbb"
    },
    {
      "property": "telefone",
      "value": "423554321"
    },
    {
      "property": "aniversario",
      "value": "26/02"
    },
    {
      "property": "Peso",
      "value": 80
    },
  ]
})


r = requests.post( url = endpoint, data = data, headers = headers )

print(r.text)
