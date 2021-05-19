import requests

API_KEY = "05361bc22fa83fe94fc8552d76d81c44"
URL = "http://api.weatherstack.com/current"

pilseta = "London"

parametri = {'access_key': API_KEY, 'query': pilseta}

atbilde = requests.get(URL, parametri)
js = atbilde.json()
print(js)
print()