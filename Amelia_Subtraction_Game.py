# -*- coding: utf-8 -*-
"""
Amelia Subtraction Game
Created on Sun Apr  9 17:07:11 2017
Written in Python 2
@author: katie
"""

#Begin with importing our packages
from __future__ import division   
import random
import time 
import webbrowser

#Define the introduction screen
def intro_screen():
    Intro = True
    while Intro:
        print 'Hi Amelia!'
        print 'Welcome to your Subtraction Game!'
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
            print "Level 1: Subtracts numbers between 0-1 from numbers between 0-9."
            print "This is the simplest level because the result is never more than one away from the original number."
            print ""
            print "Level 2: Subtracts numbers between 1-3 from numbers between 1-9."
            print "This is the next simplest level because the result is 1 to 3 away from the original number"
            print ""
            print "Level 3: Subtracts numbers between 0-9 from other numbers between 0-9."
            print "This is the most challenging level because there can be a wide variety of problems."
            print ""
            selector = raw_input('Enter number 1, 2 or 3 or h for help:')
        if selector in outcomes and selector.lower() != 'h':
           return selector
           Intro = False
           
def play_again():
    print "Would you like to play again? Enter Y for yes or N for no."
    print "Entering N will quit the game."
    cgame = raw_input('Enter Y to play again, N to quit: ')
    return cgame
    
def internet_treat():
    print "Please enjoy this internet treat as a reward for your hard work!"
    library = ['http://www.zooborns.com/', 
        'http://spaceplace.nasa.gov/menu/solar-system/', 
        'http://kids.nationalgeographic.com/animals/', 
        'http://www.akc.org/', 
        'http://www.americaslibrary.gov/es/index.php', 
        'http://www.americaslibrary.gov/aa/earhart/aa_earhart_subj.html', 
        'http://www.americaslibrary.gov/jb/index.php', 
        'http://www.americaslibrary.gov/sh/animation/sh_animation_cartoon_1.html',
        'http://www.scholastic.com/scholastic_thanksgiving/',
        'http://amazingspace.org/',
        'https://earth.jsc.nasa.gov/Collections/EarthFromSpace/lores.pl?PHOTO=ISS029-E-12564',
        'https://earth.jsc.nasa.gov/Collections/EarthFromSpace/photoinfo.pl?PHOTO=STS064-46-26',
        'https://earth.jsc.nasa.gov/Collections/EarthFromSpace/photoinfo.pl?PHOTO=STS066-124-46',
        'https://earth.jsc.nasa.gov/Collections/EarthFromSpace/photoinfo.pl?PHOTO=SL3-46-199',
        'https://earth.jsc.nasa.gov/Collections/EarthFromSpace/photoinfo.pl?PHOTO=ISS006-E-21591',
        'https://earth.jsc.nasa.gov/Collections/EarthFromSpace/photoinfo.pl?PHOTO=STS039-342-28',
        'http://fourmilab.ch/cgi-bin/Earth/action?opt=-p',
        'https://www.youtube.com/watch?v=bWeaQctUp1c',
        'http://creatingmusic.com/new/scales/index.html',
        'http://creatingmusic.com/stepPlay/index.html',
        'https://archive.org/details/PeterAndTheWolf_753',
        'http://www.classicsforkids.com/music/instruments_orchestra.asp',
        'http://www.classicsforkids.com/music/hear.asp',
        'http://www.classicsforkids.com/music/periods.asp',
        'http://www.exploratorium.edu/hockey/',
        'http://www.colormatters.com/color-matters-for-kids/why-are-school-buses-yellow',
        'http://www.colormatters.com/color-matters-for-kids/how-animals-see-color',
        'http://www.metmuseum.org/metmedia/interactives/start-with-art/learn-about-color',
        'http://www.metmuseum.org/art/online-features/metkids/time-machine',
        'http://www.bbc.co.uk/nature/life/Dinosaur',
        'http://www.nationalgeographic.com/features/96/dinoeggs/museum/intro/museum.html'
        ]
    ts = random.randint(0, 30)
    webbrowser.open(library[ts])
    
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
        first = max((i, j))
        second = min((i, j))
        eq = ("\t %s " + "-" + " %s = ") % (first, second)
        panswer = raw_input(eq)
        canswer = first - second
        if int(panswer) == canswer:
            print "\tThat's right!"
            print ""
            ccount = ccount + 1
            time.sleep(2)
        elif int(panswer) != canswer and loopct < 5:
            print "\tThat's not right, let's try another one"
            print ""
            time.sleep(2)
        else:
            print "\tThat's not right, let's see how you did"
        
    pctc = str((ccount / 5)*100) + "%"
    print "You got %d correct out of 5" % (ccount)
    print "That's %s correct!" % (pctc) 
    
    if ccount / 5 < .5:
        print "Let's play again so that you can keep trying."
    else:
        print "You did great!"
        time.sleep(5)
        internet_treat()
            
    #We will need to add some code down here in order to add a library of the internet treat
    #And we will need to add some stuff to allow Amelia to play again if she wants to     

#Game execution

lgame = True
while lgame:
    selector = intro_screen()
    game(selector)
    cgame = play_again()
	    
    if cgame.lower() == 'n':
	lgame = False
    elif cgame.lower() == 'y':
	lgame = True
    else:
	print "That entry won't work!"
	print "Please enter a Y to keep playing, N to quit."
	cgame = play_again()
quit()