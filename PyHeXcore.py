# PyHeX is a Python3 command-line script made by YoshiOG.  It is used for 
# cloning Pokemon in Gen 7 games on-the-fly using NTR CFW.

# Credits:
#  - imthe666st : Wrote PyNTR, which this script depends on
#    - https://github.com/imthe666st/PyNTR
#  - Cell9 : Created NTR CFW
#  - YoshiOG : Created this script

# You may redistribute this script, just don't claim this as your work!
import socket
from PyNTR import PyNTR
import time
import os
import random
import array
import binascii
import sys
import struct

if len(sys.argv) >= 3:
    myIP = sys.argv[1]
    game = sys.argv[2]

client = PyNTR.PyNTR(myIP)
client.start_connection()
# client.send_hello_packet()
if game.lower() == 'usum' or game.lower() == 'u':
    client.set_game_name('momiji')
    boxOffset = 0x33015AB0
    wtNameOff = 0x32992184
    msgOff = 0x33060C60
if game.lower() == 'sm' or game.lower() == 'sumo':
    client.set_game_name('niji_loc')
    boxOffset = 0x330D9838
    wtNameOff = 0x32A6A184
viewOffset = 0x30000298

# !! LIST OF ALL POKEMON NAMES !! #
speciesList = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard", "Squirtle", "Wartortle", "Blastoise", "Caterpie", "Metapod", "Butterfree", "Weedle", "Kakuna", "Beedrill", "Pidgey", "Pidgeotto", "Pidgeot", "Rattata", "Raticate", "Spearow", "Fearow", "Ekans", "Arbok", "Pikachu", "Raichu", "Sandshrew", "Sandslash", "Nidoran♀", "Nidorina", "Nidoqueen", "Nidoran♂", "Nidorino", "Nidoking", "Clefairy", "Clefable", "Vulpix", "Ninetales", "Jigglypuff", "Wigglytuff", "Zubat", "Golbat", "Oddish", "Gloom", "Vileplume", "Paras", "Parasect", "Venonat", "Venomoth", "Diglett", "Dugtrio", "Meowth", "Persian", "Psyduck", "Golduck", "Mankey", "Primeape", "Growlithe", "Arcanine", "Poliwag", "Poliwhirl", "Poliwrath", "Abra", "Kadabra", "Alakazam", "Machop", "Machoke", "Machamp", "Bellsprout", "Weepinbell", "Victreebel", "Tentacool", "Tentacruel", "Geodude", "Graveler", "Golem", "Ponyta", "Rapidash", "Slowpoke", "Slowbro", "Magnemite", "Magneton", "Farfetch’d", "Doduo", "Dodrio", "Seel", "Dewgong", "Grimer", "Muk", "Shellder", "Cloyster", "Gastly", "Haunter", "Gengar", "Onix", "Drowzee", "Hypno", "Krabby", "Kingler", "Voltorb", "Electrode", "Exeggcute", "Exeggutor", "Cubone", "Marowak", "Hitmonlee", "Hitmonchan", "Lickitung", "Koffing", "Weezing", "Rhyhorn", "Rhydon", "Chansey", "Tangela", "Kangaskhan", "Horsea", "Seadra", "Goldeen", "Seaking", "Staryu", "Starmie", "Mr. Mime", "Scyther", "Jynx", "Electabuzz", "Magmar", "Pinsir", "Tauros", "Magikarp", "Gyarados", "Lapras", "Ditto", "Eevee", "Vaporeon", "Jolteon", "Flareon", "Porygon", "Omanyte", "Omastar", "Kabuto", "Kabutops", "Aerodactyl", "Snorlax", "Articuno", "Zapdos", "Moltres", "Dratini", "Dragonair", "Dragonite", "Mewtwo", "Mew", "Chikorita", "Bayleef", "Meganium", "Cyndaquil", "Quilava", "Typhlosion", "Totodile", "Croconaw", "Feraligatr", "Sentret", "Furret", "Hoothoot", "Noctowl", "Ledyba", "Ledian", "Spinarak", "Ariados", "Crobat", "Chinchou", "Lanturn", "Pichu", "Cleffa", "Igglybuff", "Togepi", "Togetic", "Natu", "Xatu", "Mareep", "Flaaffy", "Ampharos", "Bellossom", "Marill", "Azumarill", "Sudowoodo", "Politoed", "Hoppip", "Skiploom", "Jumpluff", "Aipom", "Sunkern", "Sunflora", "Yanma", "Wooper", "Quagsire", "Espeon", "Umbreon", "Murkrow", "Slowking", "Misdreavus", "Unown", "Wobbuffet", "Girafarig", "Pineco", "Forretress", "Dunsparce", "Gligar", "Steelix", "Snubbull", "Granbull", "Qwilfish", "Scizor", "Shuckle", "Heracross", "Sneasel", "Teddiursa", "Ursaring", "Slugma", "Magcargo", "Swinub", "Piloswine", "Corsola", "Remoraid", "Octillery", "Delibird", "Mantine", "Skarmory", "Houndour", "Houndoom", "Kingdra", "Phanpy", "Donphan", "Porygon2", "Stantler", "Smeargle", "Tyrogue", "Hitmontop", "Smoochum", "Elekid", "Magby", "Miltank", "Blissey", "Raikou", "Entei", "Suicune", "Larvitar", "Pupitar", "Tyranitar", "Lugia", "Ho-Oh", "Celebi", "Treecko", "Grovyle", "Sceptile", "Torchic", "Combusken", "Blaziken", "Mudkip", "Marshtomp", "Swampert", "Poochyena", "Mightyena", "Zigzagoon", "Linoone", "Wurmple", "Silcoon", "Beautifly", "Cascoon", "Dustox", "Lotad", "Lombre", "Ludicolo", "Seedot", "Nuzleaf", "Shiftry", "Taillow", "Swellow", "Wingull", "Pelipper", "Ralts", "Kirlia", "Gardevoir", "Surskit", "Masquerain", "Shroomish", "Breloom", "Slakoth", "Vigoroth", "Slaking", "Nincada", "Ninjask", "Shedinja", "Whismur", "Loudred", "Exploud", "Makuhita", "Hariyama", "Azurill", "Nosepass", "Skitty", "Delcatty", "Sableye", "Mawile", "Aron", "Lairon", "Aggron", "Meditite", "Medicham", "Electrike", "Manectric", "Plusle", "Minun", "Volbeat", "Illumise", "Roselia", "Gulpin", "Swalot", "Carvanha", "Sharpedo", "Wailmer", "Wailord", "Numel", "Camerupt", "Torkoal", "Spoink", "Grumpig", "Spinda", "Trapinch", "Vibrava", "Flygon", "Cacnea", "Cacturne", "Swablu", "Altaria", "Zangoose", "Seviper", "Lunatone", "Solrock", "Barboach", "Whiscash", "Corphish", "Crawdaunt", "Baltoy", "Claydol", "Lileep", "Cradily", "Anorith", "Armaldo", "Feebas", "Milotic", "Castform", "Kecleon", "Shuppet", "Banette", "Duskull", "Dusclops", "Tropius", "Chimecho", "Absol", "Wynaut", "Snorunt", "Glalie", "Spheal", "Sealeo", "Walrein", "Clamperl", "Huntail", "Gorebyss", "Relicanth", "Luvdisc", "Bagon", "Shelgon", "Salamence", "Beldum", "Metang", "Metagross", "Regirock", "Regice", "Registeel", "Latias", "Latios", "Kyogre", "Groudon", "Rayquaza", "Jirachi", "Deoxys", "Turtwig", "Grotle", "Torterra", "Chimchar", "Monferno", "Infernape", "Piplup", "Prinplup", "Empoleon", "Starly", "Staravia", "Staraptor", "Bidoof", "Bibarel", "Kricketot", "Kricketune", "Shinx", "Luxio", "Luxray", "Budew", "Roserade", "Cranidos", "Rampardos", "Shieldon", "Bastiodon", "Burmy", "Wormadam", "Mothim", "Combee", "Vespiquen", "Pachirisu", "Buizel", "Floatzel", "Cherubi", "Cherrim", "Shellos", "Gastrodon", "Ambipom", "Drifloon", "Drifblim", "Buneary", "Lopunny", "Mismagius", "Honchkrow", "Glameow", "Purugly", "Chingling", "Stunky", "Skuntank", "Bronzor", "Bronzong", "Bonsly", "Mime Jr.", "Happiny", "Chatot", "Spiritomb", "Gible", "Gabite", "Garchomp", "Munchlax", "Riolu", "Lucario", "Hippopotas", "Hippowdon", "Skorupi", "Drapion", "Croagunk", "Toxicroak", "Carnivine", "Finneon", "Lumineon", "Mantyke", "Snover", "Abomasnow", "Weavile", "Magnezone", "Lickilicky", "Rhyperior", "Tangrowth", "Electivire", "Magmortar", "Togekiss", "Yanmega", "Leafeon", "Glaceon", "Gliscor", "Mamoswine", "Porygon-Z", "Gallade", "Probopass", "Dusknoir", "Froslass", "Rotom", "Uxie", "Mesprit", "Azelf", "Dialga", "Palkia", "Heatran", "Regigigas", "Giratina", "Cresselia", "Phione", "Manaphy", "Darkrai", "Shaymin", "Arceus", "Victini", "Snivy", "Servine", "Serperior", "Tepig", "Pignite", "Emboar", "Oshawott", "Dewott", "Samurott", "Patrat", "Watchog", "Lillipup", "Herdier", "Stoutland", "Purrloin", "Liepard", "Pansage", "Simisage", "Pansear", "Simisear", "Panpour", "Simipour", "Munna", "Musharna", "Pidove", "Tranquill", "Unfezant", "Blitzle", "Zebstrika", "Roggenrola", "Boldore", "Gigalith", "Woobat", "Swoobat", "Drilbur", "Excadrill", "Audino", "Timburr", "Gurdurr", "Conkeldurr", "Tympole", "Palpitoad", "Seismitoad", "Throh", "Sawk", "Sewaddle", "Swadloon", "Leavanny", "Venipede", "Whirlipede", "Scolipede", "Cottonee", "Whimsicott", "Petilil", "Lilligant", "Basculin", "Sandile", "Krokorok", "Krookodile", "Darumaka", "Darmanitan", "Maractus", "Dwebble", "Crustle", "Scraggy", "Scrafty", "Sigilyph", "Yamask", "Cofagrigus", "Tirtouga", "Carracosta", "Archen", "Archeops", "Trubbish", "Garbodor", "Zorua", "Zoroark", "Minccino", "Cinccino", "Gothita", "Gothorita", "Gothitelle", "Solosis", "Duosion", "Reuniclus", "Ducklett", "Swanna", "Vanillite", "Vanillish", "Vanilluxe", "Deerling", "Sawsbuck", "Emolga", "Karrablast", "Escavalier", "Foongus", "Amoonguss", "Frillish", "Jellicent", "Alomomola", "Joltik", "Galvantula", "Ferroseed", "Ferrothorn", "Klink", "Klang", "Klinklang", "Tynamo", "Eelektrik", "Eelektross", "Elgyem", "Beheeyem", "Litwick", "Lampent", "Chandelure", "Axew", "Fraxure", "Haxorus", "Cubchoo", "Beartic", "Cryogonal", "Shelmet", "Accelgor", "Stunfisk", "Mienfoo", "Mienshao", "Druddigon", "Golett", "Golurk", "Pawniard", "Bisharp", "Bouffalant", "Rufflet", "Braviary", "Vullaby", "Mandibuzz", "Heatmor", "Durant", "Deino", "Zweilous", "Hydreigon", "Larvesta", "Volcarona", "Cobalion", "Terrakion", "Virizion", "Tornadus", "Thundurus", "Reshiram", "Zekrom", "Landorus", "Kyurem", "Keldeo", "Meloetta", "Genesect", "Chespin", "Quilladin", "Chesnaught", "Fennekin", "Braixen", "Delphox", "Froakie", "Frogadier", "Greninja", "Bunnelby", "Diggersby", "Fletchling", "Fletchinder", "Talonflame", "Scatterbug", "Spewpa", "Vivillon", "Litleo", "Pyroar", "Flabébé", "Floette", "Florges", "Skiddo", "Gogoat", "Pancham", "Pangoro", "Furfrou", "Espurr", "Meowstic", "Honedge", "Doublade", "Aegislash", "Spritzee", "Aromatisse", "Swirlix", "Slurpuff", "Inkay", "Malamar", "Binacle", "Barbaracle", "Skrelp", "Dragalge", "Clauncher", "Clawitzer", "Helioptile", "Heliolisk", "Tyrunt", "Tyrantrum", "Amaura", "Aurorus", "Sylveon", "Hawlucha", "Dedenne", "Carbink", "Goomy", "Sliggoo", "Goodra", "Klefki", "Phantump", "Trevenant", "Pumpkaboo", "Gourgeist", "Bergmite", "Avalugg", "Noibat", "Noivern", "Xerneas", "Yveltal", "Zygarde", "Diancie", "Hoopa", "Volcanion", "Rowlet", "Dartrix", "Decidueye", "Litten", "Torracat", "Incineroar", "Popplio", "Brionne", "Primarina", "Pikipek", "Trumbeak", "Toucannon", "Yungoos", "Gumshoos", "Grubbin", "Charjabug", "Vikavolt", "Crabrawler", "Crabominable", "Oricorio", "Cutiefly", "Ribombee", "Rockruff", "Lycanroc", "Wishiwashi", "Mareanie", "Toxapex", "Mudbray", "Mudsdale", "Dewpider", "Araquanid", "Fomantis", "Lurantis", "Morelull", "Shiinotic", "Salandit", "Salazzle", "Stufful", "Bewear", "Bounsweet", "Steenee", "Tsareena", "Comfey", "Oranguru", "Passimian", "Wimpod", "Golisopod", "Sandygast", "Palossand", "Pyukumuku", "Type: Null", "Silvally", "Minior", "Komala", "Turtonator", "Togedemaru", "Mimikyu", "Bruxish", "Drampa", "Dhelmise", "Jangmo-o", "Hakamo-o", "Kommo-o", "Tapu Koko", "Tapu Lele", "Tapu Bulu", "Tapu Fini", "Cosmog", "Cosmoem", "Solgaleo", "Lunala", "Nihilego", "Buzzwole", "Pheromosa", "Xurkitree", "Celesteela", "Kartana", "Guzzlord", "Necrozma", "Magearna", "Marshadow", "Poipole", "Naganadel", "Stakataka", "Blacephalon", "Zeraora"]

