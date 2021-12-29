from hubspot3 import Hubspot3
from os import getenv
from pprint import pprint


API_KEY = getenv('HUBSPOT_API_KEY')

client = Hubspot3(api_key=API_KEY)

# all of the clients are accessible as attributes of the main Hubspot3 Client
contact = client.contacts.get_contact_by_email('thomyorke@gmail.com')
contact_id = contact['vid']

all_companies = client.companies.get_all()

pprint(contact)
