#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Helper():

  def nice_time(self,string):
    value = int(string)
    if value < 10:
      newTime = "0" + str(value)
      return newTime

    return str(value)
