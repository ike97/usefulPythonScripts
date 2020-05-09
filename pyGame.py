# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 07:43:10 2018

@author: ikeos
"""

import pygame

pygame.init()
width = 640
height = 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Hey, man...')
clock = pygame.time.Clock()
fps = 30
color = (0,0,255)
black = (0,0,0)
surface = pygame.Surface(screen.get_size())
surface.fill(color)
screen.blit(surface, (0,0))
surface = surface.convert()

movedSurface = pygame.Surface((50,50))
pygame.draw.rect(movedSurface, black, (50,50,50,50))
x = 50
y = 50
screen.blit(movedSurface , (x,y))
movedSurface = movedSurface.convert()
running = True

while(running):
    screen.fill(color)
    pygame.draw.rect(movedSurface, black, (x,y,50,50))   
    screen.blit(movedSurface, (x,y))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                
    clock.tick(fps)
    pygame.display.flip() 
    
pygame.quit()