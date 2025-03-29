import requests

base_url="https://pokeapi.co/api/v2/"

def get_pokemon(name):
    url=f"{base_url}/pokemon/{name}"
    response=requests.get(url)
    
    if response.status_code==200:
        pokemon_data=response.json()
        return pokemon_data
    else:
        print(f"Failed to retrive data {response.status_code}")


pokemon_name="typhlosion"
pokemon_info=get_pokemon(pokemon_name)

if pokemon_info:
    print(f"Pokemon name: {pokemon_info["name"]}")
    print(f"Pokemon height: {pokemon_info["height"]}")
    print(f"Pokemon id: {pokemon_info["id"]}")