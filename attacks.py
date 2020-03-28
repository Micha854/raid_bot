
class attacks():

  def getShortAttack(self,value,language):
    switch = {
      200: {
        "de": "Zornklinge",
        "en": "Fury Cutter",
        "fr": "Taillade"
      },
      201: {
        "de": "K\U000000e4ferbiss",
        "en": "Bug Bite",
        "fr": "Piqûre"
      },
      202: {
        "de": "Biss",
        "en": "Bite",
        "fr": "Morsure"
      },
      203: {
        "de": "Tiefschlag",
        "en": "Sucker Punch",
        "fr": "Coup Bas"
      },
      204: {
        "de": "Feuerodem",
        "en": "Dragon Breath",
        "fr": "Dracosouffle"
      },
      205: {
        "de": "Donnerschock",
        "en": "Thunder Shock Punch",
        "fr": "Éclair"
      },
      206: {
        "de": "Funkensprung",
        "en": "Spark",
        "fr": "Étincelle"
      },
      207: {
        "de": "Fu\U000000DFkick",
        "en": "Low Kick",
        "fr": "Balayage"
      },
      208: {
        "de": "Karateschlag",
        "en": "Karate Chop",
        "fr": "Poing-Karaté"
      },
      209: {
        "de": "Glut",
        "en": "Ember",
        "fr": "Flammèche"
      },
      210: {
        "de": "Fl\U000000fcgelschlag",
        "en": "Wing Attack",
        "fr": "Cru-Aile"
      },
      211: {
        "de": "Schnabel",
        "en": "Peck",
        "fr": "Picpic"
      },
      212: {
        "de": "Schlecker",
        "en": "Lick",
        "fr": "Léchouille"
      },
      213: {
        "de": "Dunkelklaue",
        "en": "Shadow Claw",
        "fr": "Griffe Ombre"
      },
      214: {
        "de": "Rankenhieb",
        "en": "Vine Whip",
        "fr": "Fouet Lianes"
      },
      215: {
        "de": "Rasierblatt",
        "en": "Razor Leaf",
        "fr": ""
      },
      216: {
        "de": "Lehmschuss",
        "en": "Mud Shot",
        "fr": "Tranch'Herbe"
      },
      217: {
        "de": "Eissplitter",
        "en": "Ice Shard",
        "fr": "Éclats Glace"
      },
      218: {
        "de": "Eisesodem",
        "en": "Frost Breath",
        "fr": "Souffle Glacé"
      },
      219: {
        "de": "Ruckzuckhieb",
        "en": "Quick Attack",
        "fr": "Vive-Attaque"
      },
      220: {
        "de": "Kratzer",
        "en": "Scratch",
        "fr": "Griffe"
      },
      221: {
        "de": "Tackle",
        "en": "Tackle",
        "fr": "Charge"
      },
      222: {
        "de": "Pfund",
        "en": "Pound",
        "fr": "Écras'Face"
      },
      223: {
        "de": "Zerschneider",
        "en": "Cut",
        "fr": "Coupe"
      },
      224: {
        "de": "Gifthieb",
        "en": "Poison Jab",
        "fr": "Direct Toxik"
      },
      225: {
        "de": "S\U000000e4ure",
        "en": "Acid",
        "fr": "Acide"
      },
      226: {
        "de": "Psychoklinge",
        "en": "Psycho Cut",
        "fr": "Coupe Psycho"
      },
      227: {
        "de": "Steinwurf",
        "en": "Rock Throw",
        "fr": "Jet-Pierres"
      },
      228: {
        "de": "Metallklaue",
        "en": "Metal Claw",
        "fr": "Griffe Acier"
      },
      229: {
        "de": "Patronenhieb",
        "en": "Bullet Punch",
        "fr": "Pisto-Poing"
      },
      230: {
        "de": "Aquaknarre",
        "en": "Water Gun",
        "fr": "Pistolet à O"
      },
      231: {
        "de": "Platscher",
        "en": "Splash",
        "fr": "Trempette"
      },
      232: {
        "de": "Aquaknarre",
        "en": "Water Gun",
        "fr": "Pistolet à O"
      },
      233: {
        "de": "Lehmschelle",
        "en": "Mud-Slap",
        "fr": "Coud'Boue"
      },
      234: {
        "de": "Zen-Kopfsto\U000000DF",
        "en": "Zen Headbutt",
        "fr": "Psykoud'Boul"
      },
      235: {
        "de": "Konfusion",
        "en": "Confusion",
        "fr": "Choc Mental"
      },
      236: {
        "de": "Giftstachel",
        "en": "Poison Sting",
        "fr": "Dard-Venin"
      },
      237: {
        "de": "Blubber",
        "en": "Bubble",
        "fr": "Écume"
      },
      238: {
        "de": "Finte",
        "en": "Feint Attack",
        "fr": "Feinte"
      },
      239: {
        "de": "Stahlfl\U000000fcgel",
        "en": "Steel Wing",
        "fr": "Aile d’Acier"
      },
      240: {
        "de": "Feuerzahn",
        "en": "Fire Fang",
        "fr": "Crocs Feu"
      },
      241: {
        "de": "Zertr\U000000fcmmerer",
        "en": "Rock Smash",
        "fr": "Éclate-Roc"
      },
      242: {
        "de": "Wandler",
        "en": "Transform",
        "fr": "Morphing"
      },
      243: {
        "de": "Kontor",
        "en": "Counter",
        "fr": "Riposte"
      },
      244: {
        "de": "Pulverschnee",
        "en": "Powder Snow",
        "fr": "Poudreuse"
      },
      249: {
        "de": "Ladestrahl",
        "en": "Charge Beam",
        "fr": "Rayon Chargé"
      },
      250: {
        "de": "Voltwechsel",
        "en": "Volt Switch",
        "fr": "Change Éclair"
      },
      253: {
        "de": "Drachenrute",
        "en": "Dragon Tail",
        "fr": "Draco-Queue"
      },
      255: {
        "de": "Luftschnitt",
        "en": "Air Slash",
        "fr": "Lame d'Air"
      },
      260: {
        "de": "Plage",
        "en": "Infestation",
        "fr": "Harcèlement"
      },
      261: {
        "de": "K\U000000e4fertrutz",
        "en": "Struggle Bug",
        "fr": "Survinsecte"
      },
      263: {
        "de": "Erstauner",
        "en": "Astonish",
        "fr": "Étonnement"
      },
      264: {
        "de": "B\U000000fcrde",
        "en": "Hex",
        "fr": "Châtiment"
      },
      266: {
        "de": "Eisenschweif",
        "en": "Iron Tail",
        "fr": "Queue de Fer"
      },
      269: {
        "de": "Feuerwirbel",
        "en": "Fire Spin",
        "fr": "Danse Flamme"
      },
      271: {
        "de": "Kugelsaat",
        "en": "Bullet Seed",
        "fr": "Balle Graine"
      },
      274: {
        "de": "Sondersensor",
        "en": "Extrasensory",
        "fr": "Extrasenseur"
      },
      278: {
        "de": "Standpauke",
        "en": "Snarl",
        "fr": "Aboiement"
      },
      281: {
        "de": "Kraftreserve",
        "en": "Hidden Power",
        "fr": "Puissance Cachée"
      },
      282: {
        "de": "Bodycheck",
        "en": "Take Down",
        "fr": "Bélier"
      },
      283: {
        "de": "Kaskade",
        "en": "Waterfall",
        "fr": "Cascade"
      },
      287: {
        "de": "G\U000000e4hner",
        "en": "Yawn",
        "fr": "Bâillement"
      },
      291: {
        "de": "Geschenk",
        "en": "Present",
        "fr": "Cadeau"
      },
      297: {
        "de": "Katapult",
        "en": "Smack Down",
        "fr": "Anti-Air"
      },
      320: {
        "de": "Charme",
        "en": "Charm",
        "fr": "Charme"
      },
      325: {
        "de": "Zielschuss",
        "en": "Lock-On",
        "fr": "Verrouillage"
      },
      326: {
        "de": "Donnerzahn",
        "en": "Thunder Fang",
        "fr": "Crocs Éclair"
      },
      327: {
        "de": "Eiszahn",
        "en": "Ice Fang",
        "fr": "Crocs Givre"
      }
    }
    #return switch.get(value,lambda: str(value))
    return switch[value][language]

  def getLoadAttack(self,value,language):
    switch = {
      13: {
        "de": "Wickel",
        "en": "Wrap",
        "fr": "Ligotage"
      },
      14: {
        "de": "Hyperstrahl",
        "en": "Hyper Beam",
        "fr": "Ultralase"
      },
      16: {
        "de": "Finsteraura",
        "en": "Dark Pulse",
        "fr": "Vibrobscur"
      },
      18: {
        "de": "Schlammbad",
        "en": "Sludge",
        "fr": "Détritus"
      },
      20: {
        "de": "Klammer",
        "en": "Vice Grip",
        "fr": "Force Poigne"
      },
      21: {
        "de": "Flammenrad",
        "en": "Flame Wheel",
        "fr": "Roue de Feu"
      },
      22: {
        "de": "Vielender",
        "en": "Megahorn",
        "fr": "Mégacorne"
      },
      24: {
        "de": "Flammenwurf",
        "en": "Flamethrower",
        "fr": "Lance-Flammes"
      },
      26: {
        "de": "Schaufler",
        "en": "Dig",
        "fr": "Tunnel"
      },
      28: {
        "de": "Kreuzhieb",
        "en": "Cross Chop",
        "fr": "Coup-Croix"
      },
      30: {
        "de": "Psystrahl",
        "en": "Psybeam",
        "fr": "Rafale Psy"
      },
      31: {
        "de": "Erdbeben",
        "en": "Earthquake",
        "fr": "Séisme"
      },
      32: {
        "de": "Steinkante",
        "en": "Stone Edge",
        "fr": "Lame de Roc"
      },
      33: {
        "de": "Eishieb",
        "en": "Ice Punch",
        "fr": "Poing-Glace"
      },
      34: {
        "de": "Herzstempel",
        "en": "Heart Stamp",
        "fr": "Crèvecœur"
      },
      35: {
        "de": "Ladungssto\U000000DF",
        "en": "Discharge",
        "fr": "Coup d'Jus"
      },
      36: {
        "de": "Lichtkanone",
        "en": "Flash Cannon",
        "fr": "Luminocanon"
      },
      38: {
        "de": "Bohrschnabel",
        "en": "Drill Peck",
        "fr": "Bec Vrille"
      },
      39: {
        "de": "Eisstrahl",
        "en": "Ice Beam",
        "fr": "Laser Glace"
      },
      40: {
        "de": "Blizzard",
        "en": "Blizzard",
        "fr": "Blizzard"
      },
      42: {
        "de": "Hitzewelle",
        "en": "Heat Wave",
        "fr": "Canicule"
      },
      45: {
        "de": "Aero-Ass",
        "en": "Aerial Ace",
        "fr": "Aéropique"
      },
      46: {
        "de": "Schlagbohrer",
        "en": "Drill Run",
        "fr": "Tunnelier"
      },
      47: {
        "de": "Bl\U000000fctenwirbel",
        "en": "Petal Blizzard",
        "fr": "Tempête Florale"
      },
      48: {
        "de": "Megasauger",
        "en": "Mega Drain",
        "fr": "Méga-Sangsue"
      },
      49: {
        "de": "K\U000000e4fergebrumm",
        "en": "Bug Buzz",
        "fr": "Bourdon"
      },
      50: {
        "de": "Giftzahn",
        "en": "Poison Fang",
        "fr": "Crochet Venin"
      },
      51: {
        "de": "Nachthieb",
        "en": "Night Slash",
        "fr": "Tranche-Nuit"
      },
      53: {
        "de": "Blubbstrahl",
        "en": "Bubble Beam",
        "fr": "Bulles d’O"
      },
      54: {
        "de": "\U000000DCberroller",
        "en": "Submission",
        "fr": "Sacrifice"
      },
      56: {
        "de": "Fu\U000000DFtritt",
        "en": "Low Sweep",
        "fr": "Balayette"
      },
      57: {
        "de": "Wasserd\U000000fcse",
        "en": "Aqua Jet",
        "fr": "Aqua-Jet"
      },
      58: {
        "de": "Nassschweif",
        "en": "Aqua Tail",
        "fr": "Hydroqueue"
      },
      59: {
        "de": "Samenbomben",
        "en": "Seed Bomb",
        "fr": "Canon Graine"
      },
      60: {
        "de": "Psychoschock",
        "en": "Psyshock",
        "fr": "Choc Psy"
      },
      62: {
        "de": "Antik-Kraft",
        "en": "Ancient Power",
        "fr": "Pouvoir Antique"
      },
      63: {
        "de": "Felsgrab",
        "en": "Rock Tomb",
        "fr": "Tomberoche"
      },
      64: {
        "de": "Steinhagel",
        "en": "Rock Slide",
        "fr": "Éboulement"
      },
      65: {
        "de": "Juwelenkraft",
        "en": "Power Gem",
        "fr": "Rayon Gemme"
      },
      66: {
        "de": "Schattensto\U000000DF",
        "en": "Shadow Sneak",
        "fr": "Ombre Portée"
      },
      67: {
        "de": "Finsterfaust",
        "en": "Shadow Punch",
        "fr": "Poing Ombre"
      },
      69: {
        "de": "Unheilb\U000000F6en",
        "en": "Ominous Wind",
        "fr": "Vent Mauvais"
      },
      70: {
        "de": "Spukball",
        "en": "Shadow Ball",
        "fr": "Ball'Ombre"
      },
      72: {
        "de": "Magnetbombe",
        "en": "Magnet Bomb",
        "fr": "Bombaimant"
      },
      74: {
        "de": "Eisensch\U000000e4del",
        "en": "Iron Head",
        "fr": "Tête de Fer"
      },
      75: {
        "de": "Parabolladung",
        "en": "Parabolic Charge",
        "fr": "Parabocharge"
      },
      77: {
        "de": "Donnerschlag",
        "en": "Thunder Punch",
        "fr": "Poing-Éclair"
      },
      78: {
        "de": "Donner",
        "en": "Thunder",
        "fr": "Fatal-Foudre"
      },
      79: {
        "de": "Donnerblitz",
        "en": "Thunderbolt",
        "fr": "Tonnerre"
      },
      80: {
        "de": "Windhose",
        "en": "Twister",
        "fr": "Ouragan"
      },
      82: {
        "de": "Drachenpuls",
        "en": "Dragon Pulse",
        "fr": "Dracochoc"
      },
      83: {
        "de": "Drachenklaue",
        "en": "Dragon Claw",
        "fr": "Dracogriffe"
      },
      84: {
        "de": "S\U000000e4uselstimme",
        "en": "Disarming Voice",
        "fr": "Voix Enjôleuse"
      },
      85: {
        "de": "Diebeskuss",
        "en": "Draining Kiss",
        "fr": "Vampibaiser"
      },
      86: {
        "de": "Zauberschein",
        "en": "Dazzling Gleam",
        "fr": "Éclat Magique"
      },
      87: {
        "de": "Mondgewalt",
        "en": "Moonblast",
        "fr": "Pouvoir Lunaire"
      },
      88: {
        "de": "Knuddler",
        "en": "Play Rough",
        "fr": "Câlinerie"
      },
      89: {
        "de": "Giftstreich",
        "en": "Cross Poison",
        "fr": "Poison-Croix"
      },
      90: {
        "de": "Matschbombe",
        "en": "Sludge Bomb",
        "fr": "Bomb-Beurk"
      },
      91: {
        "de": "Schlammwoge",
        "en": "Sludge Wave",
        "fr": "Cradovague"
      },
      92: {
        "de": "M\U000000fclltreffer",
        "en": "Gunk Shot",
        "fr": "Détricanon"
      },
      94: {
        "de": "Knochenkeule",
        "en": "Bone Club",
        "fr": "Massd'Os"
      },
      95: {
        "de": "Dampfwalze",
        "en": "Bulldoze",
        "fr": "Piétisol"
      },
      96: {
        "de": "Schlammbombe",
        "en": "Mud Bomb",
        "fr": "Boue-Bombe"
      },
      99: {
        "de": "Ampelleuchte",
        "en": "Signal Beam",
        "fr": "Rayon Signal"
      },
      100: {
        "de": "Kreuzschere",
        "en": "X-Scissor",
        "fr": "Plaie-Croix"
      },
      101: {
        "de": "Nitroladung",
        "en": "Flame Charge",
        "fr": "Nitrocharge"
      },
      102: {
        "de": "Funkenflug",
        "en": "Flame Burst",
        "fr": "Rebondifeu"
      },
      103: {
        "de": "Feuersturm",
        "en": "Fire Blast",
        "fr": "Déflagration"
      },
      104: {
        "de": "Lake",
        "en": "Brine",
        "fr": "Saumure"
      },
      105: {
        "de": "Aquawelle",
        "en": "Water Pulse",
        "fr": "Vibraqua"
      },
      106: {
        "de": "Siedewasser",
        "en": "Scald",
        "fr": "Ébullition"
      },
      107: {
        "de": "Hydropumpe",
        "en": "Hydro Pump",
        "fr": "Hydrocanon"
      },
      108: {
        "de": "Psychokinese",
        "en": "Psychic",
        "fr": "Psyko"
      },
      109: {
        "de": "Psychosto\U000000DF",
        "en": "Psystrike",
        "fr": "Frappe Psy"
      },
      111: {
        "de": "Eissturm",
        "en": "Icy Wind",
        "fr": "Vent Glace"
      },
      114: {
        "de": "Gigasauger",
        "en": "Giga Drain",
        "fr": "Giga-Sangsue"
      },
      115: {
        "de": "Feuerschlag",
        "en": "Fire Punch",
        "fr": "Poing de Feu"
      },
      116: {
        "de": "Solarstrahl",
        "en": "Solar Beam",
        "fr": "Lance-Soleil"
      },
      117: {
        "de": "Laubklinge",
        "en": "Leaf Blade",
        "fr": "Lame-Feuille"
      },
      118: {
        "de": "Blattgei\U000000DFel",
        "en": "Power Whip",
        "fr": "Mégafouet"
      },
      121: {
        "de": "WindschnittF",
        "en": "Air Cutter",
        "fr": "Tranch'Air"
      },
      122: {
        "de": "Orkan",
        "en": "Hurricane",
        "fr": "Vent Violent"
      },
      123: {
        "de": "Durchbruch",
        "en": "Brick Break",
        "fr": "Casse-Brique"
      },
      125: {
        "de": "Sternschauer",
        "en": "Swift",
        "fr": "Météores"
      },
      126: {
        "de": "Hornattacke",
        "en": "Horn Attack",
        "fr": "Koud'Korne"
      },
      127: {
        "de": "Stampfer",
        "en": "Stomp",
        "fr": "Écrasement"
      },
      129: {
        "de": "Hyperzahn",
        "en": "Hyper Fang",
        "fr": "Croc de Mort"
      },
      131: {
        "de": "Bodyslam",
        "en": "Body Slam",
        "fr": "Plaquage"
      },
      132: {
        "de": "Erholung",
        "en": "Rest",
        "fr": "Repos"
      },
      133: {
        "de": "Verzweifler",
        "en": "Struggle",
        "fr": "Lutte"
      },
      134: {
        "de": "Siedewasser",
        "en": "Scald (Blastoise)",
        "fr": "Ébullition"
      },
      135: {
        "de": "Hydropumpe",
        "en": "Hydro Pump (Blastoise)",
        "fr": "Hydrocanon"
      },
      136: {
        "de": "Wickel",
        "en": "Wrap (Green)",
        "fr": "Ligotage"
      },
      137: {
        "de": "Wickel",
        "en": "Wrap (Pink)",
        "fr": "Ligotage"
      },
      245: {
        "de": "Nahkampf",
        "en": "Close Combat",
        "fr": "Close Combat"
      },
      246: {
        "de": "Wuchtschlag",
        "en": "Dynamic Punch",
        "fr": "Dynamopoing"
      },
      247: {
        "de": "Fokussto\U000000DF",
        "en": "Focus Blast",
        "fr": "Exploforce"
      },
      248: {
        "de": "Aurorastrahl",
        "en": "Aurora Beam",
        "fr": "Onde Boréale"
      },
      251: {
        "de": "Stromsto\U000000DF",
        "en": "Wild Charge",
        "fr": "Éclair Fou"
      },
      252: {
        "de": "Blitzkanone",
        "en": "Zap Cannon",
        "fr": "Élecanon"
      },
      254: {
        "de": "Lawine",
        "en": "Avalanche",
        "fr": "Avalanche"
      },
      256: {
        "de": "Sturzflug",
        "en": "Brave Bird",
        "fr": "Rapace"
      },
      257: {
        "de": "Himmelsfeger",
        "en": "Sky Attack",
        "fr": "Piqué"
      },
      258: {
        "de": "Sandgrab",
        "en": "Sand Tomb",
        "fr": "Tourbi-Sable"
      },
      259: {
        "de": "Felswurf",
        "en": "Rock Blast",
        "fr": "Boule Roc"
      },
      262: {
        "de": "Silberhauch",
        "en": "Silver Wind",
        "fr": "Vent Argenté"
      },
      265: {
        "de": "Nachtnebel",
        "en": "Night Shade",
        "fr": "Ombre Nocturne"
      },
      267: {
        "de": "Gyroball",
        "en": "Gyro Ball",
        "fr": "Gyroballe"
      },
      268: {
        "de": "Rammboss",
        "en": "Heavy Slam",
        "fr": "Tacle Lourd"
      },
      270: {
        "de": "Hitzekoller",
        "en": "Overheat",
        "fr": "Surchauffe"
      },
      272: {
        "de": "Strauchler",
        "en": "Grass Knot",
        "fr": "Nœud Herbe"
      },
      273: {
        "de": "Energieball",
        "en": "Energy Ball",
        "fr": "Éco-Sphère"
      },
      275: {
        "de": "Seher",
        "en": "Future Sight",
        "fr": "Prescience"
      },
      276: {
        "de": "Spiegelcape",
        "en": "Mirror Coat",
        "fr": "Voile Miroir"
      },
      277: {
        "de": "Wutanfall",
        "en": "Outrage",
        "fr": "Colère"
      },
      279: {
        "de": "Knirscher",
        "en": "Crunch",
        "fr": "Mâchouille"
      },
      280: {
        "de": "Schmarotzer",
        "en": "Foul Play",
        "fr": "Tricherie"
      },
      284: {
        "de": "Surfer",
        "en": "Surf",
        "fr": "Surf"
      },
      285: {
        "de": "Draco Meteor",
        "en": "Draco Meteor",
        "fr": "Draco Météore"
      },
      286: {
        "de": "Kismetwunsch",
        "en": "Doom Desire",
        "fr": "Carnareket"
      },
      288: {
        "de": "Psyschub",
        "en": "Psycho Boost",
        "fr": "Psycho Boost"
      },
      289: {
        "de": "Ursprungswoge",
        "en": "Origin Pulse",
        "fr": "Onde Originelle"
      },
      290: {
        "de": "Abgrundsklinge",
        "en": "Precipice Blades",
        "fr": "Lame Pangéenne"
      },
      292: {
        "de": "Meteorologe",
        "en": "Weather Ball (Fire)",
        "fr": "Ball'Météo"
      },
      293: {
        "de": "Meteorologe",
        "en": "Weather Ball (Ice)",
        "fr": "Ball'Météo"
      },
      294: {
        "de": "Meteorologe",
        "en": "Weather Ball",
        "fr": "Ball'Météo"
      },
      295: {
        "de": "Meteorologe",
        "en": "Weather Ball (Water)",
        "fr": "Ball'Météo"
      },
      296: {
        "de": "Flora-Statue",
        "en": "Frenzy Plant",
        "fr": "Végé-Attak"
      },
      298: {
        "de": "Lohekanonade",
        "en": "Blast Burn",
        "fr": "Rafale Feu"
      },
      299: {
        "de": "Aquahaubitze",
        "en": "Hydro Cannon",
        "fr": "Hydroblast"
      },
      300: {
        "de": "Zuflucht",
        "en": "Last Resort",
        "fr": "Dernier Recours"
      },
      301: {
        "de": "Sternenhieb",
        "en": "Meteor Mash",
        "fr": "Poing Météore"
      },
      302: {
        "de": "Sch\U000000e4delwumme",
        "en": "Skull Bash",
        "fr": "Coud'Krâne"
      },
      303: {
        "de": "S\U000000e4urespeier",
        "en": "Acid Spray",
        "fr": "Bombe Acide"
      },
      304: {
        "de": "Erdkr\U000000e4fte",
        "en": "Earth Power",
        "fr": "Telluriforce"
      },
      305: {
        "de": "Krabbhammer",
        "en": "Crabhammer",
        "fr": "Pince-Masse"
      },
      306: {
        "de": "Anfallen",
        "en": "Lunge",
        "fr": "Furie-Bond"
      },
      307: {
        "de": "Zermalmklaue",
        "en": "Crush Claw",
        "fr": "Éclate Griffe"
      },
      308: {
        "de": "Octazooka",
        "en": "Octazooka",
        "fr": "Octazooka"
      },
      309: {
        "de": "Spiegelsalve",
        "en": "Mirror Shot",
        "fr": "Miroi-Tir"
      },
      310: {
        "de": "Kraftkoloss",
        "en": "Superpower",
        "fr": "Surpuissance"
      },
      311: {
        "de": "Stachelfinale",
        "en": "Fell Stinger",
        "fr": "Dard Mortel"
      },
      312: {
        "de": "Grasmixer",
        "en": "Leaf Tornado",
        "fr": "Phytomixeur"
      },
      313: {
        "de": "Blutsauger",
        "en": "Leech Life",
        "fr": "Vampirisme"
      },
      314: {
        "de": "Ableithieb",
        "en": "Drain Punch",
        "fr": "Vampipoing"
      },
      315: {
        "de": "Schattenknochen",
        "en": "Shadow Bone",
        "fr": "Os'Ombre"
      },
      316: {
        "de": "Lehmbr\U000000fche",
        "en": "Muddy Water",
        "fr": "Ocroupi"
      },
      317: {
        "de": "Feuerfeger",
        "en": "Blaze Kick",
        "fr": "Pied Brûleur"
      },
      318: {
        "de": "Kalkklinge",
        "en": "Razor Shell",
        "fr": "Coquilame"
      },
      319: {
        "de": "Steigerungshieb",
        "en": "Power-Up Punch",
        "fr": "Poing Boost"
      },
      321: {
        "de": "Gigasto\U000000DF",
        "en": "Giga Impact",
        "fr": "Giga Impact"
      },
      322: {
        "de": "Frustration",
        "en": "Frustration",
        "fr": "Frustration"
      },
      323: {
        "de": "R\U000000fcckkehr",
        "en": "Return",
        "fr": "Retour"
      },
      324: {
        "de": "Synchrol\U000000e4rm",
        "en": "Synchronoise",
        "fr": "Synchropeine"
      },
      328: {
        "de": "Hornbohrer",
        "en": "Horn Drill",
        "fr": "Empal'Korne"
      },
      329: {
        "de": "Geofissur",
        "en": "Fissure",
        "fr": "Abîme"
      }
    }
    #return switch.get(value,lambda: str(value))
    return switch[value][language]

#https://bulbapedia.bulbagarden.net/wiki/List_of_moves_in_Pok%C3%A9mon_GO