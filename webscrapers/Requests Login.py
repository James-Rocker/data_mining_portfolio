
import json
import requests

payload = {'inUserName': '', 'inUserPass': ''}
url = ''
requests.post(url, data=payload)

url = ''
r = requests.get(url)

# status code 200 is what we want, this means that the HTTP Status code is working as intended

header = {'': ''}
t = requests.get(url, headers=True)
newDictionary=json.loads(t)
