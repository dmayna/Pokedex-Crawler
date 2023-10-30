import json
import requests
from bs4 import BeautifulSoup 

def crawl_pokemon(url, pokemon):
    pokemon_map = {}
    for poke in pokemon:
        resp = requests.get(url + poke)

        #http_respone 200 means OK status 
        if resp.status_code==200: 
            print("Successfully opened the web page")
        else:
             print("Failed opened the web page")
             return

        soup = BeautifulSoup(resp.text,'html.parser')

        poke_stats = soup.find("div",{"class":"grid-col span-md-12 span-lg-8"})
        poke_vitals = soup.find("table",{"class":"vitals-table"})
        

        if poke == "Farfetchd":
            poke =  "Farfetch\'d"
        if poke == "Mr-Mime":
            poke =  "Mr. Mime"

        for i, poke_ in enumerate(poke_stats.findAll("td")):
                match i:
                        case 0:
                            pokemon_map[poke] = {}
                            pokemon_map[poke]["HP"] = poke_.text
                        case 4:
                            pokemon_map[poke]["Attack"] = poke_.text
                        case 8:
                            pokemon_map[poke]["Defense"] = poke_.text
                        case 12:
                            pokemon_map[poke]["Sp Atk"] = poke_.text
                        case 16:
                            pokemon_map[poke]["Sp. Def"] = poke_.text
                        case 20:
                            pokemon_map[poke]["Speed"] = poke_.text
        for i, poke_v in enumerate(poke_vitals.findAll("td")):
            match i:
                    case 1:
                      type = poke_v.text.strip("\n",).split(" ")[:-1]
                      pokemon_map[poke]["Type"] = type
                    case 3:
                       pokemon_map[poke]["Height"] = poke_v.text.split(" ")[0][:-2]
                    case 4:
                       pokemon_map[poke]["Weight"] = poke_v.text.split(" ")[0][:-5]
    with open("pokemon.json", "w") as outfile: 
        json.dump(pokemon_map, outfile, indent = 4)

pokemon = [
    "Bulbasaur",
    "Ivysaur",
    "Venusaur",
    "Charmander",
    "Charmeleon",
    "Charizard",
    "Squirtle",
    "Wartortle",
    "Blastoise",
    "Caterpie",
    "Metapod",
    "Butterfree",
    "Weedle",
    "Kakuna",
    "Beedrill",
    "Pidgey",
    "Pidgeotto",
    "Pidgeot",
    "Rattata",
    "Raticate",
    "Spearow",
    "Fearow",
    "Ekans",
    "Arbok",
    "Pikachu",
    "Raichu",
    "Sandshrew",
    "Sandslash",
    "Nidoran-f",
    "Nidorina",
    "Nidoqueen",
    "Nidoran-m",
    "Nidorino",
    "Nidoking",
    "Clefairy",
    "Clefable",
    "Vulpix",
    "Ninetales",
    "Jigglypuff",
    "Wigglytuff",
    "Zubat",
    "Golbat",
    "Oddish",
    "Gloom",
    "Vileplume",
    "Paras",
    "Parasect",
    "Venonat",
    "Venomoth",
    "Diglett",
    "Dugtrio",
    "Meowth",
    "Persian",
    "Psyduck",
    "Golduck",
    "Mankey",
    "Primeape",
    "Growlithe",
    "Arcanine",
    "Poliwag",
    "Poliwhirl",
    "Poliwrath",
    "Abra",
    "Kadabra",
    "Alakazam",
    "Machop",
    "Machoke",
    "Machamp",
    "Bellsprout",
    "Weepinbell",
    "Victreebel",
    "Tentacool",
    "Tentacruel",
    "Geodude",
    "Graveler",
    "Golem",
    "Ponyta",
    "Rapidash",
    "Slowpoke",
    "Slowbro",
    "Magnemite",
    "Magneton",
    "Farfetchd",
    "Doduo",
    "Dodrio",
    "Seel",
    "Dewgong",
    "Grimer",
    "Muk",
    "Shellder",
    "Cloyster",
    "Gastly",
    "Haunter",
    "Gengar",
    "Onix",
    "Drowzee",
    "Hypno",
    "Krabby",
    "Kingler",
    "Voltorb",
    "Electrode",
    "Exeggcute",
    "Exeggutor",
    "Cubone",
    "Marowak",
    "Hitmonlee",
    "Hitmonchan",
    "Lickitung",
    "Koffing",
    "Weezing",
    "Rhyhorn",
    "Rhydon",
    "Chansey",
    "Tangela",
    "Kangaskhan",
    "Horsea",
    "Seadra",
    "Goldeen",
    "Seaking",
    "Staryu",
    "Starmie",
    "Mr-Mime",
    "Scyther",
    "Jynx",
    "Electabuzz",
    "Magmar",
    "Pinsir",
    "Tauros",
    "Magikarp",
    "Gyarados",
    "Lapras",
    "Ditto",
    "Eevee",
    "Vaporeon",
    "Jolteon",
    "Flareon",
    "Porygon",
    "Omanyte",
    "Omastar",
    "Kabuto",
    "Kabutops",
    "Aerodactyl",
    "Snorlax",
    "Articuno",
    "Zapdos",
    "Moltres",
    "Dratini",
    "Dragonair",
    "Dragonite",
    "Mewtwo",
    "Mew"
]

crawl_pokemon("https://pokemondb.net/pokedex/", pokemon)