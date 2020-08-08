import MySQLdb
import time

class Sql():
  gym_id = []
  team_id = []
  name = []
  latitude = []
  longitude = []
  level = []
  start = []
  end = []
  pokemon_id = []
  move_1 = []
  move_2 = []
  gender = []
  ex_raid = []
  form = []
  costume = []

  def startSQL(self,cfg):
    #Verbindungsaufbau zur MySQL-Datenbank
    try:
      connection = MySQLdb.connect(host=cfg.host,db=cfg.database,user=cfg.user, passwd=cfg.password)
      cursor = connection.cursor()
    except:
      print("Kein Verbindungsaufbau zur Datenbank, probiere es in 15 Sekunden erneut\n")
      time.sleep(15)
      return self.startSQL(cfg)
    self.gym_id.clear()
    self.team_id.clear()
    self.name.clear()
    self.latitude.clear()
    self.longitude.clear()
    self.level.clear()
    self.start.clear()
    self.end.clear()
    self.pokemon_id.clear()
    self.move_1.clear()
    self.move_2.clear()
    self.gender.clear()
    self.ex_raid.clear()
    self.form.clear()
    self.costume.clear()

#Abfragen der Daten aus der Datenbank

    cursor.execute("SELECT r.gym_id,g.team_id,d.name,g.latitude,g.longitude,r.level,r.start,r.end,r.pokemon_id,r.move_1,r.move_2,r.gender,g.is_ex_raid_eligible,r.form,r.costume FROM raid r LEFT JOIN gym g ON r.gym_id = g.gym_id LEFT JOIN gymdetails d ON r.gym_id = d.gym_id WHERE r.end > utc_timestamp() AND g.longitude BETWEEN " + cfg.min_longitude + " AND " + cfg.max_longitude + " AND g.latitude BETWEEN " + cfg.min_latitude + " AND " + cfg.max_latitude + " ORDER BY r.level DESC, r.pokemon_id, r.end")
    all = cursor.fetchall()
    i = 0
    try:
      while i < len(all):
        self.gym_id.append(all[i][0])
        self.team_id.append(all[i][1])
        self.name.append(all[i][2])
        self.latitude.append(all[i][3])
        self.longitude.append(all[i][4])
        self.level.append(all[i][5])
        self.start.append(all[i][6])
        self.end.append(all[i][7])
        self.pokemon_id.append(all[i][8])
        self.move_1.append(all[i][9])
        self.move_2.append(all[i][10])
        self.gender.append(all[i][11])
        self.ex_raid.append(all[i][12])
        self.form.append(all[i][13])
        self.costume.append(all[i][14])
        i +=1
    except Exception as e:
      outF = open(cfg.areaName+cfg.areaNumber+"/error.txt","w")
      ausgabe = "Passierte in der SQL.py\n"
      ausgabe += "gym_id: " + str(self.gym_id.__len__) + "\n"
      ausgabe += "team_id: " + str(self.team_id.__len__) + "\n"
      ausgabe += "name: " + str(self.name.__len__) + "\n"
      ausgabe += "latitude: " + str(self.latitude.__len__) + "\n"
      ausgabe += "longitude: " + str(self.longitude.__len__) + "\n"
      ausgabe += "level: " + str(self.level.__len__) + "\n"
      ausgabe += "start: " + str(self.start.__len__) + "\n"
      ausgabe += "end: " + str(self.end.__len__) + "\n"
      ausgabe += "pokemon_id: " + str(self.pokemon_id.__len__) + "\n"
      ausgabe += "move_1: " + str(self.move_1.__len__) + "\n"
      ausgabe += "move_2: " + str(self.move_2.__len__) + "\n"
      ausgabe += "gender: " + str(self.gender.__len__) + "\n"
      ausgabe += "ex_raid: " + str(self.ex_raid.__len__) + "\n"
      ausgabe += "form: " + str(self.form.__len__) + "\n"
      ausgabe += "costume: " + str(self.costume.__len__) + "\n"
      ausgabe += "Wert i" + str(i) + "\n"
      ausgabe += "All Variable: " + str(len(all))
      outF.writelines(ausgabe + str(e))
      outF.close()

    cursor = cursor.close()
    connection.close()