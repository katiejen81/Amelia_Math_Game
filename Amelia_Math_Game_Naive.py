# -*- coding: utf-8 -*-
"""
Amelia's Math Program - Naive Version
Created on Sat Oct  1 20:53:19 2016
Written in Python2
@author: katie
"""

#Begin with importing our packages
from __future__ import division   
import random
import time 

#Define the introduction screen
def intro_screen():
    Intro = True
    while Intro:
        print 'Hi Amelia!'
        print 'Welcome to your Addition Game!'
        print "First let's choose a level."
        print "Enter number 1, 2, or 3 based upon the level you want to start."
        print "Type 'h' for more information about the levels."
        selector = raw_input('Enter number 1, 2 or 3 or h for help:')
        outcomes = ['1', '2', '3', 'h']
        if selector not in outcomes:
            print "Sorry! That value won't start the game!"
            print "Enter 1, 2, or 3 to start a level."
            print "Enter 'h' for more information."
        if selector.lower() == 'h':
            print "Help Screen"
            print "Level 1: Adds together numbers between 0-9 to numbers between 0-1."
            print "This is the simplest level because you will never have to add numbers equaling more than 10."
            print ""
            print "Level 2: Adds together numbers between 0-9 to numbers between 1-3."
            print "This is the next simplest level because sums may equal more than 10."
            print ""
            print "Level 3: Adds together numbers between 0-9 to other numbers between 0-9."
            print "This is the most challenging level because summed together results can get large."
            print ""
            selector = raw_input('Enter number 1, 2 or 3 or h for help:')
        if selector in outcomes and selector.lower() != 'h':
           return selector
           Intro = False
           
#Define the game play
def game(s):
    x = int(s)
    print 'Starting level %s:' % s
    selected = []
    while len(selected) < 5:
        r = random.randint(0, 9)
        if r not in selected:
            selected.append(r)
    ccount = 0
    loopct = 0      
    for i in selected:
        loopct = loopct + 1
        if x == 1:
            j = random.randint(0, 1)
        elif x == 2:
            j = random.randint(1, 3)
        elif x == 3:
            j = random.randint(0, 9)
        eq = ("\t %s " + "+" + " %s = ") % (i, j)
        panswer = raw_input(eq)
        canswer = i + j
        if int(panswer) == canswer:
            print "\tThat's right!"
            print ""
            ccount = ccount + 1
            time.sleep(2)
        elif int(panswer) != canswer and loopct < 5:
            print "That's not right, let's try another one"
            print ""
            time.sleep(2)
        else:
            print "That's not right, let's see how you did"
        
    pctc = str((ccount / 5)*100) + "%"
    print "You got %d correct out of 5" % (ccount)
    print "That's %s correct!" % (pctc) 
    #We will need to add some code down here in order to add a library of the internet treat
    #And we will need to add some stuff to allow Amelia to play again if she wants to     

    
#Game execution
selector = intro_screen()
game(selector)