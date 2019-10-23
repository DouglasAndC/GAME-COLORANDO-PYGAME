import pygame
from pygame.locals import *
from sys import exit
from mapa import *

pygame.init()
SCREEN_SIZE = (1000,400)
screen = pygame.display.set_mode(SCREEN_SIZE, 0 ,16)

mapa = mapa('Data\mapa')

moving_right = False
moving_left = False
vertical_momentum = 0
air_timer = 0

true_scroll = [0,0]

player_rect = pygame.Rect(100,100,5,13)

def desenhar_mapa(mapa):
       tile_rects = []
       y=0
       for linha in mapa.value:
        x = 0
        for celula in linha:
            if celula == '1':
                screen.blit(mapa.img_sub,(x*32,y*32))
            if celula == '2':
                screen.blit(mapa.img_sup,(x*32,y*32))
            if celula == '3':
                screen.blit(mapa.img_triangulo_p1,(x*32,y*32))
            if celula == '4':
                screen.blit(mapa.img_triangulo_p2,(x*32,y*32))
            if celula == '5':
                screen.blit(mapa.img_trapezio_p1,(x*32,y*32))
            if celula == '6':
                screen.blit(mapa.img_trapezio_p2,(x*32,y*32))
            if celula == '7':
                screen.blit(mapa.img_trapezio_p3,(x*32,y*32))
            if celula != '0':
                tile_rects.append(pygame.Rect(x*32,y*32,32,32))
            x += 1
        y += 1

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    desenhar_mapa(mapa)

    pygame.display.update()