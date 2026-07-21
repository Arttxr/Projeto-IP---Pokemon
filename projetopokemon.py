import random

with open("pokemons.txt", "r", encoding="utf-8") as arquivo:
    pokemons = arquivo.read().split(',')
    
    numeros = list(range(1,152))

with open("raridade.txt", "r", encoding="utf-8") as arquivo:
    raridades = arquivo.read().split(',',' ')

#funçoes da pokedex!
def registrarPokemon(numeros, pokemons, raridades):
    numeroTirado = random.randint(1, 152)
    indice = numeroTirado - 1
    print (f'Parabéns, você capturou um(a) {pokemons[indice]}')
    print (f'Número do Pokemon na Pokedex: #{indice +1}')
    print (f'Raridade do pokemon: {raridades[indice]}')
    
    
registrarPokemon(numeros, pokemons, raridades)