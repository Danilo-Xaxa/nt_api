import hubspot
from pprint import pprint
from hubspot.crm.contacts import ApiException


client = hubspot.Client.create(api_key="api_key_aqui")

try:
    api_response = client.crm.contacts.basic_api.get_page(limit=10, archived=False, properties=["email", "telefone", "aniversario", "peso"])
    pprint(api_response)
except ApiException as e:
    print("Exception when calling basic_api->get_page: %s\n" % e)