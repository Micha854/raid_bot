#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telebot

class sendMessage():
  chatID = 0
  bot = ""
  list_output = [] ##Beinhaltet alle Encounters welche versendet wurden
  list_message_ID = []
  eggs = []
  overview_old = ""
  overviewId = 0
  areaName = ""
  
  def changeBossEgg(self,bolt_line,normal_line,encounter,latitude,longitude,id,pos):
    try:
      self.bot.delete_message(self.singlechatID,id)
    except:
      print(self.areaName+" Egg Nachricht konnte nicht gelöscht werden, ID:" + str(id) + " in chatID: " + str(self.singlechatID))
    try:
      id = self.bot.send_venue(self.singlechatID,latitude,longitude,bolt_line,normal_line,disable_notification=True)
      self.list_message_ID[pos] = id.message_id
      self.eggs[pos] = "change to raid"
      outE = open(self.areaName+"eggs.txt","w")
      outE.writelines(str(self.eggs))
      outE.close()
      
      outF = open(self.areaName+"output.txt","w")
      outF.writelines(str(self.list_message_ID))
      outF.close()
    except:
      print(self.areaName+" Neue Boss Nachricht konnte nicht gesendet werden")

  def send(self,bolt_line,normal_line,encounter,latitude,longitude,pokemon_id):
    try:
      id = self.bot.send_venue(self.singlechatID,latitude,longitude,bolt_line,normal_line,disable_notification=True)
      self.list_output.append(encounter)
      self.list_message_ID.append(id.message_id)
      if not pokemon_id == None:
        self.eggs.append("active raid")
      else:
        self.eggs.append(encounter)
      outE = open(self.areaName+"eggs.txt","w")
      outE.writelines(str(self.eggs))
      outE.close()

      outF = open(self.areaName+"output.txt","w")
      outF.writelines(str(self.list_message_ID))
      outF.close()
      return id.message_id
    except:
      print(self.areaName+" Nachricht konnte nicht versendet werden")
  
  def sendOverview(self,message,text,raids,old_raids):
    if message == "":
      message = text
    if not message == self.overview_old:
      if (self.singlechatID != self.chatID) or (len(message) <= len(self.overview_old)) and raids == old_raids:
        try:
          self.bot.edit_message_text(message,chat_id=self.chatID, message_id=self.overviewId.message_id, parse_mode='HTML',disable_web_page_preview=True) ##Nachricht 
          self.overview_old = message
        except:
          try:
            print(self.areaName+" Konnte aber nicht editiern")
            self.bot.delete_message(self.chatID,self.overviewId.message_id)
            self.overviewId = self.bot.send_message(self.chatID,message,parse_mode='HTML')
            self.overview_old = message
          except:
            try:
              self.overviewId = self.bot.send_message(self.chatID,message,parse_mode='HTML',disable_web_page_preview=True,disable_notification=False)
              self.overview_old = message
            except:
              print(self.areaName+" Nachricht konnte nicht editiert werden")    
      else:
        try: 
          self.bot.delete_message(self.chatID,self.overviewId.message_id)
          self.overviewId = self.bot.send_message(self.chatID,message,parse_mode='HTML')
          self.overview_old = message
        except:
          try:
            self.overviewId = self.bot.send_message(self.chatID,message,parse_mode='HTML',disable_web_page_preview=True,disable_notification=False)
            self.overview_old = message
          except:
            print(self.areaName+" Nachricht konnte nicht gesendet werden")
   
  def clearOutputList(self,encounter):
    i = 0
    print(self.areaName+" Checke Outputliste")
    for encount in self.list_output:
      if not encounter.__contains__(encount):
        try:
          print(self.areaName+" Entferne Nachricht")
          self.bot.delete_message(self.singlechatID,self.list_message_ID[i])
          self.list_message_ID.__delitem__(i)
          self.list_output.__delitem__(i)
          self.eggs.__delitem__(i)
        except:
          print(self.areaName+" Nachricht konnte nicht entfernt werden")
      i +=1
    outF = open(self.areaName+"output.txt","w")
    outF.writelines(str(self.list_message_ID))
    outF.close()

    outE = open(self.areaName+"eggs.txt","w")
    outE.writelines(str(self.eggs))
    outE.close()

  def setConfig(self,token,singlechatID,chatID,areaName):
    self.areaName = areaName
    self.singlechatID = singlechatID
    self.chatID = chatID
    self.bot = telebot.TeleBot(token)
