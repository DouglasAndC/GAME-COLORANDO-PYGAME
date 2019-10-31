import pygame
from pygame.locals import *
from sys import exit
from mapa import *

pygame.init()
SCREEN_SIZE = (1000,500)
screen = pygame.display.set_mode(SCREEN_SIZE, 0 ,16)
clock = pygame.time.Clock()
display = pygame.Surface((400,200))

mapa = mapa('Data\mapa')

moving_right = False
moving_left = False
frame_user = 1
x_user = 104
y_user = 140
true_scroll = [0,0]

player_rect = pygame.Rect(75,75,5,13)

def desenhar_mapa(mapa):
       tile_rects = []
       y=0
       for linha in mapa.value:
        x = 0
        for celula in linha:
            if celula == '1':
                display.blit(mapa.img_sub,(x*32,y*32))
            if celula == '2':
                display.blit(mapa.img_sup,(x*32,y*32))
            if celula == '3':
                display.blit(mapa.img_triangulo_p1,(x*32,y*32))
            if celula == '4':
                display.blit(mapa.img_triangulo_p2,(x*32,y*32))
            if celula == '5':
                display.blit(mapa.img_trapezio_p1,(x*32,y*32))
            if celula == '6':
                display.blit(mapa.img_trapezio_p2,(x*32,y*32))
            if celula == '7':
                display.blit(mapa.img_trapezio_p3,(x*32,y*32))
            if celula != '0':
                tile_rects.append(pygame.Rect(x*32,y*32,32,32))
            x += 1
        y += 1

while True:
    display.fill((146,244,255))
    clock.tick(12)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    display.fill((146,244,255))
    img = pygame.image.load(globals.get_path() + "\\View\\user_"+str(frame_user)+".png").convert_alpha()
    globals.speed=4
    x_user+=globals.speed
    display.blit(img,(x_user,y_user))
    if(frame_user == 4):
        frame_user=2
    else:
        frame_user-=-1
    if(x_user>=400):
        x_user=0
        display=pygame.Surface((600,400))
    desenhar_mapa(mapa)
    display.blit(mapa.img_sol,(300,10))
    screen.blit(pygame.transform.scale(display,SCREEN_SIZE),(0,0))
    pygame.display.update()
