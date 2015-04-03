# -*- coding:utf-8 -*-
"""
@author: bellkeyang
@edit_time: 2015-04-03
@function: size unit switch
"""

import math

def bform(size, unit='Bytes'):
   units = ['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB']
   return ('%.2f' + " " +unit) %(size/math.pow(1024,units.index(unit)))
