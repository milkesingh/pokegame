import requests
import json, random


class Pokemon:
    def __init__(self, name, hp, attacks):
        self.name = name
        self.hp = hp
        self.attacks = attacks

    def attack(self, other, attack_name):
        if attack_name not in self.attacks:
            print(f"{self.name} no tiene el ataque {attack_name}.")
            return
        damage = self.attacks[attack_name]
        other.hp -= damage
        print(f"{self.name} usó {attack_name}! {other.name} perdió {damage} puntos de vida.")


# Obtiene la lista de nombres de Pokémon
response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=151')  # Limitado a los primeros 151 para este ejemplo
pokemon_list_data = response.json()

# Extrae solo los nombres de los Pokémon de la lista
pokemon_names = [pokemon['name'] for pokemon in pokemon_list_data['results']]

chosen_pokemon_name = random.choice(pokemon_names)
print(f"El Pokémon elegido es: {chosen_pokemon_name}")


def get_pokemon_data(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error al obtener datos del Pokémon con ID {pokemon_id}: {response.status_code}")
        return None


def get_pokemon_attacks(pokemon_data):
    attacks = {}
    print("error aca")
    # i=0
    for move in pokemon_data['moves']:
        # i+=1
        move_data = requests.get(move['move']['url']).json()
        # Simplificamos asumiendo que el daño es fijo y está disponible directamente. En realidad, necesitarías más lógica aquí.
        damage = move_data.get('power')
        print(move)
        if damage is not None:
            attacks[move['move']['name']] = damage
    return attacks


def battle(pokemon1, pokemon2):
    turn = 0
    print("llega hasta aca 2")
    while pokemon1.hp > 0 and pokemon2.hp > 0:
        turn += 1
        print(f"\nTurno {turn}")
        
        # Alternar quién ataca primero
        if turn % 2 == 0:
            attacker, defender = pokemon2, pokemon1
        else:
            attacker, defender = pokemon1, pokemon2
        
        # Elegir un ataque al azar
        attack_name = random.choice(list(attacker.attacks.keys()))
        attacker.attack(defender, attack_name)
        
        # Verificar si el combate ha terminado
        if defender.hp <= 0:
            print(f"\n{attacker.name} derrotó a {defender.name}!\n")
            break


def main():
    pokemon_id = input("Ingrese el ID de un Pokémon: ")
    pokemon_data_1 = get_pokemon_data(pokemon_id)
    if pokemon_data_1:
        # print(json.dumps(pokemon_data, indent=4))
        nombre_pokemon = pokemon_data_1['name']
        print(f"Nombre: {nombre_pokemon}")

        tipos_pokemon = [tipo['type']['name'] for tipo in pokemon_data_1['types']]
        print(f"Tipos: {', '.join(tipos_pokemon)}")

        estadisticas_pokemon_1 = {stat['stat']['name']: stat['base_stat'] for stat in pokemon_data_1['stats']}
        print("Estadísticas:")
        for stat_name, stat_value in estadisticas_pokemon_1.items():
            print(f"{stat_name}: {stat_value}")
    else:
        print("Error al obtener datos del Pokemon 1")
    
    pokemon_id = input("Ingrese el ID de un Pokémon: ")
    pokemon_data_2 = get_pokemon_data(pokemon_id)
    if pokemon_data_2:
        # print(json.dumps(pokemon_data, indent=4))
        nombre_pokemon = pokemon_data_2['name']
        print(f"Nombre: {nombre_pokemon}")

        tipos_pokemon = [tipo['type']['name'] for tipo in pokemon_data_2['types']]
        print(f"Tipos: {', '.join(tipos_pokemon)}")

        estadisticas_pokemon_2 = {stat['stat']['name']: stat['base_stat'] for stat in pokemon_data_2['stats']}
        print("Estadísticas:")
        for stat_name, stat_value in estadisticas_pokemon_2.items():
            print(f"{stat_name}: {stat_value}")
    else:
        print("Error al obtener datos del Pokemon 2")
    
    pokemon1 = Pokemon(
        name=pokemon_data_1['name'],
        hp=estadisticas_pokemon_1['hp'],  # Asumiendo que 'hp' es una de las estadísticas obtenidas previamente
        attacks=get_pokemon_attacks(pokemon_data_1)
    )

    pokemon2 = Pokemon(
        name=pokemon_data_2['name'],
        hp=estadisticas_pokemon_2['hp'],
        attacks=get_pokemon_attacks(pokemon_data_2)
    )

    battle(pokemon1, pokemon2)



if __name__ == "__main__":
    main()

