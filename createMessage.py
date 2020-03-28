import attacks
import pokemon
import time
import datetime
import helper

class createMessage():

  def create(self,Sql,send,sleep,cfg):
    attacke = attacks.attacks()
    pokeID = pokemon.pokemon()
    Help = helper.Helper()
    overview = ""
    team = ""
    ex_raid = ""
    lvl_icon = ""
    raid_level = cfg.level
    l5 = ""
    l4 = ""
    l3 = ""
    l2 = ""
    l1 = ""

    i = 0 # all found raids
    x = 0 # raids that will be send
    id = 0

    print("####################==========\\ " + str(datetime.datetime.now()) + " /==========####################")

    try:
      for encounter in Sql.gym_id:
        name = "Unknown Area" if Sql.name[i] is None else Sql.name[i]
        level = Sql.level[i]
        zeit_start = Sql.start[i]
        zeit_end = Sql.end[i]

        zeit_start = zeit_start + datetime.timedelta(hours=1)
        zeit_end = zeit_end + datetime.timedelta(hours=1)

        ex_raid = " \u274C " if Sql.ex_raid[i] == 1 else " "

        if Sql.team_id[i] == 2:
          team = "\u2764"         # red
        elif Sql.team_id[i] == 3:
          team = "\U0001F49B"     # yellow
        elif Sql.team_id[i] == 1:
          team = "\U0001F499"     # blue
        else:
          team = "\U0001F90D"     # none

        if level == 5:
          lvl_icon = "\u0035\uFE0F\u20E3"
        elif level == 4:
          lvl_icon = "\u0034\uFE0F\u20E3"
        elif level == 3:
          lvl_icon = "\u0033\uFE0F\u20E3"
        elif level == 2:
          lvl_icon = "\u0032\uFE0F\u20E3"
        elif level == 1:
          lvl_icon = "\u0031\uFE0F\u20E3"

        if Sql.pokemon_id[i] is None:
          kurzattacke = ""
          ladeattacke = ""
          move = ""
          moveV= ""
          raid = self.getText("egg",cfg.language) + " \U0001F95A "
        else:
          kurzattacke = "\n├ " + attacke.getShortAttack(Sql.move_1[i],cfg.language)
          ladeattacke = attacke.getLoadAttack(Sql.move_2[i],cfg.language)
          move = kurzattacke + "/" + ladeattacke
          moveV= "\u2694 " + attacke.getShortAttack(Sql.move_1[i],cfg.language) + "/" + attacke.getLoadAttack(Sql.move_2[i],cfg.language)
          raid = pokeID.getPokemon(Sql.pokemon_id[i],cfg.language) + " " + pokeID.getGeschlecht(Sql.gender[i]) + " "

        if Sql.level[i] in (raid_level):
          with open(cfg.areaName+"eggs.txt") as input:
            data = input.read()
            data = data.replace("[", "").replace("'", "").replace("]", "")
            data = data.split(', ')

          bolt_line = str(lvl_icon) + " " + str(raid) + str(zeit_start.hour) + ":" + str(Help.nice_time(str(zeit_start.minute))) + " - " + str(zeit_end.hour) + ":" + str(Help.nice_time(str(zeit_end.minute)))
          normal_line = str(team) + " " + str(name) + ex_raid + moveV

          if send.list_output.__contains__(encounter):
            f = open(cfg.areaName+"output.txt", "r")
              # Split the string based on space delimiter 
            list_string = f.read()
            list_string = list_string[1:len(list_string)-1]
            f.close()
            list_string = list_string.split(', ') 
            id = list_string[send.list_output.index(encounter)]

            pos = list_string.index(id)
            egg = data[pos]
            send.eggs.__contains__(encounter)
            
            print("\n" + str(name) + " (ID: " + str(id) + ", index: " + str(pos) + ")")
            print("egg: " + str(egg))

            if egg == encounter and not Sql.pokemon_id[i] == None:
              send.changeBossEgg(bolt_line,normal_line,encounter,Sql.latitude[i],Sql.longitude[i],id,pos)

          else:
            id = send.send(bolt_line,normal_line,encounter,Sql.latitude[i],Sql.longitude[i],Sql.pokemon_id[i])
            print("===> found [" + str(i) + "] level " + str(level) + " " + str(raid))
          x +=1
          
          header = "\n<b>## Level " + str(lvl_icon) + " Raids</b> \U0001F44A\n"
          
          if not l5 and level == 5:
            l5 = header
            overview = overview + l5
          if not l4 and level == 4:
            l4 = header
            overview = overview + l4
          if not l3 and level == 3:
            l3 = header
            overview = overview + l3
          if not l2 and level == 2:
            l2 = header
            overview = overview + l2
          if not l1 and level == 1:
            l1 = header
            overview = overview + l1
          
          overview += "<b>" + str(team) + str(raid) + str(zeit_start.hour) + ":" + str(Help.nice_time(str(zeit_start.minute))) + " - " + str(zeit_end.hour) + ":" + str(Help.nice_time(str(zeit_end.minute))) + "</b>" + str(move) + "\n└ <a href='" + cfg.ivchatUrl + "/" + str(id) + "'>" + str(name) + "</a>" + str(ex_raid) + "\n"
        i +=1
      send.sendOverview(overview,self.getText("noRaids",cfg.language))
      print("\nAktuell " + str(x) + " Raids (" + str(i) + ")\n")

      # DEBUG:
      #f = open("TEST.txt", "a")
      #f.writelines("\n\n####################==========\\ " + str(datetime.datetime.now()) + " /==========####################")
      #f.writelines("len ==> " + str(len(overview)) + "\n")
      #f.writelines(str(overview))
      #f.close()
      
    except Exception as e:
        outF = open(Sql.areaName+"error.txt","w")
        ausgabe = "Passierte in der CreateMessage.py\n"
        ausgabe += "gym_id: " + str(Sql.gym_id.__len__) + "\n"
        ausgabe += "team_id: " + str(Sql.team_id.__len__) + "\n"
        ausgabe += "name: " + str(Sql.name.__len__) + "\n"
        ausgabe += "latitude: " + str(Sql.latitude.__len__) + "\n"
        ausgabe += "longitude: " + str(Sql.longitude.__len__) + "\n"
        ausgabe += "level: " + str(Sql.level.__len__) + "\n"
        ausgabe += "start: " + str(Sql.start.__len__) + "\n"
        ausgabe += "end: " + str(Sql.end.__len__) + "\n"
        ausgabe += "pokemon_id: " + str(Sql.pokemon_id.__len__) + "\n"
        ausgabe += "move_1: " + str(Sql.move_1.__len__) + "\n"
        ausgabe += "move_2: " + str(Sql.move_2.__len__) + "\n"
        ausgabe += "gender: " + str(Sql.gender.__len__) + "\n"
        ausgabe += "ex_raid: " + str(Sql.ex_raid.__len__) + "\n"
        ausgabe += "Wert i" + str(i) + "\n"
        outF.writelines(ausgabe + str(e))
        outF.close()

  def getText(self,value,language):
    text = {
      "noRaids": {
        "de": "Aktuell keine Raids vorhanden",
        "en": "no raids currently available",
        "fr": "pas de raids disponibles"
      },
      "egg": {
        "de": "Ei",
        "en": "egg",
        "fr": "oeuf"
      }
    }
    return text[value][language]