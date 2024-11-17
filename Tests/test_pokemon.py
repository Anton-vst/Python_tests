import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '0e818a12923dbb9b1d34ff063d3ad19c'
HEADER = {'Content-Type' : 'application/json' , 'trainer_token' : TOKEN}
TRAINER_ID = '7846'

def test_status_code():
  response = requests.get(url = f'{URL}/trainers' , params = {'trainer_id' : TRAINER_ID} , headers = HEADER)
  assert response.status_code == 200

def test_name_trainer():
  response_name = requests.get(url = f'{URL}/trainers' , params = {'trainer_id' : TRAINER_ID} , headers = HEADER)
  assert response_name.json()['data'][0]['trainer_name'] == 'Игривый Кабачок'