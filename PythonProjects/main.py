import requests

#{"message":"Пользователь подтверждён","id":4094 - айди тренера}
#{"message":"Покемон создан","id":"27395 - id pokemona}

URL='https://api.pokemonbattle.me/v2'
TOKEN='969f6b61b1b806b244de48723b43cb55'
HEADER={'Content-Type':'application/json',
        'trainer_token': TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "dima1111111@mail.ru",
    "password": "Iloveqa11111"
}

body_confirm = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "Бульба",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

body_change_name = {
    "pokemon_id": "27395",
    "name": "Поменял в питоне",
    "photo": "https://dolnikov.ru/pokemons/albums/005.png"
}

body_add_pokeball = {
    "pokemon_id": "27395"
}
#responce = requests.post(url = f'{URL}/trainers/reg', headers=HEADER, json=body_registration)
#print(responce.text)

#responce_confirm = requests.post(url = f'{URL}/trainers/confirm_email', headers=HEADER, json=body_confirm)
#print(responce_confirm.text)

#responce_create = requests.post(url = f'{URL}/pokemons', headers=HEADER, json=body_create)
#print(responce_create.text)

'''responce_change_name = requests.put(url = f'{URL}/pokemons', headers=HEADER, json=body_change_name)
print(responce_change_name.text)'''

responce_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_add_pokeball)
print(responce_add_pokeball.text)