import requests
import json
import urllib.parse
from os import getenv
from pprint import pprint


API_KEY = getenv('HUBSPOT_API_KEY')
print(API_KEY)

max_results = 500 
hapikey = API_KEY
count = 5 
contact_list = []
property_list = []
get_all_contacts_url = "https://api.hubapi.com/contacts/v1/lists/all/contacts/all?"
parameter_dict = {'hapikey': hapikey, 'count': count}
headers = {}

# Paginate your request using offset
has_more = True
while has_more:
	parameters = urllib.parse.urlencode(parameter_dict)
	get_url = get_all_contacts_url + parameters
	r = requests.get(url= get_url, headers = headers)
	response_dict = json.loads(r.text)
	has_more = response_dict['has-more']
	contact_list.extend(response_dict['contacts'])
	parameter_dict['vidOffset']= response_dict['vid-offset']
	if len(contact_list) >= max_results: # Exit pagination, based on whatever value you've set your max results variable to. 
		print('maximum number of results exceeded')
		break
print('loop finished')

list_length = len(contact_list) 

print("You've succesfully parsed through {} contact records and added them to a list".format(list_length))

for contato in contact_list:
    pprint(contato)
