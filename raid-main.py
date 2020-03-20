#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config
import module
import clear
import sys

####Lade das Configfile
cfg = config.Config()
try:
  cfg.readConfig(sys.argv[1])
except:
  cfg.readConfig("config.ini")

clear = clear.Clear()
clear.clear(cfg.token,cfg.ivchatId,cfg)

raids = module.Module()
if cfg.level:
  raids.level(cfg)
else:
	print("Es wurde kein Raid Level aktiviert !!!")