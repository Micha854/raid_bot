#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sql
import createMessage
import sendMessage
import logging
import time
import config
import sys

class Module():
  def level(self,cfg):
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