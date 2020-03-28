#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config
import createMessage
import sql
import sendMessage
import sys
import time
import clear

####Lade das Configfile
cfg = config.Config()
try:
  cfg.readConfig(sys.argv[1])
except:
  cfg.readConfig("config.ini")

if cfg.level:
  clear = clear.Clear()
  clear.clear(cfg.token,cfg.ivchatId,cfg)

  send = sendMessage.sendMessage()
  send.setConfig(cfg.token,cfg.ivchatId,cfg.chatId,cfg.areaName)
  sys.stdout.write("\x1b]2;%s\x07" % cfg.areaName)
  
  while 1 == 1:
    Sql = sql.Sql()
    Sql.startSQL(cfg)
    send.clearOutputList(Sql.gym_id)
    create = createMessage.createMessage()
    create.create(Sql,send,cfg.sleepTime,cfg)
    time.sleep(int(cfg.sleepTime))
else:
	print("Es wurde kein Raid Level aktiviert !!!")