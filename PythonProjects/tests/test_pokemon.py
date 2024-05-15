import requests
import pytest

URL='https://api.pokemonbattle.me/v2'
TOKEN='969f6b61b1b806b244de48723b43cb55'
TRAINER_ID = '4094'
HEADER={'Content-Type':'application/json',
        'trainer_token': TOKEN}

def test_status_code_200():
    response = requests.get(url=f'{URL}/pokemons', params={'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_get_trainer_name():
    response_get_trainer_name = requests.get(url=f'{URL}/trainers', params={'trainer_id': TRAINER_ID})
    assert response_get_trainer_name.json()['data'][0]['trainer_name'] == 'ДимаВДК'


