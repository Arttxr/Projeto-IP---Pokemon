import random

with open("pokemons.txt", "r", encoding="utf-8") as arquivo:
    pokemons = [p.strip().replace('"', '') for p in arquivo.read().split(',')]
    
    numeros = list(range(1,152))

with open("tipos.txt", "r", encoding="utf-8") as arquivo:
    tipos = arquivo.read().split('\n')

with open("pokedex.txt", "r", encoding="utf-8") as arquivo:
    pokedex = arquivo.read().split(',')

#funçoes da pokedex!
def registrarPokemon(numeros, pokemons, tipos):
    numeroTirado = random.randint(1, 152)
    indice = numeroTirado - 1
    print (f'Parabéns, você capturou um(a) {pokemons[indice]}')
    print (f'Número do Pokemon na Pokedex: #{indice +1}')
    print (f'Tipo(s)do Pokemon: {tipos[indice]}')
    if pokemons[indice].lower() not in pokedex[indice].lower():
        pokedex[indice] = f'#{indice + 1}: {pokemons[indice]}'
        print("Pokémon registrado na Pokédex!")
    else:
        print("Você já havia capturado esse Pokémon!")
    with open("pokedex.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(",".join(pokedex))
    
registrarPokemon(numeros, pokemons, tipos) 
