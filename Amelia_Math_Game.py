# -*- coding: utf-8 -*-
"""
Amelia's Math Program
Created on Sun Aug 21 17:46:24 2016

@author: Katie
"""
import sys
sys.path.insert(0, 'C:\Users\Katie\Anaconda2\Lib\site-packages')
print '\n'.join(sys.path)

import pygame
import time
pygame.init()

#Set frames per second
clock = pygame.time.Clock()

#Define Colors
aqua = 0, 245, 255
light_aqua = 204, 255, 255
purple = 128, 0, 128
black = 0, 0, 0
white = 255, 255, 255
pink = 255, 105, 180
light_pink = 255, 192, 203

#Set the screen size
width = 800
height = 600
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Amelia's Math Game")

#Text Functions
def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()
    
def title_display(text):
    titleText = pygame.font.Font('LiberationSerif-Regular.ttf', 64)
    TextSurf, TextRect = text_objects(text, titleText, aqua)
    TextRect.center = ((width/2),(height/2))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(15)
    
def counter_display(count):
    font = pygame.font.Font('LiberationSerif-Regular.ttf', 36)
    text = font.render("Number Right: "+str(count), True, aqua)
    screen.blit(text, (0,0))
    
#Button Function - Changes color with hover
def button(msg, x, y, w, h, ic, ac, tc, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print click
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))
    smalltext = pygame.font.Font('LiberationSerif-Regular.ttf', 24)
    textSurf, textRect = text_objects(msg, smalltext, tc)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

#Quit Game Loop
def quitgame():
    pygame.quit()
    quit()
    
#Start Menu Loop
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            print event
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(purple)
        button("Choose Level", 50, 400, 250, 100, aqua, light_aqua, purple)
        button("Exit Game", 500, 400, 250, 100, pink, light_pink, purple, action=quitgame)
        title_display("Amelia's Math Game")
        pygame.display.update()
        clock.tick(15)
        
game_intro()    
pygame.quit()
quit()
    
