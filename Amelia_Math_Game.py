# -*- coding: utf-8 -*-
"""
Amelia's Math Program
Created on Sun Aug 21 17:46:24 2016

@author: Katie
"""

import pygame
import time
pygame.init()

#Set frames per second
clock = pygame.time.Clock()

#Define Colors
aqua = 0, 245, 255
purple = 128, 0, 128
black = 0, 0, 0
white = 255, 255, 255
pink = 255, 105, 180

#Set the screen size
width = 800
height = 600
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Amelia's Math Game")

#Text Functions
def text_objects(text, font):
    textSurface = font.render(text, True, aqua)
    return textSurface, textSurface.get_rect()
    
def title_display(text):
    titleText = pygame.font.Font('LiberationSerif-Regular.ttf', 64)
    TextSurf, TextRect = text_objects(text, titleText)
    TextRect.center = ((width/2),(height/2))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(15)
    
def counter_display(count):
    font = pygame.font.Font('LiberationSerif-Regular.ttf', 16)
    text = font.render("Number Right: "+str(count), True, aqua)
    screen.blit(text, (0,0))

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
        pygame.draw.rect(screen, aqua, (50, 400, 250, 100))
        pygame.draw.rect(screen, pink, (500, 400, 250, 100)) 
        pygame.display.update()
        title_display("Amelia's Math Game")

        

        
game_intro()    
pygame.quit()
quit()
    
