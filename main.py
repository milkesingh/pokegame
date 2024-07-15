import requests
import json


def get_pokemon_data(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error al obtener datos del Pokémon con ID {pokemon_id}: {response.status_code}")
        return None


    pokemon_id = "pikachu"
pokemon_data = get_pokemon_data(pokemon_id)
if pokemon_data:
    print(json.dumps(pokemon_data, indent=4))


def main():
    pokemon_id = input("Ingrese el ID de un Pokémon: ")
    pokemon_data = get_pokemon_data(pokemon_id)
    if pokemon_data:
        print(json.dumps(pokemon_data, indent=4))
    else:
        print("No se pudo encontrar el Pokémon.")

if __name__ == "__main__":
    main()

