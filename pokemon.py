class pokemon():
  
  def getPokemon(self,value,language):
    switch = {
      1: {
        "de": "Bisasam",
        "en": "Bulbasaur",
        "fr": "Bulbizarre"
      },
      2: {
        "de": "Bisaknosp",
        "en": "Ivysaur",
        "fr": "Herbizarre"
      },
      3: {
        "de": "Bisaflor",
        "en": "Venusaur",
        "fr": "Florizarre"
      },
      4: {
        "de": "Glumanda",
        "en": "Charmander",
        "fr": "Salamèche"
      },
      5: {
        "de": "Glutexo",
        "en": "Charmeleon",
        "fr": "Reptincel"
      },
      6: {
        "de": "Glurak",
        "en": "Charizard",
        "fr": "Dracaufeu"
      },
      7: {
        "de": "Schiggy",
        "en": "Squirtle",
        "fr": "Carapuce"
      },
      8: {
        "de": "Schillok",
        "en": "Wartortle",
        "fr": "Carabaffe"
      },
      9: {
        "de": "Turtok",
        "en": "Blastoise",
        "fr": "Tortank"
      },
      10: {
        "de": "Raupy",
        "en": "Caterpie",
        "fr": "Chenipan"
      },
      11: {
        "de": "Safcon",
        "en": "Metapod",
        "fr": "Chrysacier"
      },
      12: {
        "de": "Smettbo",
        "en": "Butterfree",
        "fr": "Papilusion"
      },
      13: {
        "de": "Hornliu",
        "en": "Weedle",
        "fr": "Aspicot"
      },
      14: {
        "de": "Kokuna",
        "en": "Kakuna",
        "fr": "Coconfort"
      },
      15: {
        "de": "Bibor",
        "en": "Beedrill",
        "fr": "Dardargnan"
      },
      16: {
        "de": "Taubsi",
        "en": "Pidgey",
        "fr": "Roucool"
      },
      17: {
        "de": "Tauboga",
        "en": "Pidgeotto",
        "fr": "Roucoups"
      },
      18: {
        "de": "Tauboss",
        "en": "Pidgeot",
        "fr": "Roucarnage"
      },
      19: {
        "de": "Rattfratz",
        "en": "Rattata",
        "fr": "Rattata"
      },
      20: {
        "de": "Rattikarl",
        "en": "Raticate",
        "fr": "Rattatac"
      },
      21: {
        "de": "Habitak",
        "en": "Spearow",
        "fr": "Piafabec"
      },
      22: {
        "de": "Ibitak",
        "en": "Fearow",
        "fr": "Rapasdepic"
      },
      23: {
        "de": "Rettan",
        "en": "Ekans",
        "fr": "Abo"
      },
      24: {
        "de": "Arbok",
        "en": "Arbok",
        "fr": "Arbok"
      },
      25: {
        "de": "Pikachu",
        "en": "Pikachu",
        "fr": "Pikachu"
      },
      26: {
        "de": "Raichu",
        "en": "Raichu",
        "fr": "Raichu"
      },
      27: {
        "de": "Sandan",
        "en": "Sandshrew",
        "fr": "Sabelette"
      },
      28: {
        "de": "Sandamer",
        "en": "Sandslash",
        "fr": "Sablaireau"
      },
      29: {
        "de": "Nidoran♀",
        "en": "Nidoran♀",
        "fr": "Nidoran♀"
      },
      30: {
        "de": "Nidorina",
        "en": "Nidorina",
        "fr": "Nidorina"
      },
      31: {
        "de": "Nidoqueen",
        "en": "Nidoqueen",
        "fr": "Nidoqueen"
      },
      32: {
        "de": "Nidoran♂",
        "en": "Nidoran♂",
        "fr": "Nidoran♂"
      },
      33: {
        "de": "Nidorino",
        "en": "Nidorino",
        "fr": "Nidorino"
      },
      34: {
        "de": "Nidoking",
        "en": "Nidoking",
        "fr": "Nidoking"
      },
      35: {
        "de": "Piepi",
        "en": "Clefairy",
        "fr": "Mélofée"
      },
      36: {
        "de": "Pixi",
        "en": "Clefable",
        "fr": "Mélodelfe"
      },
      37: {
        "de": "Vulpix",
        "en": "Vulpix",
        "fr": "Goupix"
      },
      38: {
        "de": "Vulnona",
        "en": "Ninetales",
        "fr": "Feunard"
      },
      39: {
        "de": "Pummeluff",
        "en": "Jigglypuff",
        "fr": "Rondoudou"
      },
      40: {
        "de": "Knuddeluff",
        "en": "Wigglytuff",
        "fr": "Grodoudou"
      },
      41: {
        "de": "Zubat",
        "en": "Zubat",
        "fr": "Nosferapti"
      },
      42: {
        "de": "Golbat",
        "en": "Golbat",
        "fr": "Nosferalto"
      },
      43: {
        "de": "Myrapla",
        "en": "Oddish",
        "fr": "Mystherbe"
      },
      44: {
        "de": "Duflor",
        "en": "Gloom",
        "fr": "Ortide"
      },
      45: {
        "de": "Giflor",
        "en": "Vileplume",
        "fr": "Rafflesia"
      },
      46: {
        "de": "Paras",
        "en": "Paras",
        "fr": "Paras"
      },
      47: {
        "de": "Parasek",
        "en": "Parasect",
        "fr": "Parasect"
      },
      48: {
        "de": "Bluzuk",
        "en": "Venonat",
        "fr": "Mimitoss"
      },
      49: {
        "de": "Omot",
        "en": "Venomoth",
        "fr": "Aéromite"
      },
      50: {
        "de": "Digda",
        "en": "Diglett",
        "fr": "Taupiqueur"
      },
      51: {
        "de": "Digdri",
        "en": "Dugtrio",
        "fr": "Triopikeur"
      },
      52: {
        "de": "Mauzi",
        "en": "Meowth",
        "fr": "Miaouss"
      },
      53: {
        "de": "Snobilikat",
        "en": "Persian",
        "fr": "Persian"
      },
      54: {
        "de": "Enton",
        "en": "Psyduck",
        "fr": "Psykokwak"
      },
      55: {
        "de": "Entoron",
        "en": "Golduck",
        "fr": "Akwakwak"
      },
      56: {
        "de": "Menki",
        "en": "Mankey",
        "fr": "Férosinge"
      },
      57: {
        "de": "Rasaff",
        "en": "Primeape",
        "fr": "Colossinge"
      },
      58: {
        "de": "Fukano",
        "en": "Growlithe",
        "fr": "Caninos"
      },
      59: {
        "de": "Arkani",
        "en": "Arcanine",
        "fr": "Arcanin"
      },
      60: {
        "de": "Quapsel",
        "en": "Poliwag",
        "fr": "Ptitard"
      },
      61: {
        "de": "Quaputzi",
        "en": "Poliwhirl",
        "fr": "Têtarte"
      },
      62: {
        "de": "Quappo",
        "en": "Poliwrath",
        "fr": "Tartard"
      },
      63: {
        "de": "Abra",
        "en": "Abra",
        "fr": "Abra"
      },
      64: {
        "de": "Kadabra",
        "en": "Kadabra",
        "fr": "Kadabra"
      },
      65: {
        "de": "Simsala",
        "en": "Alakazam",
        "fr": "Alakazam"
      },
      66: {
        "de": "Machollo",
        "en": "Machop",
        "fr": "Machoc"
      },
      67: {
        "de": "Maschock",
        "en": "Machoke",
        "fr": "Machopeur"
      },
      68: {
        "de": "Machomei",
        "en": "Machamp",
        "fr": "Mackogneur"
      },
      69: {
        "de": "Knofensa",
        "en": "Bellsprout",
        "fr": "Chétiflor"
      },
      70: {
        "de": "Ultrigaria",
        "en": "Weepinbell",
        "fr": "Boustiflor"
      },
      71: {
        "de": "Sarzenia",
        "en": "Victreebel",
        "fr": "Empiflor"
      },
      72: {
        "de": "Tentacha",
        "en": "Tentacool",
        "fr": "Tentacool"
      },
      73: {
        "de": "Tentoxa",
        "en": "Tentacruel",
        "fr": "Tentacruel"
      },
      74: {
        "de": "Kleinstein",
        "en": "Geodude",
        "fr": "Racaillou"
      },
      75: {
        "de": "Georok",
        "en": "Graveler",
        "fr": "Gravalanch"
      },
      76: {
        "de": "Geowaz",
        "en": "Golem",
        "fr": "Grolem"
      },
      77: {
        "de": "Ponita",
        "en": "Ponyta",
        "fr": "Ponyta"
      },
      78: {
        "de": "Gallopa",
        "en": "Rapidash",
        "fr": "Galopa"
      },
      79: {
        "de": "Flegmon",
        "en": "Slowpoke",
        "fr": "Ramoloss"
      },
      80: {
        "de": "Lahmus",
        "en": "Slowbro",
        "fr": "Flagadoss"
      },
      81: {
        "de": "Magnetilo",
        "en": "Magnemite",
        "fr": "Magnéti"
      },
      82: {
        "de": "Magneton",
        "en": "Magneton",
        "fr": "Magnéton"
      },
      83: {
        "de": "Porenta",
        "en": "Farfetch'd",
        "fr": "Canarticho"
      },
      84: {
        "de": "Dodu",
        "en": "Doduo",
        "fr": "Doduo"
      },
      85: {
        "de": "Dodri",
        "en": "Dodrio",
        "fr": "Dodrio"
      },
      86: {
        "de": "Jurob",
        "en": "Seel",
        "fr": "Otaria"
      },
      87: {
        "de": "Jugong",
        "en": "Dewgong",
        "fr": "Lamantine"
      },
      88: {
        "de": "Sleima",
        "en": "Grimer",
        "fr": "Tadmorv"
      },
      89: {
        "de": "Sleimok",
        "en": "Muk",
        "fr": "Grotadmorv"
      },
      90: {
        "de": "Muschas",
        "en": "Shellder",
        "fr": "Kokiyas"
      },
      91: {
        "de": "Austos",
        "en": "Cloyster",
        "fr": "Crustabri"
      },
      92: {
        "de": "Nebulak",
        "en": "Gastly",
        "fr": "Fantominus"
      },
      93: {
        "de": "Alpollo",
        "en": "Haunter",
        "fr": "Spectrum"
      },
      94: {
        "de": "Gengar",
        "en": "Gengar",
        "fr": "Ectoplasma"
      },
      95: {
        "de": "Onix",
        "en": "Onix",
        "fr": "Onix"
      },
      96: {
        "de": "Traumato",
        "en": "Drowzee",
        "fr": "Soporifik"
      },
      97: {
        "de": "Hypno",
        "en": "Hypno",
        "fr": "Hypnomade"
      },
      98: {
        "de": "Krabby",
        "en": "Krabby",
        "fr": "Krabby"
      },
      99: {
        "de": "Kingler",
        "en": "Kingler",
        "fr": "Krabboss"
      },
      100: {
        "de": "Voltobal",
        "en": "Voltorb",
        "fr": "Voltorbe"
      },
      101: {
        "de": "Lektrobal",
        "en": "Electrode",
        "fr": "Électrode"
      },
      102: {
        "de": "Owei",
        "en": "Exeggcute",
        "fr": "Noeunoeuf"
      },
      103: {
        "de": "Kokowei",
        "en": "Exeggutor",
        "fr": "Noadkoko"
      },
      104: {
        "de": "Tragosso",
        "en": "Cubone",
        "fr": "Osselait"
      },
      105: {
        "de": "Knogga",
        "en": "Marowak",
        "fr": "Ossatueur"
      },
      106: {
        "de": "Kicklee",
        "en": "Hitmonlee",
        "fr": "Kicklee"
      },
      107: {
        "de": "Nockchan",
        "en": "Hitmonchan",
        "fr": "Tygnon"
      },
      108: {
        "de": "Schlurp",
        "en": "Lickitung",
        "fr": "Excelangue"
      },
      109: {
        "de": "Smogon",
        "en": "Koffing",
        "fr": "Smogo"
      },
      110: {
        "de": "Smogmog",
        "en": "Weezing",
        "fr": "Smogogo"
      },
      111: {
        "de": "Rihorn",
        "en": "Rhyhorn",
        "fr": "Rhinocorne"
      },
      112: {
        "de": "Rizeros",
        "en": "Rhydon",
        "fr": "Rhinoféros"
      },
      113: {
        "de": "Chaneira",
        "en": "Chansey",
        "fr": "Leveinard"
      },
      114: {
        "de": "Tangela",
        "en": "Tangela",
        "fr": "Saquedeneu"
      },
      115: {
        "de": "Kangama",
        "en": "Kangaskhan",
        "fr": "Kangourex"
      },
      116: {
        "de": "Seeper",
        "en": "Horsea",
        "fr": "Hypotrempe"
      },
      117: {
        "de": "Seemon",
        "en": "Seadra",
        "fr": "Hypocéan"
      },
      118: {
        "de": "Goldini",
        "en": "Goldeen",
        "fr": "Poissirène"
      },
      119: {
        "de": "Golking",
        "en": "Seaking",
        "fr": "Poissoroy"
      },
      120: {
        "de": "Sterndu",
        "en": "Staryu",
        "fr": "Stari"
      },
      121: {
        "de": "Starmie",
        "en": "Starmie",
        "fr": "Staross"
      },
      122: {
        "de": "Pantimos",
        "en": "Mr. Mime",
        "fr": "M. Mime"
      },
      123: {
        "de": "Sichlor",
        "en": "Scyther",
        "fr": "Insécateur"
      },
      124: {
        "de": "Rossana",
        "en": "Jynx",
        "fr": "Lippoutou"
      },
      125: {
        "de": "Elektek",
        "en": "Electabuzz",
        "fr": "Élektek"
      },
      126: {
        "de": "Magmar",
        "en": "Magmar",
        "fr": "Magmar"
      },
      127: {
        "de": "Pinsir",
        "en": "Pinsir",
        "fr": "Scarabrute"
      },
      128: {
        "de": "Tauros",
        "en": "Tauros",
        "fr": "Tauros"
      },
      129: {
        "de": "Karpador",
        "en": "Magikarp",
        "fr": "Magicarpe"
      },
      130: {
        "de": "Garados",
        "en": "Gyarados",
        "fr": "Léviator"
      },
      131: {
        "de": "Lapras",
        "en": "Lapras",
        "fr": "Lokhlass"
      },
      132: {
        "de": "Ditto",
        "en": "Ditto",
        "fr": "Métamorph"
      },
      133: {
        "de": "Evoli",
        "en": "Eevee",
        "fr": "Évoli"
      },
      134: {
        "de": "Aquana",
        "en": "Vaporeon",
        "fr": "Aquali"
      },
      135: {
        "de": "Blitza",
        "en": "Jolteon",
        "fr": "Voltali"
      },
      136: {
        "de": "Flamara",
        "en": "Flareon",
        "fr": "Pyroli"
      },
      137: {
        "de": "Porygon",
        "en": "Porygon",
        "fr": "Porygon"
      },
      138: {
        "de": "Amonitas",
        "en": "Omanyte",
        "fr": "Amonita"
      },
      139: {
        "de": "Amoroso",
        "en": "Omastar",
        "fr": "Amonistar"
      },
      140: {
        "de": "Kabuto",
        "en": "Kabuto",
        "fr": "Kabuto"
      },
      141: {
        "de": "Kabutops",
        "en": "Kabutops",
        "fr": "Kabutops"
      },
      142: {
        "de": "Aerodactyl",
        "en": "Aerodactyl",
        "fr": "Ptéra"
      },
      143: {
        "de": "Relaxo",
        "en": "Snorlax",
        "fr": "Ronflex"
      },
      144: {
        "de": "Arktos",
        "en": "Articuno",
        "fr": "Artikodin"
      },
      145: {
        "de": "Zapdos",
        "en": "Zapdos",
        "fr": "Électhor"
      },
      146: {
        "de": "Lavados",
        "en": "Moltres",
        "fr": "Sulfura"
      },
      147: {
        "de": "Dratini",
        "en": "Dratini",
        "fr": "Minidraco"
      },
      148: {
        "de": "Dragonir",
        "en": "Dragonair",
        "fr": "Draco"
      },
      149: {
        "de": "Dragoran",
        "en": "Dragonite",
        "fr": "Dracolosse"
      },
      150: {
        "de": "Mewtu",
        "en": "Mewtwo",
        "fr": "Mewtwo"
      },
      151: {
        "de": "Mew",
        "en": "Mew",
        "fr": "Mew"
      },
      152: {
        "de": "Endivie",
        "en": "Chikorita",
        "fr": "Germignon"
      },
      153: {
        "de": "Lorblatt",
        "en": "Bayleef",
        "fr": "Macronium"
      },
      154: {
        "de": "Meganie",
        "en": "Meganium",
        "fr": "Méganium"
      },
      155: {
        "de": "Feurigel",
        "en": "Cyndaquil",
        "fr": "Héricendre"
      },
      156: {
        "de": "Igelavar",
        "en": "Quilava",
        "fr": "Feurisson"
      },
      157: {
        "de": "Tornupto",
        "en": "Typhlosion",
        "fr": "Typhlosion"
      },
      158: {
        "de": "Karnimani",
        "en": "Totodile",
        "fr": "Kaiminus"
      },
      159: {
        "de": "Tyracroc",
        "en": "Croconaw",
        "fr": "Crocrodil"
      },
      160: {
        "de": "Impergator",
        "en": "Feraligatr",
        "fr": "Aligatueur"
      },
      161: {
        "de": "Wiesor",
        "en": "Sentret",
        "fr": "Fouinette"
      },
      162: {
        "de": "Wiesenior",
        "en": "Furret",
        "fr": "Fouinar"
      },
      163: {
        "de": "Hoothoot",
        "en": "Hoothoot",
        "fr": "Hoothoot"
      },
      164: {
        "de": "Noctuh",
        "en": "Noctowl",
        "fr": "Noarfang"
      },
      165: {
        "de": "Ledyba",
        "en": "Ledyba",
        "fr": "Coxy"
      },
      166: {
        "de": "Ledian",
        "en": "Ledian",
        "fr": "Coxyclaque"
      },
      167: {
        "de": "Webarak",
        "en": "Spinarak",
        "fr": "Mimigal"
      },
      168: {
        "de": "Ariados",
        "en": "Ariados",
        "fr": "Migalos"
      },
      169: {
        "de": "Iksbat",
        "en": "Crobat",
        "fr": "Nostenfer"
      },
      170: {
        "de": "Lampi",
        "en": "Chinchou",
        "fr": "Loupio"
      },
      171: {
        "de": "Lanturn",
        "en": "Lanturn",
        "fr": "Lanturn"
      },
      172: {
        "de": "Pichu",
        "en": "Pichu",
        "fr": "Pichu"
      },
      173: {
        "de": "Pii",
        "en": "Cleffa",
        "fr": "Mélo"
      },
      174: {
        "de": "Fluffeluff",
        "en": "Igglybuff",
        "fr": "Toudoudou"
      },
      175: {
        "de": "Togepi",
        "en": "Togepi",
        "fr": "Togepi"
      },
      176: {
        "de": "Togetic",
        "en": "Togetic",
        "fr": "Togetic"
      },
      177: {
        "de": "Natu",
        "en": "Natu",
        "fr": "Natu"
      },
      178: {
        "de": "Xatu",
        "en": "Xatu",
        "fr": "Xatu"
      },
      179: {
        "de": "Voltilamm",
        "en": "Mareep",
        "fr": "Wattouat"
      },
      180: {
        "de": "Waaty",
        "en": "Flaaffy",
        "fr": "Lainergie"
      },
      181: {
        "de": "Ampharos",
        "en": "Ampharos",
        "fr": "Pharamp"
      },
      182: {
        "de": "Blubella",
        "en": "Bellossom",
        "fr": "Joliflor"
      },
      183: {
        "de": "Marill",
        "en": "Marill",
        "fr": "Marill"
      },
      184: {
        "de": "Azumarill",
        "en": "Azumarill",
        "fr": "Azumarill"
      },
      185: {
        "de": "Mogelbaum",
        "en": "Sudowoodo",
        "fr": "Simularbre"
      },
      186: {
        "de": "Quaxo",
        "en": "Politoed",
        "fr": "Tarpaud"
      },
      187: {
        "de": "Hoppspross",
        "en": "Hoppip",
        "fr": "Granivol"
      },
      188: {
        "de": "Hubelupf",
        "en": "Skiploom",
        "fr": "Floravol"
      },
      189: {
        "de": "Papungha",
        "en": "Jumpluff",
        "fr": "Cotovol"
      },
      190: {
        "de": "Griffel",
        "en": "Aipom",
        "fr": "Capumain"
      },
      191: {
        "de": "Sonnkern",
        "en": "Sunkern",
        "fr": "Tournegrin"
      },
      192: {
        "de": "Sonnflora",
        "en": "Sunflora",
        "fr": "Héliatronc"
      },
      193: {
        "de": "Yanma",
        "en": "Yanma",
        "fr": "Yanma"
      },
      194: {
        "de": "Felino",
        "en": "Wooper",
        "fr": "Axoloto"
      },
      195: {
        "de": "Morlord",
        "en": "Quagsire",
        "fr": "Maraiste"
      },
      196: {
        "de": "Psiana",
        "en": "Espeon",
        "fr": "Mentali"
      },
      197: {
        "de": "Nachtara",
        "en": "Umbreon",
        "fr": "Noctali"
      },
      198: {
        "de": "Kramurx",
        "en": "Murkrow",
        "fr": "Cornèbre"
      },
      199: {
        "de": "Laschoking",
        "en": "Slowking",
        "fr": "Roigada"
      },
      200: {
        "de": "Traunfugil",
        "en": "Misdreavus",
        "fr": "Feuforêve"
      },
      201: {
        "de": "Icognito",
        "en": "Unown",
        "fr": "Zarbi"
      },
      202: {
        "de": "Woingenau",
        "en": "Wobbuffet",
        "fr": "Qulbutoké"
      },
      203: {
        "de": "Girafarig",
        "en": "Girafarig",
        "fr": "Girafarig"
      },
      204: {
        "de": "Tannza",
        "en": "Pineco",
        "fr": "Pomdepik"
      },
      205: {
        "de": "Forstellka",
        "en": "Forretress",
        "fr": "Foretress"
      },
      206: {
        "de": "Dummisel",
        "en": "Dunsparce",
        "fr": "Insolourdo"
      },
      207: {
        "de": "Skorgla",
        "en": "Gligar",
        "fr": "Scorplane"
      },
      208: {
        "de": "Stahlos",
        "en": "Steelix",
        "fr": "Steelix"
      },
      209: {
        "de": "Snubbull",
        "en": "Snubbull",
        "fr": "Snubbull"
      },
      210: {
        "de": "Granbull",
        "en": "Granbull",
        "fr": "Granbull"
      },
      211: {
        "de": "Baldorfish",
        "en": "Qwilfish",
        "fr": "Qwilfish"
      },
      212: {
        "de": "Scherox",
        "en": "Scizor",
        "fr": "Cizayox"
      },
      213: {
        "de": "Pottrott",
        "en": "Shuckle",
        "fr": "Caratroc"
      },
      214: {
        "de": "Skaraborn",
        "en": "Heracross",
        "fr": "Scarhino"
      },
      215: {
        "de": "Sniebel",
        "en": "Sneasel",
        "fr": "Farfuret"
      },
      216: {
        "de": "Teddiursa",
        "en": "Teddiursa",
        "fr": "Teddiursa"
      },
      217: {
        "de": "Ursaring",
        "en": "Ursaring",
        "fr": "Ursaring"
      },
      218: {
        "de": "Schneckmag",
        "en": "Slugma",
        "fr": "Limagma"
      },
      219: {
        "de": "Magcargo",
        "en": "Magcargo",
        "fr": "Volcaropod"
      },
      220: {
        "de": "Quiekel",
        "en": "Swinub",
        "fr": "Marcacrin"
      },
      221: {
        "de": "Keifel",
        "en": "Piloswine",
        "fr": "Cochignon"
      },
      222: {
        "de": "Corasonn",
        "en": "Corsola",
        "fr": "Corayon"
      },
      223: {
        "de": "Remoraid",
        "en": "Remoraid",
        "fr": "Rémoraid"
      },
      224: {
        "de": "Octillery",
        "en": "Octillery",
        "fr": "Octillery"
      },
      225: {
        "de": "Botogel",
        "en": "Delibird",
        "fr": "Cadoizo"
      },
      226: {
        "de": "Mantax",
        "en": "Mantine",
        "fr": "Démanta"
      },
      227: {
        "de": "Panzaeron",
        "en": "Skarmory",
        "fr": "Airmure"
      },
      228: {
        "de": "Hunduster",
        "en": "Houndour",
        "fr": "Malosse"
      },
      229: {
        "de": "Hundemon",
        "en": "Houndoom",
        "fr": "Démolosse"
      },
      230: {
        "de": "Seedraking",
        "en": "Kingdra",
        "fr": "Hyporoi"
      },
      231: {
        "de": "Phanpy",
        "en": "Phanpy",
        "fr": "Phanpy"
      },
      232: {
        "de": "Donphan",
        "en": "Donphan",
        "fr": "Donphan"
      },
      233: {
        "de": "Porygon2",
        "en": "Porygon2",
        "fr": "Porygon2"
      },
      234: {
        "de": "Damhirplex",
        "en": "Stantler",
        "fr": "Cerfrousse"
      },
      235: {
        "de": "Farbeagle",
        "en": "Smeargle",
        "fr": "Queulorior"
      },
      236: {
        "de": "Rabauz",
        "en": "Tyrogue",
        "fr": "Debugant"
      },
      237: {
        "de": "Kapoera",
        "en": "Hitmontop",
        "fr": "Kapoera"
      },
      238: {
        "de": "Kussilla",
        "en": "Smoochum",
        "fr": "Lippouti"
      },
      239: {
        "de": "Elekid",
        "en": "Elekid",
        "fr": "Élekid"
      },
      240: {
        "de": "Magby",
        "en": "Magby",
        "fr": "Magby"
      },
      241: {
        "de": "Miltank",
        "en": "Miltank",
        "fr": "Écrémeuh"
      },
      242: {
        "de": "Heiteira",
        "en": "Blissey",
        "fr": "Leuphorie"
      },
      243: {
        "de": "Raikou",
        "en": "Raikou",
        "fr": "Raikou"
      },
      244: {
        "de": "Entei",
        "en": "Entei",
        "fr": "Entei"
      },
      245: {
        "de": "Suicune",
        "en": "Suicune",
        "fr": "Suicune"
      },
      246: {
        "de": "Larvitar",
        "en": "Larvitar",
        "fr": "Embrylex"
      },
      247: {
        "de": "Pupitar",
        "en": "Pupitar",
        "fr": "Ymphect"
      },
      248: {
        "de": "Despotar",
        "en": "Tyranitar",
        "fr": "Tyranocif"
      },
      249: {
        "de": "Lugia",
        "en": "Lugia",
        "fr": "Lugia"
      },
      250: {
        "de": "Ho-Oh",
        "en": "Ho-Oh",
        "fr": "Ho-Oh"
      },
      251: {
        "de": "Celebi",
        "en": "Celebi",
        "fr": "Celebi"
      },
      252: {
        "de": "Geckarbor",
        "en": "Treecko",
        "fr": "Arcko"
      },
      253: {
        "de": "Reptain",
        "en": "Grovyle",
        "fr": "Massko"
      },
      254: {
        "de": "Gewaldro",
        "en": "Sceptile",
        "fr": "Jungko"
      },
      255: {
        "de": "Flemmli",
        "en": "Torchic",
        "fr": "Poussifeu"
      },
      256: {
        "de": "Jungglut",
        "en": "Combusken",
        "fr": "Galifeu"
      },
      257: {
        "de": "Lohgock",
        "en": "Blaziken",
        "fr": "Braségali"
      },
      258: {
        "de": "Hydropi",
        "en": "Mudkip",
        "fr": "Gobou"
      },
      259: {
        "de": "Moorabbel",
        "en": "Marshtomp",
        "fr": "Flobio"
      },
      260: {
        "de": "Sumpex",
        "en": "Swampert",
        "fr": "Laggron"
      },
      261: {
        "de": "Fiffyen",
        "en": "Poochyena",
        "fr": "Medhyèna"
      },
      262: {
        "de": "Magnayen",
        "en": "Mightyena",
        "fr": "Grahyèna"
      },
      263: {
        "de": "Zigzachs",
        "en": "Zigzagoon",
        "fr": "Zigzaton"
      },
      264: {
        "de": "Geradaks",
        "en": "Linoone",
        "fr": "Linéon"
      },
      265: {
        "de": "Waumpel",
        "en": "Wurmple",
        "fr": "Chenipotte"
      },
      266: {
        "de": "Schaloko",
        "en": "Silcoon",
        "fr": "Armulys"
      },
      267: {
        "de": "Papinella",
        "en": "Beautifly",
        "fr": "Charmillon"
      },
      268: {
        "de": "Panekon",
        "en": "Cascoon",
        "fr": "Blindalys"
      },
      269: {
        "de": "Pudox",
        "en": "Dustox",
        "fr": "Papinox"
      },
      270: {
        "de": "Loturzel",
        "en": "Lotad",
        "fr": "Nénupiot"
      },
      271: {
        "de": "Lombrero",
        "en": "Lombre",
        "fr": "Lombre"
      },
      272: {
        "de": "Kappalores",
        "en": "Ludicolo",
        "fr": "Ludicolo"
      },
      273: {
        "de": "Samurzel",
        "en": "Seedot",
        "fr": "Grainipiot"
      },
      274: {
        "de": "Blanas",
        "en": "Nuzleaf",
        "fr": "Pifeuil"
      },
      275: {
        "de": "Tengulist",
        "en": "Shiftry",
        "fr": "Tengalice"
      },
      276: {
        "de": "Schwalbini",
        "en": "Taillow",
        "fr": "Nirondelle"
      },
      277: {
        "de": "Schwalboss",
        "en": "Swellow",
        "fr": "Hélédelle"
      },
      278: {
        "de": "Wingull",
        "en": "Wingull",
        "fr": "Goélise"
      },
      279: {
        "de": "Pelipper",
        "en": "Pelipper",
        "fr": "Bekipan"
      },
      280: {
        "de": "Trasla",
        "en": "Ralts",
        "fr": "Tarsal"
      },
      281: {
        "de": "Kirlia",
        "en": "Kirlia",
        "fr": "Kirlia"
      },
      282: {
        "de": "Guardevoir",
        "en": "Gardevoir",
        "fr": "Gardevoir"
      },
      283: {
        "de": "Gehweiher",
        "en": "Surskit",
        "fr": "Arakdo"
      },
      284: {
        "de": "Maskeregen",
        "en": "Masquerain",
        "fr": "Maskadra"
      },
      285: {
        "de": "Knilz",
        "en": "Shroomish",
        "fr": "Balignon"
      },
      286: {
        "de": "Kapilz",
        "en": "Breloom",
        "fr": "Chapignon"
      },
      287: {
        "de": "Bummelz",
        "en": "Slakoth",
        "fr": "Parecool"
      },
      288: {
        "de": "Muntier",
        "en": "Vigoroth",
        "fr": "Vigoroth"
      },
      289: {
        "de": "Letarking",
        "en": "Slaking",
        "fr": "Monaflèmit"
      },
      290: {
        "de": "Nincada",
        "en": "Nincada",
        "fr": "Ningale"
      },
      291: {
        "de": "Ninjask",
        "en": "Ninjask",
        "fr": "Ninjask"
      },
      292: {
        "de": "Ninjatom",
        "en": "Shedinja",
        "fr": "Munja"
      },
      293: {
        "de": "Flurmel",
        "en": "Whismur",
        "fr": "Chuchmur"
      },
      294: {
        "de": "Krakeelo",
        "en": "Loudred",
        "fr": "Ramboum"
      },
      295: {
        "de": "Krawumms",
        "en": "Exploud",
        "fr": "Brouhabam"
      },
      296: {
        "de": "Makuhita",
        "en": "Makuhita",
        "fr": "Makuhita"
      },
      297: {
        "de": "Hariyama",
        "en": "Hariyama",
        "fr": "Hariyama"
      },
      298: {
        "de": "Azurill",
        "en": "Azurill",
        "fr": "Azurill"
      },
      299: {
        "de": "Nasgnet",
        "en": "Nosepass",
        "fr": "Tarinor"
      },
      300: {
        "de": "Eneco",
        "en": "Skitty",
        "fr": "Skitty"
      },
      301: {
        "de": "Enekoro",
        "en": "Delcatty",
        "fr": "Delcatty"
      },
      302: {
        "de": "Zobiris",
        "en": "Sableye",
        "fr": "Ténéfix"
      },
      303: {
        "de": "Flunkifer",
        "en": "Mawile",
        "fr": "Mysdibule"
      },
      304: {
        "de": "Stollunior",
        "en": "Aron",
        "fr": "Galekid"
      },
      305: {
        "de": "Stollrak",
        "en": "Lairon",
        "fr": "Galegon"
      },
      306: {
        "de": "Stolloss",
        "en": "Aggron",
        "fr": "Galeking"
      },
      307: {
        "de": "Meditie",
        "en": "Meditite",
        "fr": "Méditikka"
      },
      308: {
        "de": "Meditalis",
        "en": "Medicham",
        "fr": "Charmina"
      },
      309: {
        "de": "Frizelbliz",
        "en": "Electrike",
        "fr": "Dynavolt"
      },
      310: {
        "de": "Voltenso",
        "en": "Manectric",
        "fr": "Élecsprint"
      },
      311: {
        "de": "Plusle",
        "en": "Plusle",
        "fr": "Posipi"
      },
      312: {
        "de": "Minun",
        "en": "Minun",
        "fr": "Négapi"
      },
      313: {
        "de": "Volbeat",
        "en": "Volbeat",
        "fr": "Muciole"
      },
      314: {
        "de": "Illumise",
        "en": "Illumise",
        "fr": "Lumivole"
      },
      315: {
        "de": "Roselia",
        "en": "Roselia",
        "fr": "Rosélia"
      },
      316: {
        "de": "Schluppuck",
        "en": "Gulpin",
        "fr": "Gloupti"
      },
      317: {
        "de": "Schlukwech",
        "en": "Swalot",
        "fr": "Avaltout"
      },
      318: {
        "de": "Kanivanha",
        "en": "Carvanha",
        "fr": "Carvanha"
      },
      319: {
        "de": "Tohaido",
        "en": "Sharpedo",
        "fr": "Sharpedo"
      },
      320: {
        "de": "Wailmer",
        "en": "Wailmer",
        "fr": "Wailmer"
      },
      321: {
        "de": "Wailord",
        "en": "Wailord",
        "fr": "Wailord"
      },
      322: {
        "de": "Camaub",
        "en": "Numel",
        "fr": "Chamallot"
      },
      323: {
        "de": "Camerupt",
        "en": "Camerupt",
        "fr": "Camérupt"
      },
      324: {
        "de": "Qurtel",
        "en": "Torkoal",
        "fr": "Chartor"
      },
      325: {
        "de": "Spoink",
        "en": "Spoink",
        "fr": "Spoink"
      },
      326: {
        "de": "Groink",
        "en": "Grumpig",
        "fr": "Groret"
      },
      327: {
        "de": "Pandir",
        "en": "Spinda",
        "fr": "Spinda"
      },
      328: {
        "de": "Knacklion",
        "en": "Trapinch",
        "fr": "Kraknoix"
      },
      329: {
        "de": "Vibrava",
        "en": "Vibrava",
        "fr": "Vibraninf"
      },
      330: {
        "de": "Libelldra",
        "en": "Flygon",
        "fr": "Libégon"
      },
      331: {
        "de": "Tuska",
        "en": "Cacnea",
        "fr": "Cacnea"
      },
      332: {
        "de": "Noktuska",
        "en": "Cacturne",
        "fr": "Cacturne"
      },
      333: {
        "de": "Wablu",
        "en": "Swablu",
        "fr": "Tylton"
      },
      334: {
        "de": "Altaria",
        "en": "Altaria",
        "fr": "Altaria"
      },
      335: {
        "de": "Sengo",
        "en": "Zangoose",
        "fr": "Mangriff"
      },
      336: {
        "de": "Vipitis",
        "en": "Seviper",
        "fr": "Séviper"
      },
      337: {
        "de": "Lunastein",
        "en": "Lunatone",
        "fr": "Séléroc"
      },
      338: {
        "de": "Sonnfel",
        "en": "Solrock",
        "fr": "Solaroc"
      },
      339: {
        "de": "Schmerbe",
        "en": "Barboach",
        "fr": "Barloche"
      },
      340: {
        "de": "Welsar",
        "en": "Whiscash",
        "fr": "Barbicha"
      },
      341: {
        "de": "Krebscorps",
        "en": "Corphish",
        "fr": "Écrapince"
      },
      342: {
        "de": "Krebutack",
        "en": "Crawdaunt",
        "fr": "Colhomard"
      },
      343: {
        "de": "Puppance",
        "en": "Baltoy",
        "fr": "Balbuto"
      },
      344: {
        "de": "Lepumentas",
        "en": "Claydol",
        "fr": "Kaorine"
      },
      345: {
        "de": "Liliep",
        "en": "Lileep",
        "fr": "Lilia"
      },
      346: {
        "de": "Wielie",
        "en": "Cradily",
        "fr": "Vacilys"
      },
      347: {
        "de": "Anorith",
        "en": "Anorith",
        "fr": "Anorith"
      },
      348: {
        "de": "Armaldo",
        "en": "Armaldo",
        "fr": "Armaldo"
      },
      349: {
        "de": "Barschwa",
        "en": "Feebas",
        "fr": "Barpau"
      },
      350: {
        "de": "Milotic",
        "en": "Milotic",
        "fr": "Milobellus"
      },
      351: {
        "de": "Formeo",
        "en": "Castform",
        "fr": "Morphéo"
      },
      352: {
        "de": "Kecleon",
        "en": "Kecleon",
        "fr": "Kecleon"
      },
      353: {
        "de": "Shuppet",
        "en": "Shuppet",
        "fr": "Polichombr"
      },
      354: {
        "de": "Banette",
        "en": "Banette",
        "fr": "Branette"
      },
      355: {
        "de": "Zwirrlicht",
        "en": "Duskull",
        "fr": "Skelénox"
      },
      356: {
        "de": "Zwirrklop",
        "en": "Dusclops",
        "fr": "Téraclope"
      },
      357: {
        "de": "Tropius",
        "en": "Tropius",
        "fr": "Tropius"
      },
      358: {
        "de": "Palimpalim",
        "en": "Chimecho",
        "fr": "Éoko"
      },
      359: {
        "de": "Absol",
        "en": "Absol",
        "fr": "Absol"
      },
      360: {
        "de": "Isso",
        "en": "Wynaut",
        "fr": "Okéoké"
      },
      361: {
        "de": "Schneppke",
        "en": "Snorunt",
        "fr": "Stalgamin"
      },
      362: {
        "de": "Firnontor",
        "en": "Glalie",
        "fr": "Oniglali"
      },
      363: {
        "de": "Seemops",
        "en": "Spheal",
        "fr": "Obalie"
      },
      364: {
        "de": "Seejong",
        "en": "Sealeo",
        "fr": "Phogleur"
      },
      365: {
        "de": "Walraisa",
        "en": "Walrein",
        "fr": "Kaimorse"
      },
      366: {
        "de": "Perlu",
        "en": "Clamperl",
        "fr": "Coquiperl"
      },
      367: {
        "de": "Aalabyss",
        "en": "Huntail",
        "fr": "Serpang"
      },
      368: {
        "de": "Saganabyss",
        "en": "Gorebyss",
        "fr": "Rosabyss"
      },
      369: {
        "de": "Relicanth",
        "en": "Relicanth",
        "fr": "Relicanth"
      },
      370: {
        "de": "Liebiskus",
        "en": "Luvdisc",
        "fr": "Lovdisc"
      },
      371: {
        "de": "Kindwurm",
        "en": "Bagon",
        "fr": "Draby"
      },
      372: {
        "de": "Draschel",
        "en": "Shelgon",
        "fr": "Drackhaus"
      },
      373: {
        "de": "Brutalanda",
        "en": "Salamence",
        "fr": "Drattak"
      },
      374: {
        "de": "Tanhel",
        "en": "Beldum",
        "fr": "Terhal"
      },
      375: {
        "de": "Metang",
        "en": "Metang",
        "fr": "Métang"
      },
      376: {
        "de": "Metagross",
        "en": "Metagross",
        "fr": "Métalosse"
      },
      377: {
        "de": "Regirock",
        "en": "Regirock",
        "fr": "Regirock"
      },
      378: {
        "de": "Regice",
        "en": "Regice",
        "fr": "Regice"
      },
      379: {
        "de": "Registeel",
        "en": "Registeel",
        "fr": "Registeel"
      },
      380: {
        "de": "Latias",
        "en": "Latias",
        "fr": "Latias"
      },
      381: {
        "de": "Latios",
        "en": "Latios",
        "fr": "Latios"
      },
      382: {
        "de": "Kyogre",
        "en": "Kyogre",
        "fr": "Kyogre"
      },
      383: {
        "de": "Groudon",
        "en": "Groudon",
        "fr": "Groudon"
      },
      384: {
        "de": "Rayquaza",
        "en": "Rayquaza",
        "fr": "Rayquaza"
      },
      385: {
        "de": "Jirachi",
        "en": "Jirachi",
        "fr": "Jirachi"
      },
      386: {
        "de": "Deoxys",
        "en": "Deoxys",
        "fr": "Deoxys"
      },
      387: {
        "de": "Chelast",
        "en": "Turtwig",
        "fr": "Tortipouss"
      },
      388: {
        "de": "Chelcarain",
        "en": "Grotle",
        "fr": "Boskara"
      },
      389: {
        "de": "Chelterrar",
        "en": "Torterra",
        "fr": "Torterra"
      },
      390: {
        "de": "Panflam",
        "en": "Chimchar",
        "fr": "Ouisticram"
      },
      391: {
        "de": "Panpyro",
        "en": "Monferno",
        "fr": "Chimpenfeu"
      },
      392: {
        "de": "Panferno",
        "en": "Infernape",
        "fr": "Simiabraz"
      },
      393: {
        "de": "Plinfa",
        "en": "Piplup",
        "fr": "Tiplouf"
      },
      394: {
        "de": "Pliprin",
        "en": "Prinplup",
        "fr": "Prinplouf"
      },
      395: {
        "de": "Impoleon",
        "en": "Empoleon",
        "fr": "Pingoléon"
      },
      396: {
        "de": "Staralili",
        "en": "Starly",
        "fr": "Étourmi"
      },
      397: {
        "de": "Staravia",
        "en": "Staravia",
        "fr": "Étourvol"
      },
      398: {
        "de": "Staraptor",
        "en": "Staraptor",
        "fr": "Étouraptor"
      },
      399: {
        "de": "Bidiza",
        "en": "Bidoof",
        "fr": "Keunotor"
      },
      400: {
        "de": "Bidifas",
        "en": "Bibarel",
        "fr": "Castorno"
      },
      401: {
        "de": "Zirpurze",
        "en": "Kricketot",
        "fr": "Crikzik"
      },
      402: {
        "de": "Zirpeise",
        "en": "Kricketune",
        "fr": "Mélokrik"
      },
      403: {
        "de": "Sheinux",
        "en": "Shinx",
        "fr": "Lixy"
      },
      404: {
        "de": "Luxio",
        "en": "Luxio",
        "fr": "Luxio"
      },
      405: {
        "de": "Luxtra",
        "en": "Luxray",
        "fr": "Luxray"
      },
      406: {
        "de": "Knospi",
        "en": "Budew",
        "fr": "Rozbouton"
      },
      407: {
        "de": "Roserade",
        "en": "Roserade",
        "fr": "Roserade"
      },
      408: {
        "de": "Koknodon",
        "en": "Cranidos",
        "fr": "Kranidos"
      },
      409: {
        "de": "Rameidon",
        "en": "Rampardos",
        "fr": "Charkos"
      },
      410: {
        "de": "Schilterus",
        "en": "Shieldon",
        "fr": "Dinoclier"
      },
      411: {
        "de": "Bollterus",
        "en": "Bastiodon",
        "fr": "Bastiodon"
      },
      412: {
        "de": "Burmy",
        "en": "Burmy",
        "fr": "Cheniti"
      },
      413: {
        "de": "Burmadame",
        "en": "Wormadam",
        "fr": "Cheniselle"
      },
      414: {
        "de": "Moterpel",
        "en": "Mothim",
        "fr": "Papilord"
      },
      415: {
        "de": "Wadribie",
        "en": "Combee",
        "fr": "Apitrini"
      },
      416: {
        "de": "Honweisel",
        "en": "Vespiquen",
        "fr": "Apireine"
      },
      417: {
        "de": "Pachirisu",
        "en": "Pachirisu",
        "fr": "Pachirisu"
      },
      418: {
        "de": "Bamelin",
        "en": "Buizel",
        "fr": "Mustébouée"
      },
      419: {
        "de": "Bojelin",
        "en": "Floatzel",
        "fr": "Mustéflott"
      },
      420: {
        "de": "Kikugi",
        "en": "Cherubi",
        "fr": "Ceribou"
      },
      421: {
        "de": "Kinoso",
        "en": "Cherrim",
        "fr": "Ceriflor"
      },
      422: {
        "de": "Schalellos",
        "en": "Shellos",
        "fr": "Sancoki"
      },
      423: {
        "de": "Gastrodon",
        "en": "Gastrodon",
        "fr": "Tritosor"
      },
      424: {
        "de": "Ambidiffel",
        "en": "Ambipom",
        "fr": "Capidextre"
      },
      425: {
        "de": "Driftlon",
        "en": "Drifloon",
        "fr": "Baudrive"
      },
      426: {
        "de": "Drifzepeli",
        "en": "Drifblim",
        "fr": "Grodrive"
      },
      427: {
        "de": "Haspiror",
        "en": "Buneary",
        "fr": "Laporeille"
      },
      428: {
        "de": "Schlapor",
        "en": "Lopunny",
        "fr": "Lockpin"
      },
      429: {
        "de": "Traunmagil",
        "en": "Mismagius",
        "fr": "Magirêve"
      },
      430: {
        "de": "Kramshef",
        "en": "Honchkrow",
        "fr": "Corboss"
      },
      431: {
        "de": "Charmian",
        "en": "Glameow",
        "fr": "Chaglam"
      },
      432: {
        "de": "Shnurgarst",
        "en": "Purugly",
        "fr": "Chaffreux"
      },
      433: {
        "de": "Klingplim",
        "en": "Chingling",
        "fr": "Korillon"
      },
      434: {
        "de": "Skunkapuh",
        "en": "Stunky",
        "fr": "Moufouette"
      },
      435: {
        "de": "Skunktank",
        "en": "Skuntank",
        "fr": "Moufflair"
      },
      436: {
        "de": "Bronzel",
        "en": "Bronzor",
        "fr": "Archéomire"
      },
      437: {
        "de": "Bronzong",
        "en": "Bronzong",
        "fr": "Archéodong"
      },
      438: {
        "de": "Mobai",
        "en": "Bonsly",
        "fr": "Manzaï"
      },
      439: {
        "de": "Pantimimi",
        "en": "Mime Jr.",
        "fr": "Mime Jr"
      },
      440: {
        "de": "Wonneira",
        "en": "Happiny",
        "fr": "Ptiravi"
      },
      441: {
        "de": "Plaudagei",
        "en": "Chatot",
        "fr": "Pijako"
      },
      442: {
        "de": "Kryppuk",
        "en": "Spiritomb",
        "fr": "Spiritomb"
      },
      443: {
        "de": "Kaumalat",
        "en": "Gible",
        "fr": "Griknot"
      },
      444: {
        "de": "Knarksel",
        "en": "Gabite",
        "fr": "Carmache"
      },
      445: {
        "de": "Knakrack",
        "en": "Garchomp",
        "fr": "Carchacrok"
      },
      446: {
        "de": "Mampfaxo",
        "en": "Munchlax",
        "fr": "Goinfrex"
      },
      447: {
        "de": "Riolu",
        "en": "Riolu",
        "fr": "Riolu"
      },
      448: {
        "de": "Lucario",
        "en": "Lucario",
        "fr": "Lucario"
      },
      449: {
        "de": "Hippopotas",
        "en": "Hippopotas",
        "fr": "Hippopotas"
      },
      450: {
        "de": "Hippoterus",
        "en": "Hippowdon",
        "fr": "Hippodocus"
      },
      451: {
        "de": "Pionskora",
        "en": "Skorupi",
        "fr": "Rapion"
      },
      452: {
        "de": "Piondragi",
        "en": "Drapion",
        "fr": "Drascore"
      },
      453: {
        "de": "Glibunkel",
        "en": "Croagunk",
        "fr": "Cradopaud"
      },
      454: {
        "de": "Toxiquak",
        "en": "Toxicroak",
        "fr": "Coatox"
      },
      455: {
        "de": "Venuflibis",
        "en": "Carnivine",
        "fr": "Vortente"
      },
      456: {
        "de": "Finneon",
        "en": "Finneon",
        "fr": "Écayon"
      },
      457: {
        "de": "Lumineon",
        "en": "Lumineon",
        "fr": "Luminéon"
      },
      458: {
        "de": "Mantirps",
        "en": "Mantyke",
        "fr": "Babimanta"
      },
      459: {
        "de": "Shnebedeck",
        "en": "Snover",
        "fr": "Blizzi"
      },
      460: {
        "de": "Rexblisar",
        "en": "Abomasnow",
        "fr": "Blizzaroi"
      },
      461: {
        "de": "Snibunna",
        "en": "Weavile",
        "fr": "Dimoret"
      },
      462: {
        "de": "Magnezone",
        "en": "Magnezone",
        "fr": "Magnézone"
      },
      463: {
        "de": "Schlurplek",
        "en": "Lickilicky",
        "fr": "Coudlangue"
      },
      464: {
        "de": "Rihornior",
        "en": "Rhyperior",
        "fr": "Rhinastoc"
      },
      465: {
        "de": "Tangoloss",
        "en": "Tangrowth",
        "fr": "Bouldeneu"
      },
      466: {
        "de": "Elevoltek",
        "en": "Electivire",
        "fr": "Élekable"
      },
      467: {
        "de": "Magbrant",
        "en": "Magmortar",
        "fr": "Maganon"
      },
      468: {
        "de": "Togekiss",
        "en": "Togekiss",
        "fr": "Togekiss"
      },
      469: {
        "de": "Yanmega",
        "en": "Yanmega",
        "fr": "Yanmega"
      },
      470: {
        "de": "Folipurba",
        "en": "Leafeon",
        "fr": "Phyllali"
      },
      471: {
        "de": "Glaziola",
        "en": "Glaceon",
        "fr": "Givrali"
      },
      472: {
        "de": "Skorgro",
        "en": "Gliscor",
        "fr": "Scorvol"
      },
      473: {
        "de": "Mamutel",
        "en": "Mamoswine",
        "fr": "Mammochon"
      },
      474: {
        "de": "Porygon-Z",
        "en": "Porygon-Z",
        "fr": "Porygon-Z"
      },
      475: {
        "de": "Galagladi",
        "en": "Gallade",
        "fr": "Gallame"
      },
      476: {
        "de": "Voluminas",
        "en": "Probopass",
        "fr": "Tarinorme"
      },
      477: {
        "de": "Zwirrfinst",
        "en": "Dusknoir",
        "fr": "Noctunoir"
      },
      478: {
        "de": "Frosdedje",
        "en": "Froslass",
        "fr": "Momartik"
      },
      479: {
        "de": "Rotom",
        "en": "Rotom",
        "fr": "Motisma"
      },
      480: {
        "de": "Selfe",
        "en": "Uxie",
        "fr": "Créhelf"
      },
      481: {
        "de": "Vesprit",
        "en": "Mesprit",
        "fr": "Créfollet"
      },
      482: {
        "de": "Tobutz",
        "en": "Azelf",
        "fr": "Créfadet"
      },
      483: {
        "de": "Dialga",
        "en": "Dialga",
        "fr": "Dialga"
      },
      484: {
        "de": "Palkia",
        "en": "Palkia",
        "fr": "Palkia"
      },
      485: {
        "de": "Heatran",
        "en": "Heatran",
        "fr": "Heatran"
      },
      486: {
        "de": "Regigigas",
        "en": "Regigigas",
        "fr": "Regigigas"
      },
      487: {
        "de": "Giratina",
        "en": "Giratina",
        "fr": "Giratina"
      },
      488: {
        "de": "Cresselia",
        "en": "Cresselia",
        "fr": "Cresselia"
      },
      489: {
        "de": "Phione",
        "en": "Phione",
        "fr": "Phione"
      },
      490: {
        "de": "Manaphy",
        "en": "Manaphy",
        "fr": "Manaphy"
      },
      491: {
        "de": "Darkrai",
        "en": "Darkrai",
        "fr": "Darkrai"
      },
      492: {
        "de": "Shaymin",
        "en": "Shaymin",
        "fr": "Shaymin"
      },
      493: {
        "de": "Arceus",
        "en": "Arceus",
        "fr": "Arceus"
      },
      494: {
        "de": "Victini",
        "en": "Victini",
        "fr": "Victini"
      },
      495: {
        "de": "Serpifeu",
        "en": "Snivy",
        "fr": "Vipélierre"
      },
      496: {
        "de": "Efoserp",
        "en": "Servine",
        "fr": "Lianaja"
      },
      497: {
        "de": "Serpiroyal",
        "en": "Serperior",
        "fr": "Majaspic"
      },
      498: {
        "de": "Floink",
        "en": "Tepig",
        "fr": "Gruikui"
      },
      499: {
        "de": "Ferkokel",
        "en": "Pignite",
        "fr": "Grotichon"
      },
      500: {
        "de": "Flambirex",
        "en": "Emboar",
        "fr": "Roitiflam"
      },
      501: {
        "de": "Ottaro",
        "en": "Oshawott",
        "fr": "Moustillon"
      },
      502: {
        "de": "Zwottronin",
        "en": "Dewott",
        "fr": "Mateloutre"
      },
      503: {
        "de": "Admurai",
        "en": "Samurott",
        "fr": "Clamiral"
      },
      504: {
        "de": "Nagelotz",
        "en": "Patrat",
        "fr": "Ratentif"
      },
      505: {
        "de": "Kukmarda",
        "en": "Watchog",
        "fr": "Miradar"
      },
      506: {
        "de": "Yorkleff",
        "en": "Lillipup",
        "fr": "Ponchiot"
      },
      507: {
        "de": "Terribark",
        "en": "Herdier",
        "fr": "Ponchien"
      },
      508: {
        "de": "Bissbark",
        "en": "Stoutland",
        "fr": "Mastouffe"
      },
      509: {
        "de": "Felilou",
        "en": "Purrloin",
        "fr": "Chacripan"
      },
      510: {
        "de": "Kleoparda",
        "en": "Liepard",
        "fr": "Léopardus"
      },
      511: {
        "de": "Vegimak",
        "en": "Pansage",
        "fr": "Feuillajou"
      },
      512: {
        "de": "Vegichita",
        "en": "Simisage",
        "fr": "Feuiloutan"
      },
      513: {
        "de": "Grillmak",
        "en": "Pansear",
        "fr": "Flamajou"
      },
      514: {
        "de": "Grillchita",
        "en": "Simisear",
        "fr": "Flamoutan"
      },
      515: {
        "de": "Sodamak",
        "en": "Panpour",
        "fr": "Flotajou"
      },
      516: {
        "de": "Sodachita",
        "en": "Simipour",
        "fr": "Flotoutan"
      },
      517: {
        "de": "Somniam",
        "en": "Munna",
        "fr": "Munna"
      },
      518: {
        "de": "Somnivora",
        "en": "Musharna",
        "fr": "Mushana"
      },
      519: {
        "de": "Dusselgurr",
        "en": "Pidove",
        "fr": "Poichigeon"
      },
      520: {
        "de": "Navitaub",
        "en": "Tranquill",
        "fr": "Colombeau"
      },
      521: {
        "de": "Fasasnob",
        "en": "Unfezant",
        "fr": "Déflaisan"
      },
      522: {
        "de": "Elezeba",
        "en": "Blitzle",
        "fr": "Zébibron"
      },
      523: {
        "de": "Zebritz",
        "en": "Zebstrika",
        "fr": "Zéblitz"
      },
      524: {
        "de": "Kiesling",
        "en": "Roggenrola",
        "fr": "Nodulithe"
      },
      525: {
        "de": "Sedimantur",
        "en": "Boldore",
        "fr": "Géolithe"
      },
      526: {
        "de": "Brockoloss",
        "en": "Gigalith",
        "fr": "Gigalithe"
      },
      527: {
        "de": "Fleknoil",
        "en": "Woobat",
        "fr": "Chovsourir"
      },
      528: {
        "de": "Fletiamo",
        "en": "Swoobat",
        "fr": "Rhinolove"
      },
      529: {
        "de": "Rotomurf",
        "en": "Drilbur",
        "fr": "Rototaupe"
      },
      530: {
        "de": "Stalobor",
        "en": "Excadrill",
        "fr": "Minotaupe"
      },
      531: {
        "de": "Ohrdoch",
        "en": "Audino",
        "fr": "Nanméouïe"
      },
      532: {
        "de": "Praktibalk",
        "en": "Timburr",
        "fr": "Charpenti"
      },
      533: {
        "de": "Strepoli",
        "en": "Gurdurr",
        "fr": "Ouvrifier"
      },
      534: {
        "de": "Meistagrif",
        "en": "Conkeldurr",
        "fr": "Bétochef"
      },
      535: {
        "de": "Schallquap",
        "en": "Tympole",
        "fr": "Tritonde"
      },
      536: {
        "de": "Mebrana",
        "en": "Palpitoad",
        "fr": "Batracné"
      },
      537: {
        "de": "Branawarz",
        "en": "Seismitoad",
        "fr": "Crapustule"
      },
      538: {
        "de": "Jiutesto",
        "en": "Throh",
        "fr": "Judokrak"
      },
      539: {
        "de": "Karadonis",
        "en": "Sawk",
        "fr": "Karaclée"
      },
      540: {
        "de": "Strawickl",
        "en": "Sewaddle",
        "fr": "Larveyette"
      },
      541: {
        "de": "Folikon",
        "en": "Swadloon",
        "fr": "Couverdure"
      },
      542: {
        "de": "Matrifol",
        "en": "Leavanny",
        "fr": "Manternel"
      },
      543: {
        "de": "Toxiped",
        "en": "Venipede",
        "fr": "Venipatte"
      },
      544: {
        "de": "Rollum",
        "en": "Whirlipede",
        "fr": "Scobolide"
      },
      545: {
        "de": "Cerapendra",
        "en": "Scolipede",
        "fr": "Brutapode"
      },
      546: {
        "de": "Waumboll",
        "en": "Cottonee",
        "fr": "Doudouvet"
      },
      547: {
        "de": "Elfun",
        "en": "Whimsicott",
        "fr": "Farfaduvet"
      },
      548: {
        "de": "Lilminip",
        "en": "Petilil",
        "fr": "Chlorobule"
      },
      549: {
        "de": "Dressella",
        "en": "Lilligant",
        "fr": "Fragilady"
      },
      550: {
        "de": "Barschuft",
        "en": "Basculin",
        "fr": "Bargantua"
      },
      551: {
        "de": "Ganovil",
        "en": "Sandile",
        "fr": "Mascaïman"
      },
      552: {
        "de": "Rokkaiman",
        "en": "Krokorok",
        "fr": "Escroco"
      },
      553: {
        "de": "Rabigator",
        "en": "Krookodile",
        "fr": "Crocorible"
      },
      554: {
        "de": "Flampion",
        "en": "Darumaka",
        "fr": "Darumarond"
      },
      555: {
        "de": "Flampivian",
        "en": "Darmanitan",
        "fr": "Darumacho"
      },
      556: {
        "de": "Maracamba",
        "en": "Maractus",
        "fr": "Maracachi"
      },
      557: {
        "de": "Lithomith",
        "en": "Dwebble",
        "fr": "Crabicoque"
      },
      558: {
        "de": "Castellith",
        "en": "Crustle",
        "fr": "Crabaraque"
      },
      559: {
        "de": "Zurrokex",
        "en": "Scraggy",
        "fr": "Baggiguane"
      },
      560: {
        "de": "Irokex",
        "en": "Scrafty",
        "fr": "Baggaïd"
      },
      561: {
        "de": "Symvolara",
        "en": "Sigilyph",
        "fr": "Cryptéro"
      },
      562: {
        "de": "Makabaja",
        "en": "Yamask",
        "fr": "Tutafeh"
      },
      563: {
        "de": "Echnatoll",
        "en": "Cofagrigus",
        "fr": "Tutankafer"
      },
      564: {
        "de": "Galapaflos",
        "en": "Tirtouga",
        "fr": "Carapagos"
      },
      565: {
        "de": "Karippas",
        "en": "Carracosta",
        "fr": "Mégapagos"
      },
      566: {
        "de": "Flapteryx",
        "en": "Archen",
        "fr": "Arkéapti"
      },
      567: {
        "de": "Aeropteryx",
        "en": "Archeops",
        "fr": "Aéroptéryx"
      },
      568: {
        "de": "Unratütox",
        "en": "Trubbish",
        "fr": "Miamiasme"
      },
      569: {
        "de": "Deponitox",
        "en": "Garbodor",
        "fr": "Miasmax"
      },
      570: {
        "de": "Zorua",
        "en": "Zorua",
        "fr": "Zorua"
      },
      571: {
        "de": "Zoroark",
        "en": "Zoroark",
        "fr": "Zoroark"
      },
      572: {
        "de": "Picochilla",
        "en": "Minccino",
        "fr": "Chinchidou"
      },
      573: {
        "de": "Chillabell",
        "en": "Cinccino",
        "fr": "Pashmilla"
      },
      574: {
        "de": "Mollimorba",
        "en": "Gothita",
        "fr": "Scrutella"
      },
      575: {
        "de": "Hypnomorba",
        "en": "Gothorita",
        "fr": "Mesmérella"
      },
      576: {
        "de": "Morbitesse",
        "en": "Gothitelle",
        "fr": "Sidérella"
      },
      577: {
        "de": "Monozyto",
        "en": "Solosis",
        "fr": "Nucléos"
      },
      578: {
        "de": "Mitodos",
        "en": "Duosion",
        "fr": "Méios"
      },
      579: {
        "de": "Zytomega",
        "en": "Reuniclus",
        "fr": "Symbios"
      },
      580: {
        "de": "Piccolente",
        "en": "Ducklett",
        "fr": "Couaneton"
      },
      581: {
        "de": "Swaroness",
        "en": "Swanna",
        "fr": "Lakmécygne"
      },
      582: {
        "de": "Gelatini",
        "en": "Vanillite",
        "fr": "Sorbébé"
      },
      583: {
        "de": "Gelatroppo",
        "en": "Vanillish",
        "fr": "Sorboul"
      },
      584: {
        "de": "Gelatwino",
        "en": "Vanilluxe",
        "fr": "Sorbouboul"
      },
      585: {
        "de": "Sesokitz",
        "en": "Deerling",
        "fr": "Vivaldaim"
      },
      586: {
        "de": "Kronjuwild",
        "en": "Sawsbuck",
        "fr": "Haydaim"
      },
      587: {
        "de": "Emolga",
        "en": "Emolga",
        "fr": "Emolga"
      },
      588: {
        "de": "Laukaps",
        "en": "Karrablast",
        "fr": "Carabing"
      },
      589: {
        "de": "Cavalanzas",
        "en": "Escavalier",
        "fr": "Lançargot"
      },
      590: {
        "de": "Tarnpignon",
        "en": "Foongus",
        "fr": "Trompignon"
      },
      591: {
        "de": "Hutsassa",
        "en": "Amoonguss",
        "fr": "Gaulet"
      },
      592: {
        "de": "Quabbel",
        "en": "Frillish",
        "fr": "Viskuse"
      },
      593: {
        "de": "Apoquallyp",
        "en": "Jellicent",
        "fr": "Moyade"
      },
      594: {
        "de": "Mamolida",
        "en": "Alomomola",
        "fr": "Mamanbo"
      },
      595: {
        "de": "Wattzapf",
        "en": "Joltik",
        "fr": "Statitik"
      },
      596: {
        "de": "Voltula",
        "en": "Galvantula",
        "fr": "Mygavolt"
      },
      597: {
        "de": "Kastadur",
        "en": "Ferroseed",
        "fr": "Grindur"
      },
      598: {
        "de": "Tentantel",
        "en": "Ferrothorn",
        "fr": "Noacier"
      },
      599: {
        "de": "Klikk",
        "en": "Klink",
        "fr": "Tic"
      },
      600: {
        "de": "Kliklak",
        "en": "Klang",
        "fr": "Clic"
      },
      601: {
        "de": "Klikdiklak",
        "en": "Klinklang",
        "fr": "Cliticlic"
      },
      602: {
        "de": "Zapplardin",
        "en": "Tynamo",
        "fr": "Anchwatt"
      },
      603: {
        "de": "Zapplalek",
        "en": "Eelektrik",
        "fr": "Lampéroie"
      },
      604: {
        "de": "Zapplarang",
        "en": "Eelektross",
        "fr": "Ohmassacre"
      },
      605: {
        "de": "Pygraulon",
        "en": "Elgyem",
        "fr": "Lewsor"
      },
      606: {
        "de": "Megalon",
        "en": "Beheeyem",
        "fr": "Neitram"
      },
      607: {
        "de": "Lichtel",
        "en": "Litwick",
        "fr": "Funécire"
      },
      608: {
        "de": "Laternecto",
        "en": "Lampent",
        "fr": "Mélancolux"
      },
      609: {
        "de": "Skelabra",
        "en": "Chandelure",
        "fr": "Lugulabre"
      },
      610: {
        "de": "Milza",
        "en": "Axew",
        "fr": "Coupenotte"
      },
      611: {
        "de": "Sharfax",
        "en": "Fraxure",
        "fr": "Incisache"
      },
      612: {
        "de": "Maxax",
        "en": "Haxorus",
        "fr": "Tranchodon"
      },
      613: {
        "de": "Petznief",
        "en": "Cubchoo",
        "fr": "Polarhume"
      },
      614: {
        "de": "Siberio",
        "en": "Beartic",
        "fr": "Polagriffe"
      },
      615: {
        "de": "Frigometri",
        "en": "Cryogonal",
        "fr": "Hexagel"
      },
      616: {
        "de": "Schnuthelm",
        "en": "Shelmet",
        "fr": "Escargaume"
      },
      617: {
        "de": "Hydragil",
        "en": "Accelgor",
        "fr": "Limaspeed"
      },
      618: {
        "de": "Flunschlik",
        "en": "Stunfisk",
        "fr": "Limonde"
      },
      619: {
        "de": "Fu",
        "en": "Mienfoo",
        "fr": "Kungfouine"
      },
      620: {
        "de": "Shu",
        "en": "Mienshao",
        "fr": "Shaofouine"
      },
      621: {
        "de": "Shardrago",
        "en": "Druddigon",
        "fr": "Drakkarmin"
      },
      622: {
        "de": "Golbit",
        "en": "Golett",
        "fr": "Gringolem"
      },
      623: {
        "de": "Golgantes",
        "en": "Golurk",
        "fr": "Golemastoc"
      },
      624: {
        "de": "Gladiantri",
        "en": "Pawniard",
        "fr": "Scalpion"
      },
      625: {
        "de": "Caesurio",
        "en": "Bisharp",
        "fr": "Scalproie"
      },
      626: {
        "de": "Bisofank",
        "en": "Bouffalant",
        "fr": "Frison"
      },
      627: {
        "de": "Geronimatz",
        "en": "Rufflet",
        "fr": "Furaiglon"
      },
      628: {
        "de": "Washakwil",
        "en": "Braviary",
        "fr": "Gueriaigle"
      },
      629: {
        "de": "Skallyk",
        "en": "Vullaby",
        "fr": "Vostourno"
      },
      630: {
        "de": "Grypheldis",
        "en": "Mandibuzz",
        "fr": "Vaututrice"
      },
      631: {
        "de": "Furnifraß",
        "en": "Heatmor",
        "fr": "Aflamanoir"
      },
      632: {
        "de": "Fermicula",
        "en": "Durant",
        "fr": "Fermite"
      },
      633: {
        "de": "Kapuno",
        "en": "Deino",
        "fr": "Solochi"
      },
      634: {
        "de": "Duodino",
        "en": "Zweilous",
        "fr": "Diamat"
      },
      635: {
        "de": "Trikephalo",
        "en": "Hydreigon",
        "fr": "Trioxhydre"
      },
      636: {
        "de": "Ignivor",
        "en": "Larvesta",
        "fr": "Pyronille"
      },
      637: {
        "de": "Ramoth",
        "en": "Volcarona",
        "fr": "Pyrax"
      },
      638: {
        "de": "Kobalium",
        "en": "Cobalion",
        "fr": "Cobaltium"
      },
      639: {
        "de": "Terrakium",
        "en": "Terrakion",
        "fr": "Terrakium"
      },
      640: {
        "de": "Viridium",
        "en": "Virizion",
        "fr": "Viridium"
      },
      641: {
        "de": "Boreos",
        "en": "Tornadus",
        "fr": "Boréas"
      },
      642: {
        "de": "Voltolos",
        "en": "Thundurus",
        "fr": "Fulguris"
      },
      643: {
        "de": "Reshiram",
        "en": "Reshiram",
        "fr": "Reshiram"
      },
      644: {
        "de": "Zekrom",
        "en": "Zekrom",
        "fr": "Zekrom"
      },
      645: {
        "de": "Demeteros",
        "en": "Landorus",
        "fr": "Démétéros"
      },
      646: {
        "de": "Kyurem",
        "en": "Kyurem",
        "fr": "Kyurem"
      },
      647: {
        "de": "Keldeo",
        "en": "Keldeo",
        "fr": "Keldeo"
      },
      648: {
        "de": "Meloetta",
        "en": "Meloetta",
        "fr": "Meloetta"
      },
      649: {
        "de": "Genesect",
        "en": "Genesect",
        "fr": "Genesect"
      },
      650: {
        "de": "Igamaro",
        "en": "Chespin",
        "fr": "Marisson"
      },
      651: {
        "de": "Igastarnish",
        "en": "Quilladin",
        "fr": "Boguérisse"
      },
      652: {
        "de": "Brigaron",
        "en": "Chesnaught",
        "fr": "Blindépique"
      },
      653: {
        "de": "Fynx",
        "en": "Fennekin",
        "fr": "Feunnec"
      },
      654: {
        "de": "Rutena",
        "en": "Braixen",
        "fr": "Roussil"
      },
      655: {
        "de": "Fennexis",
        "en": "Delphox",
        "fr": "Goupelin"
      },
      656: {
        "de": "Froxy",
        "en": "Froakie",
        "fr": "Grenousse"
      },
      657: {
        "de": "Amphizel",
        "en": "Frogadier",
        "fr": "Croâporal"
      },
      658: {
        "de": "Quajutsu",
        "en": "Greninja",
        "fr": "Amphinobi"
      },
      659: {
        "de": "Scoppel",
        "en": "Bunnelby",
        "fr": "Sapereau"
      },
      660: {
        "de": "Grebbit",
        "en": "Diggersby",
        "fr": "Excavarenne"
      },
      661: {
        "de": "Dartiri",
        "en": "Fletchling",
        "fr": "Passerouge"
      },
      662: {
        "de": "Dartignis",
        "en": "Fletchinder",
        "fr": "Braisillon"
      },
      663: {
        "de": "Fiaro",
        "en": "Talonflame",
        "fr": "Flambusard"
      },
      664: {
        "de": "Purmel",
        "en": "Scatterbug",
        "fr": "Lépidonille"
      },
      665: {
        "de": "Puponcho",
        "en": "Spewpa",
        "fr": "Pérégrain"
      },
      666: {
        "de": "Vivillon",
        "en": "Vivillon",
        "fr": "Prismillon"
      },
      667: {
        "de": "Leufeo",
        "en": "Litleo",
        "fr": "Hélionceau"
      },
      668: {
        "de": "Pyroleo",
        "en": "Pyroar",
        "fr": "Némélios"
      },
      669: {
        "de": "Flabébé",
        "en": "Flabébé",
        "fr": "Flabébé"
      },
      670: {
        "de": "Floette",
        "en": "Floette",
        "fr": "FLOETTE"
      },
      671: {
        "de": "Florges",
        "en": "Florges",
        "fr": "Florges"
      },
      672: {
        "de": "Mähikel",
        "en": "Skiddo",
        "fr": "Cabriolaine"
      },
      673: {
        "de": "Chevrumm",
        "en": "Gogoat",
        "fr": "Chevroum"
      },
      674: {
        "de": "Pam",
        "en": "Pancham",
        "fr": "Pandespiègle"
      },
      675: {
        "de": "Pandagro",
        "en": "Pangoro",
        "fr": "Pandarbare"
      },
      676: {
        "de": "Coiffwaff",
        "en": "Furfrou",
        "fr": "Couafarel"
      },
      677: {
        "de": "Psiau",
        "en": "Espurr",
        "fr": "Psystigri"
      },
      678: {
        "de": "Psiaugon",
        "en": "Meowstic",
        "fr": "Mistigrix"
      },
      679: {
        "de": "Gramokles",
        "en": "Honedge",
        "fr": "Monorpale"
      },
      680: {
        "de": "Duokles",
        "en": "Doublade",
        "fr": "Dimoclès"
      },
      681: {
        "de": "Durengard",
        "en": "Aegislash",
        "fr": "Exagide"
      },
      682: {
        "de": "Parfi",
        "en": "Spritzee",
        "fr": "Fluvetin"
      },
      683: {
        "de": "Parfinesse",
        "en": "Aromatisse",
        "fr": "Cocotine"
      },
      684: {
        "de": "Flauschling",
        "en": "Swirlix",
        "fr": "Sucroquin"
      },
      685: {
        "de": "Sabbaione",
        "en": "Slurpuff",
        "fr": "Cupcanaille"
      },
      686: {
        "de": "Iscalar",
        "en": "Inkay",
        "fr": "Sepiatop"
      },
      687: {
        "de": "Calamanero",
        "en": "Malamar",
        "fr": "Sepiatroce"
      },
      688: {
        "de": "Bithora",
        "en": "Binacle",
        "fr": "Opermine"
      },
      689: {
        "de": "Thanathora",
        "en": "Barbaracle",
        "fr": "Golgopathe"
      },
      690: {
        "de": "Algitt",
        "en": "Skrelp",
        "fr": "Venalgue"
      },
      691: {
        "de": "Tandrak",
        "en": "Dragalge",
        "fr": "Kravarech"
      },
      692: {
        "de": "Scampisto",
        "en": "Clauncher",
        "fr": "Flingouste"
      },
      693: {
        "de": "Wummer",
        "en": "Clawitzer",
        "fr": "Gamblast"
      },
      694: {
        "de": "Eguana",
        "en": "Helioptile",
        "fr": "Galvaran"
      },
      695: {
        "de": "Elezard",
        "en": "Heliolisk",
        "fr": "Iguolta"
      },
      696: {
        "de": "Balgoras",
        "en": "Tyrunt",
        "fr": "Ptyranidur"
      },
      697: {
        "de": "Monargoras",
        "en": "Tyrantrum",
        "fr": "Rexillius"
      },
      698: {
        "de": "Amarino",
        "en": "Amaura",
        "fr": "Amagara"
      },
      699: {
        "de": "Amagarga",
        "en": "Aurorus",
        "fr": "Dragmara"
      },
      700: {
        "de": "Feelinara",
        "en": "Sylveon",
        "fr": "Nymphali"
      },
      701: {
        "de": "Resladero",
        "en": "Hawlucha",
        "fr": "Brutalibré"
      },
      702: {
        "de": "Dedenne",
        "en": "Dedenne",
        "fr": "DEDENNE"
      },
      703: {
        "de": "Rocara",
        "en": "Carbink",
        "fr": "Strassie"
      },
      704: {
        "de": "Viscora",
        "en": "Goomy",
        "fr": "Mucuscule"
      },
      705: {
        "de": "Viscargot",
        "en": "Sliggoo",
        "fr": "Colimucus"
      },
      706: {
        "de": "Viscogon",
        "en": "Goodra",
        "fr": "Muplodocus"
      },
      707: {
        "de": "Clavion",
        "en": "Klefki",
        "fr": "Trousselin"
      },
      708: {
        "de": "Paragoni",
        "en": "Phantump",
        "fr": "Brocélôme"
      },
      709: {
        "de": "Trombork",
        "en": "Trevenant",
        "fr": "Desséliande"
      },
      710: {
        "de": "Irrbis",
        "en": "Pumpkaboo",
        "fr": "Pitrouille"
      },
      711: {
        "de": "Pumpdjinn",
        "en": "Gourgeist",
        "fr": "Banshitrouye"
      },
      712: {
        "de": "Arktip",
        "en": "Bergmite",
        "fr": "Grelaçon"
      },
      713: {
        "de": "Arktilas",
        "en": "Avalugg",
        "fr": "Séracrawl"
      },
      714: {
        "de": "eF-eM",
        "en": "Noibat",
        "fr": "Sonistrelle"
      },
      715: {
        "de": "UHaFnir",
        "en": "Noivern",
        "fr": "Bruyverne"
      },
      716: {
        "de": "Xerneas",
        "en": "Xerneas",
        "fr": "Xerneas"
      },
      717: {
        "de": "Yveltal",
        "en": "Yveltal",
        "fr": "Yveltal"
      },
      718: {
        "de": "Zygarde",
        "en": "Zygarde",
        "fr": "Zygarde"
      },
      719: {
        "de": "Diancie",
        "en": "Diancie",
        "fr": "Diancie"
      },
      720: {
        "de": "Hoopa",
        "en": "Hoopa",
        "fr": "Hoopa"
      },
      721: {
        "de": "Volcanion",
        "en": "Volcanion",
        "fr": "Volcanion"
      },
      722: {
        "de": "Bauz",
        "en": "Rowlet",
        "fr": "Brindibou"
      },
      723: {
        "de": "Arboretoss",
        "en": "Dartrix",
        "fr": "Efflèche"
      },
      724: {
        "de": "Silvarro",
        "en": "Decidueye",
        "fr": "Archéduc"
      },
      725: {
        "de": "Flamiau",
        "en": "Litten",
        "fr": "Flamiaou"
      },
      726: {
        "de": "Miezunder",
        "en": "Torracat",
        "fr": "Matoufeu"
      },
      727: {
        "de": "Fuegro",
        "en": "Incineroar",
        "fr": "Félinferno"
      },
      728: {
        "de": "Robball",
        "en": "Popplio",
        "fr": "Otaquin"
      },
      729: {
        "de": "Marikeck",
        "en": "Brionne",
        "fr": "Otarlette"
      },
      730: {
        "de": "Primarene",
        "en": "Primarina",
        "fr": "Oratoria"
      },
      731: {
        "de": "Peppeck",
        "en": "Pikipek",
        "fr": "Picassaut"
      },
      732: {
        "de": "Trompeck",
        "en": "Trumbeak",
        "fr": "Piclairon"
      },
      733: {
        "de": "Tukanon",
        "en": "Toucannon",
        "fr": "Bazoucan"
      },
      734: {
        "de": "Mangunior",
        "en": "Yungoos",
        "fr": "Manglouton"
      },
      735: {
        "de": "Manguspektor",
        "en": "Gumshoos",
        "fr": "Argouste"
      },
      736: {
        "de": "Mabula",
        "en": "Grubbin",
        "fr": "Larvibule"
      },
      737: {
        "de": "Akkup",
        "en": "Charjabug",
        "fr": "Chrysapile"
      },
      738: {
        "de": "Donarion",
        "en": "Vikavolt",
        "fr": "Lucanon"
      },
      739: {
        "de": "Krabbox",
        "en": "Crabrawler",
        "fr": "Crabagarre"
      },
      740: {
        "de": "Krawell",
        "en": "Crabominable",
        "fr": "Crabominable"
      },
      741: {
        "de": "Choreogel",
        "en": "Oricorio",
        "fr": "Plumeline"
      },
      742: {
        "de": "Wommel",
        "en": "Cutiefly",
        "fr": "Bombydou"
      },
      743: {
        "de": "Bandelby",
        "en": "Ribombee",
        "fr": "Rubombelle"
      },
      744: {
        "de": "Wuffels",
        "en": "Rockruff",
        "fr": "Rocabot"
      },
      745: {
        "de": "Wolwerock",
        "en": "Lycanroc",
        "fr": "Lougaroc"
      },
      746: {
        "de": "Lusardin",
        "en": "Wishiwashi",
        "fr": "Froussardine"
      },
      747: {
        "de": "Garstella",
        "en": "Mareanie",
        "fr": "Vorastérie"
      },
      748: {
        "de": "Aggrostella",
        "en": "Toxapex",
        "fr": "Prédastérie"
      },
      749: {
        "de": "Pampuli",
        "en": "Mudbray",
        "fr": "Tiboudet"
      },
      750: {
        "de": "Pampross",
        "en": "Mudsdale",
        "fr": "Bourrinos"
      },
      751: {
        "de": "Araqua",
        "en": "Dewpider",
        "fr": "Araqua"
      },
      752: {
        "de": "Aranestro",
        "en": "Araquanid",
        "fr": "Tarenbulle"
      },
      753: {
        "de": "Imantis",
        "en": "Fomantis",
        "fr": "Mimantis"
      },
      754: {
        "de": "Mantidea",
        "en": "Lurantis",
        "fr": "Floramantis"
      },
      755: {
        "de": "Bubungus",
        "en": "Morelull",
        "fr": "Spododo"
      },
      756: {
        "de": "Lamellux",
        "en": "Shiinotic",
        "fr": "Lampignon"
      },
      757: {
        "de": "Molunk",
        "en": "Salandit",
        "fr": "Tritox"
      },
      758: {
        "de": "Amfira",
        "en": "Salazzle",
        "fr": "Malamandre"
      },
      759: {
        "de": "Velursi",
        "en": "Stufful",
        "fr": "Nounourson"
      },
      760: {
        "de": "Kosturso",
        "en": "Bewear",
        "fr": "Chelours"
      },
      761: {
        "de": "Frubberl",
        "en": "Bounsweet",
        "fr": "Croquine"
      },
      762: {
        "de": "Frubaila",
        "en": "Steenee",
        "fr": "Candine"
      },
      763: {
        "de": "Fruyal",
        "en": "Tsareena",
        "fr": "Sucreine"
      },
      764: {
        "de": "Curelei",
        "en": "Comfey",
        "fr": "Guérilande"
      },
      765: {
        "de": "Kommandutan",
        "en": "Oranguru",
        "fr": "Gouroutan"
      },
      766: {
        "de": "Quartermak",
        "en": "Passimian",
        "fr": "Quartermac"
      },
      767: {
        "de": "Reißlaus",
        "en": "Wimpod",
        "fr": "Sovkipou"
      },
      768: {
        "de": "Tectass",
        "en": "Golisopod",
        "fr": "Sarmuraï"
      },
      769: {
        "de": "Sankabuh",
        "en": "Sandygast",
        "fr": "Bacabouh"
      },
      770: {
        "de": "Colossand",
        "en": "Palossand",
        "fr": "Trépassable"
      },
      771: {
        "de": "Gufa",
        "en": "Pyukumuku",
        "fr": "Concombaffe"
      },
      772: {
        "de": "Typ:Null",
        "en": "Type: Null",
        "fr": "Silvallié"
      },
      773: {
        "de": "Amigento",
        "en": "Silvally",
        "fr": "Silvallié"
      },
      774: {
        "de": "Meteno",
        "en": "Minior",
        "fr": "Météno"
      },
      775: {
        "de": "Koalelu",
        "en": "Komala",
        "fr": "Dodoala"
      },
      776: {
        "de": "Tortunator",
        "en": "Turtonator",
        "fr": "Boumata"
      },
      777: {
        "de": "Togedemaru",
        "en": "Togedemaru",
        "fr": "Togedemaru"
      },
      778: {
        "de": "Mimigma",
        "en": "Mimikyu",
        "fr": "Mimiqui"
      },
      779: {
        "de": "Knirfish",
        "en": "Bruxish",
        "fr": "Denticrisse"
      },
      780: {
        "de": "Sen-Long",
        "en": "Drampa",
        "fr": "Draïeul"
      },
      781: {
        "de": "Moruda",
        "en": "Dhelmise",
        "fr": "Sinistrail"
      },
      782: {
        "de": "Miniras",
        "en": "Jangmo-o",
        "fr": "Bébécaille"
      },
      783: {
        "de": "Mediras",
        "en": "Hakamo-o",
        "fr": "Écaïd"
      },
      784: {
        "de": "Grandiras",
        "en": "Kommo-o",
        "fr": "Ékaïser"
      },
      785: {
        "de": "Kapu-Riki",
        "en": "Tapu Koko",
        "fr": "Tokorico"
      },
      786: {
        "de": "Kapu-Fala",
        "en": "Tapu Lele",
        "fr": "Tokopiyon"
      },
      787: {
        "de": "Kapu-Toro",
        "en": "Tapu Bulu",
        "fr": "Tokotoro"
      },
      788: {
        "de": "Kapu-Kime",
        "en": "Tapu Fini",
        "fr": "Tokopisco"
      },
      789: {
        "de": "Cosmog",
        "en": "Cosmog",
        "fr": "Cosmog"
      },
      790: {
        "de": "Cosmovum",
        "en": "Cosmoem",
        "fr": "Cosmovum"
      },
      791: {
        "de": "Solgaleo",
        "en": "Solgaleo",
        "fr": "Solgaleo"
      },
      792: {
        "de": "Lunala",
        "en": "Lunala",
        "fr": "Lunala"
      },
      793: {
        "de": "Anego",
        "en": "Nihilego",
        "fr": "Zéroïd"
      },
      794: {
        "de": "Masskito",
        "en": "Buzzwole",
        "fr": "Mouscoto"
      },
      795: {
        "de": "Schabelle",
        "en": "Pheromosa",
        "fr": "Cancrelove"
      },
      796: {
        "de": "Voltriant",
        "en": "Xurkitree",
        "fr": "Câblifère"
      },
      797: {
        "de": "Kaguron",
        "en": "Celesteela",
        "fr": "Bamboiselle"
      },
      798: {
        "de": "Katagami",
        "en": "Kartana",
        "fr": "Katagami"
      },
      799: {
        "de": "Schlingking",
        "en": "Guzzlord",
        "fr": "Engloutyran"
      },
      800: {
        "de": "Necrozma",
        "en": "Necrozma",
        "fr": "Necrozma"
      },
      801: {
        "de": "Magearna",
        "en": "Magearna",
        "fr": "Magearna"
      },
      802: {
        "de": "Marshadow",
        "en": "Marshadow",
        "fr": "Marshadow"
      },
      803: {
        "de": "Venicro",
        "en": "Poipole",
        "fr": "Vémini"
      },
      804: {
        "de": "Agoyon",
        "en": "Naganadel",
        "fr": "Mandrillon"
      },
      805: {
        "de": "Muramura",
        "en": "Stakataka",
        "fr": "Ama-Ama"
      },
      806: {
        "de": "Kopplosio",
        "en": "Blacephalon",
        "fr": "Pierroteknik"
      },
      807: {
        "de": "Zeraora",
        "en": "Zeraora",
        "fr": "Zeraora"
      },
      808: {
        "de": "Meltan",
        "en": "Meltan",
        "fr": "Meltan"
      },
      809: {
        "de": "Melmetal",
        "en": "Melmetal",
        "fr": "Melmetal"
      }
    }
    #return switch.get(value,lambda: str(value))###davor den iv wert aus der liste auslesen
    return switch[value][language]

  def getGeschlecht(self,value):
    if value == 1:
      return "\U00002642"
    elif value == 2:
      return "\U00002640"
    else:
      return "\U0000267E"