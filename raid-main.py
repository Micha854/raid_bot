#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config
import createMessage
import sql
import sendMessage
import sys
import time
import clear
import os

from datetime import datetime
timestamp = time.time()
time_now = datetime.fromtimestamp(timestamp)
time_utc = datetime.utcfromtimestamp(timestamp)
utc_offset_secs = (time_now - time_utc).total_seconds()

# Flag variable to hold if the current time is behind UTC.
is_behind_utc = False

# If the current time is behind UTC convert the offset
# seconds to a positive value and set the flag variable.
if utc_offset_secs < 0:
    is_behind_utc = True
    utc_offset_secs *= -1

# Build a UTC offset string suitable for use in a timestamp.
if is_behind_utc:
    pos_neg_prefix = "-"
else:
    pos_neg_prefix = "+"

utc_offset = time.gmtime(utc_offset_secs)
utc_offset_fmt = time.strftime("%H", utc_offset)
gmt = int(pos_neg_prefix + utc_offset_fmt)

####Lade das Configfile
cfg = config.Config()
try:
  cfg.readConfig(sys.argv[1])
except:
  cfg.readConfig("config.ini")

if not os.path.exists(cfg.areaName+cfg.areaNumber):
    os.mkdir(cfg.areaName+cfg.areaNumber)
    print("Temp Directory " , cfg.areaName+cfg.areaNumber ,  " Created ")
else:    
    print("Temp Directory " , cfg.areaName+cfg.areaNumber ,  " already exists")

if cfg.level:
  clear = clear.Clear()
  clear.clear(cfg.token,cfg.singlechatId,cfg)

  send = sendMessage.sendMessage()
  send.setConfig(cfg.token,cfg.singlechatId,cfg.chatId,cfg.areaName,cfg.areaNumber)
  sys.stdout.write("\x1b]2;%s\x07" % cfg.areaName+cfg.areaNumber)
  
  while 1 == 1:
    Sql = sql.Sql()
    Sql.startSQL(cfg)
    send.clearOutputList(Sql.gym_id)
    create = createMessage.createMessage()
    create.create(Sql,send,cfg.sleepTime,cfg,gmt)
    time.sleep(int(cfg.sleepTime))
else:
	print("Es wurde kein Raid Level aktiviert !!!")