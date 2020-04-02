#!/usr/bin/env python
# -*- coding: utf-8 -*-

from configparser import ConfigParser
import ast

####Hier wird die Config aus dem Configfile geladen und den einzelen
####Werten zugewiesen

class Config():
  host = ""
  database = ""
  user = ""
  password = ""
  token = ""
  singlechatId = ""
  singlechatUrl = ""
  chatId = ""
  chatUrl = ""
  level = ""
  language = ""
  clockformat = int
  areaName = ""
  min_latitude = ""
  max_latitude = ""
  min_longitude = ""
  max_longitude = ""
  sleepTime = ""

  def readConfig(self,cfgFile):  
    parser = ConfigParser()
    parser.read(cfgFile, encoding='utf-8')

    self.host = parser.get('Mysql', 'host')
    self.database = parser.get('Mysql', 'database')
    self.user = parser.get('Mysql', 'user')
    self.password = parser.get('Mysql', 'password')

    self.token = parser.get('Bot Settings', 'token')
    self.singlechatId = parser.get('Bot Settings', 'singlechat_id')
    self.SinglechatUrl = parser.get('Bot Settings', 'singlechat_url')
    self.chatId = parser.get('Bot Settings', 'chat_id')
    self.chatUrl = parser.get('Bot Settings', 'chat_url')

    self.level = ast.literal_eval(parser.get("Raids", "level"))
    self.language = parser.get("Raids", "language")
    self.clockformat = parser.getint("Raids", "clockformat")

    self.areaName = parser.get('Geofence', 'areaName')
    self.min_latitude = parser.get('Geofence', 'minLat')
    self.max_latitude = parser.get('Geofence', 'maxLat')
    self.min_longitude = parser.get('Geofence', 'minLon')
    self.max_longitude = parser.get('Geofence', 'maxLon')

    self.sleepTime = parser.get('Message', 'sleep_time')