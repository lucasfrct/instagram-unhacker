import requests
import re

username_extract = 'lucas.ferreira.costa.oficial'

url = 'https://www.instagram.com/'+ username_extract
r = requests.get(url)
m = re.search(r'"p:":\{"count":([0-9]+)\}', str(r.content))
print(r.content)