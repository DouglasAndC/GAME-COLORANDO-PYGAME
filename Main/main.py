import pygame
import pygame as pygame
from pygame.locals import *
from sys import exit
from mapa import *

pygame.init()
SCREEN_SIZE = (1000, 600)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 16)
clock = pygame.time.Clock()
display = pygame.Surface((400, 300))

mapa = mapa('Data\mapa')

moving_right = False
moving_left = False
frame_user = 0
frame_vil = 0
frame_exp = 0
x_user = 20
y_user = 142
true_scroll = [0, 0]
fase_run = False
player_rect = pygame.Rect(75, 75, 5, 13)
globals.speed = 4
time = 500
sprites_user = [pygame.image.load(globals.get_path() + "\\View\\user_1.png").convert_alpha(),
                pygame.image.load(globals.get_path() + "\\View\\user_2.png").convert_alpha(),
                pygame.image.load(globals.get_path() + "\\View\\user_3.png").convert_alpha(),
                pygame.image.load(globals.get_path() + "\\View\\user_4.png").convert_alpha()]

sprites_vil = [pygame.image.load(globals.get_path() + "\\View\\vil_1.png").convert_alpha(),
               pygame.image.load(globals.get_path() + "\\View\\vil_2.png").convert_alpha(),
               pygame.image.load(globals.get_path() + "\\View\\vil_3.png").convert_alpha(),
               pygame.image.load(globals.get_path() + "\\View\\vil_4.png").convert_alpha(),
               pygame.image.load(globals.get_path() + "\\View\\vil_5.png").convert_alpha(),
               pygame.image.load(globals.get_path() + "\\View\\vil_6.png").convert_alpha(),
               pygame.image.load(globals.get_path() + "\\View\\vil_7.png").convert_alpha(),
               pygame.image.load(globals.get_path() + "\\View\\vil_8.png").convert_alpha(),
               pygame.image.load(globals.get_path() + "\\View\\vil_9.png").convert_alpha()]

sprites_exp = [pygame.image.load(globals.get_path() + "\\View\\exp_1.png").convert_alpha(),
               pygame.image.load(globals.get_path() + "\\View\\exp_2.png").convert_alpha(),
               pygame.image.load(globals.get_path() + "\\View\\exp_3.png").convert_alpha(),
               pygame.image.load(globals.get_path() + "\\View\\exp_4.png").convert_alpha(),
               pygame.image.load(globals.get_path() + "\\View\\exp_5.png").convert_alpha(),
               pygame.image.load(globals.get_path() + "\\View\\exp_6.png").convert_alpha()]


def desenhar_mapa(mapa):
    tile_rects = []
    y = 0
    for linha in mapa.value:
        x = 0
        for celula in linha:
            if celula == '1':
                display.blit(mapa.img_sub, (x * 32, y * 32))
            if celula == '2':
                display.blit(mapa.img_sup, (x * 32, y * 32))
            if celula == '3':
                display.blit(mapa.img_triangulo_p1, (x * 32, y * 32))
            if celula == '4':
                display.blit(mapa.img_triangulo_p2, (x * 32, y * 32))
            if celula == '5':
                display.blit(mapa.img_trapezio_p1, (x * 32, y * 32))
            if celula == '6':
                display.blit(mapa.img_trapezio_p2, (x * 32, y * 32))
            if celula == '7':
                display.blit(mapa.img_trapezio_p3, (x * 32, y * 32))
            if celula == '8':
                display.blit(mapa.img_triangulo_paralelo, (x * 32, y * 32))
            if celula != '0':
                tile_rects.append(pygame.Rect(x * 32, y * 32, 32, 32))
            x += 1
        y += 1


def explodir():
    pygame.time.wait(1000)
    return pygame.transform.scale(sprites_exp[frame_exp], (200, 200))


def gerar_desafio():
    formas = []


while True:
    clock.tick(12)
    screen.blit(pygame.transform.scale(display, SCREEN_SIZE), (0, 0))
    display.fill((146, 244, 255))
    display.blit(mapa.img_sol, (300, 10))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    desenhar_mapa(mapa)
    if frame_vil != 9:
        pygame.time.wait(time)
        frame_vil += 1
    if frame_vil == 9:
        frame_vil = 6
    if frame_vil == 5:
        pygame.time.wait(time)
        if frame_exp != 5:
            frame_exp += 1
        pygame.time.wait(time)
        display.blit(explodir(), (160, 100))
        mapa.att_mapa('Data\mapa_2')
        fase_run = False
    if fase_run:
        x_user += globals.speed
        if frame_user == 3:
            frame_user = 2
        else:
            frame_user += 1
        if x_user >= 400:
            x_user = 0

    img = sprites_user[frame_user]
    img_vil = sprites_vil[frame_vil]
    display.blit(img, (x_user, y_user))
    display.blit(img_vil, (360, 160))
    pygame.display.flip()
    pygame.display.update()
