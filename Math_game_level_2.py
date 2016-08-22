# -*- coding: utf-8 -*-
"""
Random Addition Problems - Level 2
Created on Sun Aug 21 21:12:12 2016

@author: Katie
"""
from __future__ import division   
import random     

selected = []
while len(selected) < 5:
    r = random.randint(0, 9)
    if r in selected:
        print r
    else:
        selected.append(r)
        
ccount = 0      
loopct = 0
for i in selected:
    loopct = loopct + 1
    j = random.randint(1, 3)
    eq = ("%s " + "+" + " %s") % (i, j)
    panswer = raw_input(eq)
    canswer = i + j
    if int(panswer) == canswer:
        print "That's right!"
        ccount = ccount + 1
    elif int(panswer) != canswer and loopct < 5:
        print "That's not right, let's try another one"
    else:
        print "That's not right, let's see how you did"
        
pctc = str((ccount / 5)*100) + "%"
print "You got %d correct out of 5" % (ccount)
print "That's %s correct!" % (pctc)      
    
