import pygame
from pygame.locals import *
from sys import exit
from mapa import *

pygame.init()
SCREEN_SIZE = (1000, 500)
screen = pygame.display.set_mode()
clock = pygame.time.Clock()
display = pygame.Surface((500, 300))
pulo = False

global cont
cont = 1

mapa = mapa('Data\mapaCorrida')

BLACK = (0, 0, 0)
moving_right = False
moving_left = False
frame_user = 1
x_user = 10
y_user = 140
true_scroll = [0, 0]
aux = 1

player_rect = pygame.Rect(65, 75, 5, 13)


def dimensao_botao(botao):
    btn = pygame.image.load(globals.get_path() + '\\View\\corrida\\' + botao + '.png').convert_alpha()
    novo_botao = pygame.transform.scale(btn, (int(372 / 2), int(149 / 2)))
    return novo_botao


def botoesMenu(color, x, y, width, height):
    return pygame.draw.rect(screen, color, [x, y, width, height])


def regras():
    pos = pygame.mouse.get_pos()
    pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
    btn1 = botoesMenu(BLACK, 400, 400, 372 / 2, 149 / 2)
    display.fill((146, 244, 255))
    txtFase3 = pygame.image.load(globals.get_path() + '\\View\\corrida\\txtFase3.png').convert_alpha()
    novo_txtFase3 = pygame.transform.scale(txtFase3, (int(1376 / 2), int(541 / 2)))
    screen.blit(novo_txtFase3, (180, 50))
    screen.blit(dimensao_botao('btnContinuar'), (400, 400))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    if btn1.collidepoint(pos) and pressed1:
        return 1
    else:
        return 0


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
            if celula != '0':
                tile_rects.append(pygame.Rect(x * 32, y * 32, 32, 32))
            x += 1
        y += 1


while True:
    display.fill((146, 244, 255))
    if cont == 1:
        cont = cont - regras()
    else:
        clock.tick(12)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    pulo = True
        if pulo:
            if aux < 11:
                aux = aux + 1
                y_user = y_user - 5
            elif 11 <= aux < 14:
                aux = aux + 1
            elif 14 <= aux < 24:
                aux = aux + 1
                y_user = y_user + 5
            else:
                aux = 1
                pulo = False

        display.fill((146, 244, 255))
        img = pygame.image.load(globals.get_path() + "\\View\\user_" + str(frame_user) + ".png").convert_alpha()
        globals.speed = 6
        x_user += globals.speed
        display.blit(img, (x_user, y_user))
        if pulo == True:
            frame_user = 1
        else:
            if frame_user == 4:
                frame_user = 2
            else:
                frame_user -= -1
        desenhar_mapa(mapa)
        # display.blit(mapa.img_sol,(300,-30))
        screen.blit(pygame.transform.scale(display, SCREEN_SIZE), (0, 0))
        pygame.display.update()
