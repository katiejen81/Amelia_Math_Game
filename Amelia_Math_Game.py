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

#Set the screen size
width = 800
height = 600
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Amelia's Math Game")

#Text Functions
def text_objects(text, font):
    textSurface = font.render(text, True, aqua)
    return textSurface, textSurface.get_rect()
    
def message_display(text):
    titleText = pygame.font.Font('Century Schoolbook.ttf', 64)
    TextSurf, TextRect = text_objects(text, titleText)
    TextRect.center = ((width/2),(height/2))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    
    

#Initialize the Close Game Button

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        print event
        screen.fill(purple)
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
quit()
    
