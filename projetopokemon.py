import random
import os

# Pega o caminho da pasta onde o script está salvo
PASTA_ATUAL = os.path.dirname(os.path.abspath(__file__))

# Define os caminhos completos para os arquivos .txt
caminho_pokemons = os.path.join(PASTA_ATUAL, "pokemons.txt")
caminho_pc = os.path.join(PASTA_ATUAL, "pc.txt")
caminho_tipos = os.path.join(PASTA_ATUAL, "tipos.txt")
caminho_pokedex = os.path.join(PASTA_ATUAL, "pokedex.txt")

with open(caminho_pokemons, "r", encoding="utf-8") as arquivo:
    pokemons = [p.strip().replace('"', '') for p in arquivo.read().split(',')]
    
numeros = list(range(1,152))

with open(caminho_pc, "r", encoding="utf-8") as arquivo:
    pc = arquivo.read().splitlines()

with open(caminho_tipos, "r", encoding="utf-8") as arquivo:
    tipos = arquivo.read().split('\n')

with open(caminho_pokedex, "r", encoding="utf-8") as arquivo:
    pokedex = arquivo.read().split(',')

def iniciarUsuario():
    print("=" * 40)
    print("        BEM-VINDO À POKÉDEX")
    print("=" * 40)

    nome = input("Digite o nome do treinador: ").strip()

    if nome == "":
        nome = "Treinador"

    print(f"\nOlá, {nome}!")
    print("Boa sorte na sua jornada Pokémon!")

    return nome

#funçoes da pokedex!
def registrarPokemon(pokemons, tipos): #gera um pokemon aleatorio da região de Kanto para ser capturado
    numeroTirado = random.randint(1, 152)
    indice = numeroTirado - 1
    print ('='*20)
    print (f'Parabéns, você capturou um(a) {pokemons[indice]}')
    print (f'Número do Pokemon na Pokedex: #{indice +1}')
    print (f'Tipo(s)do Pokemon: {tipos[indice]}')
    if pokemons[indice].lower() not in pokedex[indice].lower():
        pokedex[indice] = f'#{indice + 1}: {pokemons[indice]} tipo: {tipos[indice]}'
        print("Pokémon registrado na Pokédex!")
    else:
        print("Você já havia capturado esse Pokémon!")
    with open(caminho_pokedex, "w", encoding="utf-8") as arquivo:
        arquivo.write(",".join(pokedex))

    status = (f'pokemon: {pokemons[indice]} | tipo: {tipos[indice]} lvl:{random.randint(1, 100)}')
    pc.append(status)
    with open(caminho_pc, "a", encoding="utf-8") as arquivo:
        arquivo.write(status + "\n")

def pesquisarNaPokedex(pokedex):
    pokemonApesquisar = input('Qual nome ou número do Pokemon que você quer encontrar na pokedex? (Ex: #2 // Ivysaur)').strip().lower()
    for pokemon in pokedex:
        dados = pokemon.split()
        numero = dados[0].replace(":", "")
        nome = dados[1].lower()

        if pokemonApesquisar == numero or pokemonApesquisar == nome:
            print (pokemon)
            return
        
    print ("Pokémon não registrado ou nome digitado errado.")

    #funções para o pc 
    
def mostrarPC(pc):
    if not pc:
        print("\nO seu PC está vazio.\n")
        return
        
    print("Pokémons no PC:")
    for pokemon in pc:
        print(pokemon)

def removerPokemonDoPC(pc):
    if not pc:
        print("\nO seu PC está vazio, não há nenhum Pokémon para remover.\n")
        return

    print("\n--- POKÉMONS NO PC ---")
    for i, pokemon in enumerate(pc, 1):
        print(f"{i}. {pokemon}")
    print("----------------------")

    try:
        escolha = int(input("\nDigite o número do Pokémon que deseja tirar do PC (ou 0 para cancelar): "))
        
        if escolha == 0:
            print("Operação cancelada.")
            return

        if 1 <= escolha <= len(pc):
            # Remove o Pokemon da lista na memória
            pokemon_removido = pc.pop(escolha - 1)
            
            # Atualiza o arquivo pc.txt salvando apenas os Pokémon restantes
            with open(caminho_pc, "w", encoding="utf-8") as arquivo:
                for pokemon in pc:
                    arquivo.write(pokemon + "\n")

            print("\nPokémon solto do PC com sucesso!")
        else:
            print("\nNúmero inválido.")

    except ValueError:
        print("\nPor favor, digite apenas um número inteiro válido.")

# --- EXECUÇÃO DO PROGRAMA ---
treinador = iniciarUsuario()

while True:
    print("=== MENU PRINCIPAL ===")
    print("1. Capturar Pokémon")
    print("2. Pesquisar na Pokédex")
    print("3. Ver Pokémons no PC")
    print("4. Soltar Pokémon do PC")
    print("5. Sair do Jogo")
    
    opcao = input("\nEscolha uma opção (1-5): ").strip()

    if opcao == "1":
        registrarPokemon(pokemons, tipos)
    elif opcao == "2":
        pesquisarNaPokedex(pokedex)
    elif opcao == "3":
        mostrarPC(pc)
    elif opcao == "4":
        removerPokemonDoPC(pc)
    elif opcao == "5":
        print(f"\nAté logo, {treinador}! Boa sorte na sua jornada.")
        break
    else:
        print("\nOpção inválida! Tente novamente.\n")
