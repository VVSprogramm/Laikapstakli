import requests

API_KEY = "05361bc22fa83fe94fc8552d76d81c44"
URL = "http://api.weatherstack.com/current"

pilsetas = []

with open("pilsetas.txt") as f:
  for line in f:
    pilsetas.append(line.strip())
print(pilsetas)


for pilseta in pilsetas:
  parametri = {'access_key': API_KEY, 'query': pilseta}
  atbilde = requests.get(URL, parametri)
  js = atbilde.json()

  temp = js['current']['temperature']
  datums = js['location']['localtime']

  with open(f"{pilseta}.txt", "w") as f:
    f.write(f"{datums}, {temp}\n")


#1. versija
# pilseta = "London"
# parametri = {'access_key': API_KEY, 'query': pilseta}

# atbilde = requests.get(URL, parametri)
# js = atbilde.json()
# print(js)
# print()

# temp = js['current']['temperature']
# datums = js['location']['localtime']
# pilsetaa =js['location']['name']
# valsts = js['location']['country']

# print(f"Temperatūra {pilsetaa}, {valsts}. {datums} ir {temp} grādi pēc celsija.")