import requests
id = '3440'
Tname = 'Garri' 
token = '96dba1ba3a49b30e0d7d441396c029ea'

response = requests.post('https://pokemonbattle.me:9104/pokemons', 
        headers = {'Content-Type': 'application/json', 'trainer_token': token}, 
        json = {"name": "Лисович", "photo": "https://dolnikov.ru/pokemons/createthumb.php?filename=albums/014.png&size=200"})
print(response.text)

name_response = requests.put('https://pokemonbattle.me:9104/pokemons', 
        headers = {'Content-Type': 'application/json', 'trainer_token': token}, 
        json = {"pokemon_id": 6314, "name": "Колобок"})
print(name_response.text)

pokeball_response = requests.post('https://pokemonbattle.me:9104/trainers/add_pokeball', 
        headers = {'Content-Type': 'application/json', 'trainer_token': token}, 
        json = {"pokemon_id": 6314})
print(pokeball_response.text)