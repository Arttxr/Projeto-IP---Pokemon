import random

with open("pokemons.txt", "r", encoding="utf-8") as arquivo:
    pokemons = [p.strip().replace('"', '') for p in arquivo.read().split(',')]
    
    numeros = list(range(1,152))

with open("tipos.txt", "r", encoding="utf-8") as arquivo:
    tipos = arquivo.read().split('\n')

with open("pokedex.txt", "r", encoding="utf-8") as arquivo:
    pokedex = arquivo.read().split(',')

#funçoes da pokedex!
def registrarPokemon(pokemons, tipos):
    numeroTirado = random.randint(1, 152)
    indice = numeroTirado - 1
    print (f'Parabéns, você capturou um(a) {pokemons[indice]}')
    print (f'Número do Pokemon na Pokedex: #{indice +1}')
    print (f'Tipo(s)do Pokemon: {tipos[indice]}')
    if pokemons[indice].lower() not in pokedex[indice].lower():
        pokedex[indice] = f'#{indice + 1}: {pokemons[indice]} tipo: {tipos[indice]}'
        print("Pokémon registrado na Pokédex!")
    else:
        print("Você já havia capturado esse Pokémon!")
    with open("pokedex.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(",".join(pokedex))

def pesquisarNaPokedex(pokedex):
    pokemonApesquisar = input('Qual nome ou número do Pokemon que você quer encontrar na pokedex? (Ex: #2 // Ivysaur)').strip().lower()
    for pokemon in pokedex:
        dados = pokemon.split()
        numero = dados[0].replace(":", "")
        nome = dados[1].lower()

        if pokemonApesquisar == numero or pokemonApesquisar == nome:
            print (pokemon)
            
        
    print ("Pokémon não registrado ou nome digitado errado.")

