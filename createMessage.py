import importer
import json
import time
import datetime
import helper


class createMessage():

    def create(self, Sql, send, sleep, cfg, gmt):

        ### can be configured custom ###

        limit = 40                # Raid Limit

################################

        Help = helper.Helper()
        overview = ""
        team = ""
        ex_raid = ""
        lvl_icon = ""
        clock = cfg.clockformat
        raid_level = cfg.level
        l10 = ""
        l9 = ""
        l8 = ""
        l7 = ""
        l6 = ""
        l5 = ""
        l4 = ""
        l3 = ""
        l2 = ""
        l1 = ""

        i = 0  # all found raids
        x = 0  # raids that will be send
        x_old = 0  # old raids
        id = 0

        now = datetime.datetime.now()
        print("\n\n####################==========\\ *** Raid *** Update " + cfg.areaName +
              cfg.areaNumber + " " + now.strftime("%m/%d/%Y, %H:%M:%S") + " /==========####################\n")

        try:
            for encounter in Sql.gym_id:
                name = "Unknown Area" if Sql.name[i] is None else Sql.name[i]
                level = Sql.level[i]
                zeit_start = Sql.start[i]
                zeit_end = Sql.end[i]

                zeit_start = zeit_start + datetime.timedelta(hours=gmt)
                zeit_end = zeit_end + datetime.timedelta(hours=gmt)

                if clock == 12:
                    t_start = time.strptime(
                        str(zeit_start.hour)+":"+Help.nice_time(str(zeit_start.minute)), "%H:%M")
                    t_end = time.strptime(
                        str(zeit_end.hour)+":"+Help.nice_time(str(zeit_end.minute)), "%H:%M")
                    raid_start = time.strftime("%I:%M %p", t_start)
                    raid_end = time.strftime("%I:%M %p", t_end)
                else:
                    raid_start = str(zeit_start.hour) + ":" + \
                        str(Help.nice_time(str(zeit_start.minute)))
                    raid_end = str(zeit_end.hour) + ":" + \
                        str(Help.nice_time(str(zeit_end.minute)))

                ex_raid = " \u274C " if Sql.ex_raid[i] == 1 else " "

                # set team ICONS
                if Sql.team_id[i] == 2:
                    team = "\u2764"         # red
                elif Sql.team_id[i] == 3:
                    team = "\U0001F49B"     # yellow
                elif Sql.team_id[i] == 1:
                    team = "\U0001F499"     # blue
                else:
                    team = "\U0001F90D"     # none

                # set raid level ICONS
                if level == 10:
                    lvl_icon = "\U0001F51F"
                    mega = "Proto "
                elif level == 9:
                    lvl_icon = "\u0039\uFE0F\u20E3"
                    mega = " "
                elif level == 8:
                    lvl_icon = "\u0038\uFE0F\u20E3"
                    mega = " "
                elif level == 7:
                    lvl_icon = "\u0037\uFE0F\u20E3"
                    mega = "Mega "
                elif level == 6:
                    lvl_icon = "\u0036\uFE0F\u20E3"
                    mega = "Mega " if Sql.evolution[i] > 0 else " "
                elif level == 5:
                    lvl_icon = "\u0035\uFE0F\u20E3"
                    mega = " "
                elif level == 4:
                    lvl_icon = "\u0034\uFE0F\u20E3"
                    mega = " "
                elif level == 3:
                    lvl_icon = "\u0033\uFE0F\u20E3"
                    mega = " "
                elif level == 2:
                    lvl_icon = "\u0032\uFE0F\u20E3"
                    mega = " "
                elif level == 1:
                    lvl_icon = "\u0031\uFE0F\u20E3"
                    mega = " "

                # set pokemon form name
                if self.getForm(Sql.form[i], cfg.language):
                    getform = "(" + \
                        self.getForm(Sql.form[i], cfg.language) + ")"
                else:
                    getform = ""

                # set pokemon costume name
                if self.getCostume(Sql.costume[i], cfg.language):
                    getcostume = "(" + \
                        self.getCostume(Sql.costume[i], cfg.language) + ")"
                else:
                    getcostume = ""

                # get mega evolution
                if Sql.evolution[i] == 3:
                    evolution = " Y"
                elif Sql.evolution[i] == 2:
                    evolution = " X"
                else:
                    evolution = ""

                if Sql.pokemon_id[i] is None:
                    kurzattacke = ""
                    ladeattacke = ""
                    move = ""
                    moveV = ""
                    raid = self.getText("egg", cfg.language) + " \U0001F95A "
                else:
                    kurzattacke = "\n├ " + \
                        self.getShortAttack(Sql.move_1[i], cfg.language)
                    ladeattacke = self.getLoadAttack(
                        Sql.move_2[i], cfg.language)
                    move = kurzattacke + "/" + ladeattacke
                    moveV = "\u2694 " + self.getShortAttack(
                        Sql.move_1[i], cfg.language) + "/" + self.getLoadAttack(Sql.move_2[i], cfg.language)
                    raid = str(mega) + self.getPokemon(Sql.pokemon_id[i], cfg.language) + getform + getcostume + str(
                        evolution) + " " + self.getGeschlecht(Sql.gender[i]) + " "

                if Sql.level[i] in (raid_level):
                    with open(cfg.areaName+cfg.areaNumber+"/eggs.txt") as input:
                        data = input.read()
                        data = data.replace(
                            "[", "").replace("'", "").replace("]", "")
                        data = data.split(', ')

                    bolt_line = str(lvl_icon) + " " + str(raid) + \
                        raid_start + " - " + raid_end
                    normal_line = str(team) + " " + str(name) + ex_raid + moveV

                    if send.list_output.__contains__(encounter):
                        f = open(cfg.areaName+cfg.areaNumber +
                                 "/output.txt", "r")
                        # Split the string based on space delimiter
                        list_string = f.read()
                        list_string = list_string[1:len(list_string)-1]
                        f.close()
                        list_string = list_string.split(', ')
                        id = list_string[send.list_output.index(encounter)]

                        pos = list_string.index(id)
                        egg = data[pos]
                        send.eggs.__contains__(encounter)

                        print("\n" + str(name) + " (ID: " +
                              str(id) + ", index: " + str(pos) + ")")
                        print("egg: " + str(egg))

                        x_old += 1

                        if egg == encounter and not Sql.pokemon_id[i] == None and cfg.singlechatId:
                            send.changeBossEgg(
                                bolt_line, normal_line, encounter, Sql.latitude[i], Sql.longitude[i], id, pos)

                    else:
                        print(
                            "===> found [" + str(i) + "] level " + str(level) + " " + str(raid))
                        if cfg.singlechatId:
                            try:
                                id = send.send(
                                    bolt_line, normal_line, encounter, Sql.latitude[i], Sql.longitude[i], Sql.pokemon_id[i])
                            except:
                                print("Fehler beim senden... Warte 60 Sekunden")
                                time.sleep(60)
                                id = send.send(
                                    bolt_line, normal_line, encounter, Sql.latitude[i], Sql.longitude[i], Sql.pokemon_id[i])
                    x += 1

                    header = "\n<b>## Level " + \
                        str(lvl_icon) + " Raids</b> \U0001F44A\n"

                    if cfg.singlechatId:
                        linked = cfg.singlechatUrl + "/" + str(id)
                    else:
                        linked = "https://maps.google.de/?q=" + \
                            str(Sql.latitude[i]) + ", " + str(Sql.longitude[i])

                    if x <= limit:
                        if not l10 and level == 10:
                            l10 = header
                            overview = overview + l10
                        if not l9 and level == 9:
                            l9 = header
                            overview = overview + l9
                        if not l8 and level == 8:
                            l8 = header
                            overview = overview + l8
                        if not l7 and level == 7:
                            l7 = header
                            overview = overview + l7
                        if not l6 and level == 6:
                            l6 = header
                            overview = overview + l6
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

                        overview += "<b>" + str(team) + str(raid) + raid_start + " - " + raid_end + "</b>" + str(
                            move) + "\n└ <a href='" + linked + "'>" + str(name) + "</a>" + str(ex_raid) + "\n"
                    elif x == limit+1:
                        overview += "\n\U00002514 Limit der Liste erreicht...\n"
                i += 1
            send.sendOverview(overview, self.getText(
                "noRaids", cfg.language), x, x_old)
            print("\nAktuell " + str(x) + " Raids (old: " +
                  str(x_old) + ", DB: " + str(i) + ")\n")

            # DEBUG:
            #f = open("TEST.txt", "a")
            # f.writelines("\n\n####################==========\\ " + str(datetime.datetime.now()) + " /==========####################")
            #f.writelines("len ==> " + str(len(overview)) + "\n")
            # f.writelines(str(overview))
            # f.close()

        except Exception as e:
            outF = open(Sql.areaName+cfg.areaNumber+"/error.txt", "w")
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
            ausgabe += "form: " + str(Sql.form.__len__) + "\n"
            ausgabe += "costume: " + str(Sql.costume.__len__) + "\n"
            ausgabe += "Wert i" + str(i) + "\n"
            outF.writelines(ausgabe + str(e))
            outF.close()

    # get pokemon name
    def getPokemon(self, value, language):
        data = open('json/Pokemon.json').read()
        switch = json.loads(data)
        if not str(value) in switch:
            return switch["null"][language]
        else:
            return switch[str(value)][language]

    # get pokemon form
    def getForm(self, value, language):
        data = open('json/Form.json').read()
        switch = json.loads(data)
        if not str(value) in switch:
            return switch["null"][language]
        else:
            return switch[str(value)][language]

    # get pokemon costume
    def getCostume(self, value, language):
        data = open('json/Costume.json').read()
        switch = json.loads(data)
        if not str(value) in switch:
            return switch["null"][language]
        else:
            return switch[str(value)][language]

    # get pokemon gender
    def getGeschlecht(self, value):
        if value == 1:
            return "\U00002642"
        elif value == 2:
            return "\U00002640"
        else:
            return "\U0000267E"

    # get pokemon quick move
    def getShortAttack(self, value, language):
        data = open('json/ShortAttack.json').read()
        switch = json.loads(data)
        if not str(value) in switch:
            return switch["null"][language]
        else:
            return switch[str(value)][language]

    # get pokemon load move
    def getLoadAttack(self, value, language):
        data = open('json/LoadAttack.json').read()
        switch = json.loads(data)
        if not str(value) in switch:
            return switch["null"][language]
        else:
            return switch[str(value)][language]

    # tranlate some other text
    def getText(self, value, language):
        text = {
            "noRaids": {
                "de": "Aktuell keine Raids vorhanden",
                "en": "No raids currently available",
                "fr": "Pas de raids disponibles actuellement"
            },
            "egg": {
                "de": "Ei",
                "en": "Egg",
                "fr": "Oeuf"
            }
        }
        return text[value][language]

    def gmt(self, datetime):
        millis = 1288483950000
        ts = millis * 1e-3
        utc_offset = datetime.fromtimestamp(ts) - datetime.utcfromtimestamp(ts)
        gmt = str(utc_offset)
        return gmt[0]