countryList = ["N/A", "Japan", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "Anguilla", "Antigua and Barbuda", "Argentina", "Aruba", "Bahamas", "Barbados", "Belize", "Bolivia", "Brazil", "British Virgin Islands", "Canada", "Cayman Islands", "Chile", "Colombia", "Costa Rica", "Dominica", "Dominican Republic", "Ecuador", "El Salvador", "French Guiana", "Grenada", "Guadeloupe", "Guatemala", "Guyana", "Haiti", "Honduras", "Jamaica", "Martinique", "Mexico", "Montserrat", "Netherlands Antilles", "Nicaragua", "Panama", "Paraguay", "Peru", "St. Kitts and Nevis", "St. Lucia", "St. Vincent and the Grenadines", "Suriname", "Trinidad and Tobago", "Turks and Caicos Islands", "United States", "Uruguay", "US Virgin Islands", "Venezuela", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "Albania", "Australia", "Austria", "Belgium", "Bosnia and Herzegovina", "Botswana", "Bulgaria", "Croatia", "Cyprus", "Czech Republic", "Denmark (Kingdom of)", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Latvia", "Lesotho", "Liechtenstein", "Lithuania", "Luxembourg", "Macedonia (Republic of)", "Malta", "Montenegro", "Mozambique", "Namibia", "Netherlands", "New Zealand", "Norway", "Poland", "Portugal", "Romania", "Russia", "Serbia and Kosovo", "Slovakia", "Slovenia", "South Africa", "Spain", "Swaziland", "Sweden", "Switzerland", "Turkey", "United Kingdom", "Zambia", "Zimbabwe", "Azerbaijan", "Mauritania", "Mali", "Niger", "Chad", "Sudan", "Eritrea", "Djibouti", "Somalia", "Andorra", "Gibraltar", "Guernsey", "Isle of Man", "Jersey", "Monaco", "Taiwan", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "South Korea", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "Hong Kong", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "Singapore", "N/A", "N/A", "Malaysia", "N/A", "N/A", "N/A", "China", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "U.A.E.", "India", "N/A", "N/A", "N/A", "N/A", "Saudi Arabia", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "San Marino", "Vatican City", "Bermuda"]

stateList = ['N/A','N/A','D.C.','Alaska','Alabama','Arkansas','Arizona','California','Colorado','Connecticut','Delaware','Florida','Georgia','Hawaii','Iowa','Idaho','Illinois','Indiana','Kansas','Kentucky','Louisiana','Massachusetts','Maryland','Maine','Michigan','Minnesota','Missouri','Mississippi','Montana','North Carolina','North Dakota','Nebraska','New Hampshire','New Jersey','New Mexico','Nevada','New York','Ohio','Oklahoma','Oregon','Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Virginia','Vermont','Washington','Wisconsin','West Virginia','Wyoming','Puerto Rico']

# ======================
#   BEGIN CRYPTO STUFF

def rshift(val, n): return val>>n if val >= 0 else (val+0x100000000)>>n
A = 0
B = 1
C = 2
D = 3

blocks = [[[A, B, C, D], [A, B, C, D]], [[A, B, D, C], [A, B, D, C]], [[A, C, B, D], [A, C, B, D]], [[A, C, D, B], [A, D, B, C]], [[A, D, B, C], [A, C, D, B]], [[A, D, C, B], [A, D, C, B]], [[B, A, C, D], [B, A, C, D]], [[B, A, D, C], [B, A, D, C]], [[B, C, A, D], [C, A, B, D]], [[B, C, D, A], [D, A, B, C]], [[B, D, A, C], [C, A, D, B]], [[B, D, C, A], [D, A, C, B]], [[C, A, B, D], [B, C, A, D]], [[C, A, D, B], [B, D, A, C]], [[C, B, A, D], [C, B, A, D]], [[C, B, D, A], [D, B, A, C]], [[C, D, A, B], [C, D, A, B]], [[C, D, B, A], [D, C, A, B]], [[D, A, B, C], [B, C, D, A]], [[D, A, C, B], [B, D, C, A]], [[D, B, A, C], [C, B, D, A]], [[D, B, C, A], [D, B, C, A]], [[D, C, A, B], [C, D, B, A]], [[D, C, B, A], [D, C, B, A]]]

def nextRandom(obj):
    obj[0] = (obj[0] * 0x41C64E6D + 0x00006073) & 0xFFFFFFFF
    return rshift(obj[0], 16)

def cipherPkx(pk):
    tmpStr = str(binascii.hexlify(pk)).replace( '\\x', '' ).replace( ',', '' )[2:466]
    
    tmpArray = [tmpStr[i:i+2] for i in range(0, len(tmpStr), 2)]
    for y in range(0,232):
        tmpArray[y] = int(tmpArray[y], 16)
    aux = 0
    seed = [(tmpArray[0] + (tmpArray[1] << 8) + (tmpArray[2] << 16) + (tmpArray[3] * 0x1000000))]
    for eye in range(4,116):
        i = eye * 2
        aux = (tmpArray[i] + ( tmpArray[i+1] << 8 )) ^ nextRandom(seed)
        pk[i] = aux & 0xFF
        pk[i+1] = rshift(aux, 8)
    return pk

def shuffleBlocks(pkm, mode):
    tmpStr = str(binascii.hexlify(pkm)).replace( '\\x', '' ).replace( ',', '' )[2:467]
    tmpArray = [tmpStr[i:i+2] for i in range(0, len(tmpStr), 2)]
    for y in range(0,232):
        tmpArray[y] = int(tmpArray[y], 16)
    aux = tmpArray
    order = rshift(((tmpArray[0] + (tmpArray[1] << 8) + (tmpArray[2] << 16) ) & 0x3E000), 0x0D) % 24
    for i in range(0,4):
        for j in range(0,56):
            pkm[j + 56 * i + 8] = aux[j + 56 * blocks[order][mode][i] + 8]
    return pkm

def encryptPkx(pkm):
    pkx = pkm
    shuffleBlocks(pkx, 0)
    cipherPkx(pkx)
    return pkx
def decryptPkx(pkm):
    pkx = pkm
    cipherPkx(pkx)
    shuffleBlocks(pkx, 1)
    return pkx

#    END CRYPTO STUFF
# ======================
def cmdhelp():
    print("PyHeX by YoshiOG.  Please use responsibly; I am not responsible for any data loss, bans, etc.")
    print("Currently implemented commands: (probably outdated list)")
    print(" clone(sourceBox, sourceSlot, copies[, destBox, destSlot])\n   Clones the Pokemon from source box/slot N times to destination box/slot.  Default destination is set to source.")
    print(" boxexport(box[, filepath])\n  Dumps all Pokemon data from given box to an EK7 binary.  Default filepath is 'boxdump.ek7' in the folder PyHeX is in.")
    print(" boximport(box[, filepath])\n  Overwrites all Pokemon data in given box with data from an EK7 box binary.  Imports from 'boxdump.ek7' by default.")
    print(" inject(pkmPath[, box, slot[, copies]])\n  Overwrites Pokemon starting at given box/slot with N copies of a given PK7 (decrypted).  Imports to Box 1 Slot 1 once by default.")
    print(" stats([box, slot])\n  Prints various stats of the Pokemon at given box/slot, or the currently selected Pokemon in the PC by default.")
    print(" batchdump(box, slot, length[, dumpPath])\n  Dumps 2 or more Pokemon to a raw EK7 binary that can be used to fill a box using boximport.  Default dumpPath is 'batchdump.ek7'")
    print(" dirimport(box, dirPath[, randomize (True/False)])\n  Fills given box number with 30 of the PK7 files from the given folder path.\n  To randomize the order of the PK7s, type True as the third argument.")
    print(" ")

def clone(sourceBox = 255, sourceSlot = 255, copies = 0, destBox = 0, destSlot = 0):
    if sourceBox == 255 or sourceSlot == 255 or copies == 0:
        print('Please specify a box/slot and number of copies (at least 1)')
        return
    if sourceBox > 32 and sourceBox != 255:
        print('Box number must be between 1-32!')
        return
    if sourceSlot > 30 or sourceSlot == 0:
        print('Slot number must be between 1-30!')
        return
    if destBox > 32:
        print('Box number must be between 1-32!')
        return
    if destSlot > 30:
        print('Slot number must be between 1-30!')
        return
    sourceOff = boxOffset + (0xE8 * (sourceSlot - 1)) + (0x1B30 * (sourceBox - 1))
    destOff = sourceOff
    if destSlot != 0:
        destOff = boxOffset + (0xE8 * (destSlot - 1)) + (0x1B30 * (destBox - 1))
    if destSlot == 0:
        destBox = sourceBox
        destSlot = sourceSlot
    
    print('Reading PKM at Box ' + str(sourceBox) + ', Slot ' + str(sourceSlot))
    sourcePkm = client.ReadCustom(sourceOff, 0xE8)
    print('Writing ' + str(copies) + ' copies starting at Box ' + str(destBox) + ', Slot ' + str(destSlot))
    for x in range(0, copies):
        client.WriteCustom(0xE8 * x + destOff, sourcePkm, 0xE8)
    
    print('Cloning complete!')

def boxexport(box = 0, dumpPath = './boxdump.ek7'):
    if box > 32 or box < 1:
        print('Box number must be between 1-32!')
        return
    dumpOffset = 0x1B30 * (box - 1) + boxOffset
    print('Reading raw data from Box ' + str(box))
    dumpPkm = client.ReadCustom(dumpOffset, 0x1B30)
    f = open(dumpPath, 'w+b')
    f.write(dumpPkm.to_bytes(0x1B30, 'little'))
    f.close()
    print('Box ' + str(box) + ' dumped to ' + dumpPath)

def boximport(box = 0, thePath = './boxdump.ek7'):
    if box > 32 or box < 1:
        print('Box number must be between 1-32!')
        return
    importOff = 0x1B30 * (box - 1) + boxOffset
    print('Writing raw box data to Box ' + str(box))
    if not os.path.exists(thePath):
        print("The file could not be found.  Try boxexport() to create a dump!")
    f = open(thePath, 'r+b')
    content = f.read()
    if len(content) < 0x1B30:
        newContent = bytearray(content)
        while len(newContent) <= 0x1B30:
            newContent += bytearray(content)
    else:
        newContent = content
    client.WriteCustom(importOff, newContent, 0x1B30)
    f.close()
    print('Data from ' + str(thePath) + ' written to fill Box ' + str(box))

def dirimport(box = 0, dirPath = './dirimport', randomize = False):
    if box > 32 or box < 1:
        print('Box number must be between 1-32!')
        return
    importOff = 0x1B30 * (box - 1) + boxOffset
    print('Writing raw box data to Box ' + str(box))
    i = 0
    dirArray = [""]
    while i < 30:
        dirArray = os.listdir(dirPath)
        if randomize == True:
            random.shuffle(dirArray)
        for thePath in dirArray:
            if thePath.split(".")[-1].lower() == "pk7":
                if i >= 30:
                    print('Data from folder ' + str(dirPath) + ' written to fill Box ' + str(box))
                    return
                f = open(dirPath + "/" + thePath, 'rb+')
                content = f.read()
                newContent = encryptPkx(bytearray(content)[0:232])
                client.WriteCustom(importOff + i * 232, newContent, 232)
                f.close()
                #print(dirPath + "/" + thePath)
                i += 1
    print('Data from folder ' + str(dirPath) + ' written to fill Box ' + str(box))
    return

def inject(pkmPath, box=1, slot=1, copies=1):
    if box > 32 or box < 1:
        print('Box number must be between 1-32!')
        return
    if slot > 30 or slot < 1:
        print('Slot number must be between 1-30!')
        return
    f = open(pkmPath, 'rb+')
    pkm = bytearray(f.read())
    f.close()
    if pkmPath[len(pkmPath) - 4 :] == '.pk7':
        pkm = encryptPkx(pkm)
    injectOff = boxOffset + (0xE8 * (slot - 1)) + (0x1B30 * (box - 1))
    for ewe in range(0,copies):
        client.WriteCustom(232 * ewe + injectOff, bytes(pkm), 0xE8)
    print('Injection complete!')

def dump(dumpPath = "./pkmDump.pk7", box = 0, slot = 1, doPrint=True):
    if box > 32 or box < 0:
        print('Box number must be between 1-32!')
        return
    if slot > 30 or slot < 1:
        print('Slot number must be between 1-30!')
        return
    dumpOff = boxOffset + (0xE8 * (slot - 1)) + (0x1B30 * (box - 1))
    if box == 0:
        dumpOff = viewOffset
    dumpRaw = client.ReadCustom(dumpOff, 232).to_bytes(232, "little")
    dumpPkmBA = bytearray.fromhex(bytes(dumpRaw).hex())
    dumpPkm = decryptPkx(dumpPkmBA)
    dumpStats = stats(box, slot, False)
    f = open(dumpPath, 'w+')
    f.close()
    f = open(dumpPath, 'wb')
    f.write(dumpPkm)
    f.close()
    if doPrint == True:
        print(dumpStats[0][0] + " dumped to " + dumpPath)

def stats(box=0, slot=1, doPrint=True):
    if box > 32 or box < 0:
        print('Box number must be between 1-32!')
        return
    if slot > 30 or slot < 1:
        print('Slot number must be between 1-30!')
        return
    dumpOff = boxOffset + (0xE8 * (slot - 1)) + (0x1B30 * (box - 1))
    if box == 0:
        dumpOff = viewOffset
    dumpRaw = client.ReadCustom(dumpOff, 232).to_bytes(232, "little")
    dumpPkmBA = bytearray.fromhex(bytes(dumpRaw).hex())
    dumpPkm = decryptPkx(dumpPkmBA)
    # Nickname, Species
    nickBytes = dumpPkm[0x40:0x58].split(b'\x00\x00')[0]
    if len(nickBytes) % 2 != 0:
        nickBytes += b'\x00'
    nickBytes = dumpPkm[0x40:0x58].split(b'\x00\x00')[0]
    if len(nickBytes) % 2 != 0:
        nickBytes += b'\x00'
    nick = nickBytes.decode("utf-16")
    species = int.from_bytes(dumpPkm[8:10], "little")
    if(species < 1 or species > 807):
        speciesName = "Missingno."
    else:
        speciesName = speciesList[species - 1]
    # PID, TID/SID, shiny values, OT name
    encKey = int.from_bytes(dumpPkm[0:4], "little")
    otBytes = dumpPkm[0xB0:0xC8].split(b'\x00\x00')[0]
    if len(otBytes) % 2 != 0:
        otBytes += b'\x00'
    ot = otBytes.decode("utf-16")
    pid = int.from_bytes(dumpPkm[0x18:0x1C], "little")
    tid = int.from_bytes(dumpPkm[0xC:0xE], "little")
    sid = int.from_bytes(dumpPkm[0xE:0x10], "little")
    psv = ((pid >> 16 ^ pid & 0xFFFF) >> 4)
    tsv = (tid ^ sid) >> 4
    isShiny = (psv == tsv)
    # Individual Values
    iv32 = int.from_bytes(dumpPkm[0x74:0x78], "little")
    ivHP = "%02d" % ((iv32 >> 0) & 0x1F)
    ivAtk = "%2d" % ((iv32 >> 5) & 0x1F)
    ivDef = "%2d" % ((iv32 >> 10) & 0x1F)
    ivSpA = "%2d" % ((iv32 >> 20) & 0x1F)
    ivSpD = "%2d" % ((iv32 >> 25) & 0x1F)
    ivSpe = "%2d" % ((iv32 >> 15) & 0x1F)
    # Effort Values
    i = 0
    ev = [0,0,0,0,0,0]
    evTotal = 0
    evOrder = [0,1,2,5,3,4]
    for i in range(0,6):
        #ev[i] = "%03d" % int(dumpPkm[0x1E + i])
        ev[evOrder[i]] = str(int(dumpPkm[0x1E + i]))
        #evTotal += int(ev[i])
    evTotal = int(ev[0])+int(ev[1])+int(ev[2])+int(ev[3])+int(ev[4])+int(ev[5])
    # Print data
    if doPrint:
        print("\nStats for this #%03d" % species + " " + speciesName)
        print('Nickname: ' + nick)
        print("PID: 0x%08x" % pid + "      (ESV=%04d)" % psv)
        print("OT: " + ot)
        print("TID/SID: %05d" % tid + "/%05d" % sid + " (TSV=%04d)" % tsv)
        if isShiny:
            print("Shiny: YES")
        else:
            print("Shiny: no")
        print("\n>> IV/EV Spreads (HP/Atk/Def/SpA/SpD/Spe)")
        ivString = "IVs: " + " / ".join([ivHP,ivAtk,ivDef,ivSpA,ivSpD,ivSpe])
        print(f"{ivString:<{38}}" + "  Total: " + str(int(ivHP)+int(ivAtk)+int(ivDef)+int(ivSpA)+int(ivSpD)+int(ivSpe)))
        evString = "EVs: " + " / ".join(ev)
        print(f"{evString:<{38}}" + "  Total: " + str(evTotal))
    return [[speciesName,nick,ot], isShiny, pid, species, encKey, evTotal]

def batchdump(box, slot, length, dumpPath = "./batchdump.ek7"):
    if box > 32 or box < 1:
        print('Box number must be between 1-32!')
        return
    if slot > 29 or slot < 1:
        print('Starting slot number must be between 1-29!')
        return
    if length + slot > 30 or length < 2:
        print('Length of dump must be between 2 and end of box!')
        return
    dumpOff = boxOffset + (0xE8 * (slot - 1)) + (0x1B30 * (box - 1))
    dumpEkx = client.ReadCustom(dumpOff, 232 * length)
    f = open(dumpPath, 'wb+')
    f.write(dumpEkx.to_bytes(232 * length, 'little'))
    f.close()
    print("Data dumped from Box " + str(box) + " Slots " + str(slot) + " thru " + str(slot + length - 1))
def setmsg(offset, id = -1):
    if id <= -1:
        id = random.randint(0,1048)
    if id >= 0 and id < 1049:
        client.WriteU16(msgOff + offset * 2, id)
        print("Set Festival Plaza message #" + str(offset) + " to ID " + str(id))

############################################################
# !! BELOW ARE TEST COMMANDS USED IN MAKING THIS SCRIPT !! #
#          Only use if you know what you're doing!         #
############################################################
def encryptTest(inputPath = './test.pk7', outputPath = './test.ek7'):
    f = open(inputPath, 'rb+')
    pkm = bytearray(f.read())
    f.close()
    f = open(outputPath, 'rb+')
    f.write(bytes(encryptPkx(pkm)))
    f.close()
    print('Done.  Make sure to open the newly generated EK7 with PKHeX to make sure it\'s valid!')
def decryptTest(sourceBox = 255, sourceSlot = 255, outputPath = './test.pk7'):
    if sourceBox == 255 or sourceSlot == 255:
        print('Please specify a box/slot and number of copies (at least 1)')
        return
    if sourceBox > 32 and sourceBox != 255:
        print('Box number must be between 1-32!')
        return
    if sourceSlot > 30 or sourceSlot == 0:
        print('Slot number must be between 1-30!')
        return
    sourceOff = boxOffset + (0xE8 * (sourceSlot - 1)) + (0x1B30 * (sourceBox - 1))
    pkm = bytearray.fromhex(bytes(client.ReadCustom(sourceOff, 0xE8).to_bytes(232, "little")).hex())
    #print(bytearray(pkm))
    f = open(outputPath, 'rb+')
    f.write(bytes(decryptPkx(pkm)))
    f.close()
    print('Done.  Make sure to open the newly generated PK7 with PKHeX or a hex editor to make sure it\'s valid!')

def getwtname(doPrint=True):
    wtNameB = client.ReadCustom(wtNameOff, 24).to_bytes(24, "little").split(b'\x00\x00')[0]
    if len(wtNameB) % 2 != 0:
        wtNameB += b'\x00'
    wtName = wtNameB.decode("utf-16")
    if doPrint == True: print(u"Recent Wonder Trade partner: %s" % wtName)
    return wtName
def getwtcountry():
    wtCountryB = client.ReadU8(wtNameOff + 0xCB)
    if countryList[wtCountryB] == "United States":
        wtSubregionB = client.ReadU8(wtNameOff + 0xCA)
        return countryList[wtCountryB] + " (" + stateList[wtSubregionB] + ")"
    else:
        return countryList[wtCountryB]
def viewerstring(doPrint=True):
    viewerStr = ""
    msg0 = client.ReadU16(wtNameOff + 0xCC)
    msg1 = client.ReadU16(wtNameOff + 0xCE)
    msg2 = client.ReadU16(wtNameOff + 0xD0)
    if msg0 == 0x409 and msg2 == 0x3C1:  # *twitch twitch*, Too optimistic!
        viewerStr = "[Viewer] "
        if doPrint: print("Trade partner is an AuSLove viewer")
    if msg0 == 0x409 and msg2 != 0x3C1:  # just *twitch twitch*
        viewerStr = "[maybe viewer?] "
        if doPrint: print("Trade partner might be an AuSLove viewer")
    return viewerStr