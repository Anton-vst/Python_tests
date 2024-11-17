import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '0e818a12923dbb9b1d34ff063d3ad19c'
HEADER = {'Content-Type' : 'application/json' , 'trainer_token' : TOKEN}
body_new_pokemon = {
    "name": "Pika",
    "photo_id": -1
}

response = requests.post(url = f'{URL}/pokemons' , headers = HEADER , json = body_new_pokemon)
print(response.text)

pokemon_id = response.json()['id']

body_new_name = {
    "pokemon_id": pokemon_id,
    "name": "Polly",
    "photo_id": 2
}

response_change_name = requests.put(url = f'{URL}/pokemons' , headers = HEADER , json = body_new_name)
print(response_change_name.text)

body_add_pokeball = {
    "pokemon_id": pokemon_id
}

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball' , headers = HEADER , json = body_add_pokeball)
print(response_add_pokeball.text)
