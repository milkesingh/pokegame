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


# pokemon_id = "pikachu"
# pokemon_data = get_pokemon_data(pokemon_id)
# if pokemon_data:
#     print(json.dumps(pokemon_data, indent=4))


def main():
    pokemon_id = input("Ingrese el ID de un Pokémon: ")
    pokemon_data = get_pokemon_data(pokemon_id)
    if pokemon_data:
        # print(json.dumps(pokemon_data, indent=4))
        nombre_pokemon = pokemon_data['name']
        print(f"Nombre: {nombre_pokemon}")

        tipos_pokemon = [tipo['type']['name'] for tipo in pokemon_data['types']]
        print(f"Tipos: {', '.join(tipos_pokemon)}")

        estadisticas_pokemon = {stat['stat']['name']: stat['base_stat'] for stat in pokemon_data['stats']}
        print("Estadísticas:")
        for stat_name, stat_value in estadisticas_pokemon.items():
            print(f"{stat_name}: {stat_value}")



    else:
        print("No se pudo encontrar el Pokémon.")

if __name__ == "__main__":
    main()

