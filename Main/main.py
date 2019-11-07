import pygame
import pygame as pygame
from pygame.locals import *
from sys import exit
import random
from mapa import *

pygame.init()
SCREEN_SIZE = (1000, 600)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 16)
clock = pygame.time.Clock()
display = pygame.Surface((400, 300))

mapa = mapa('Data\\mapa')
pygame.mixer.music.load(globals.get_path() + "\\Sound\\gameplay.mpeg")
pygame.mixer.music.play()
moving_right = False
moving_left = False
frame_user = 0
frame_vil = 0
frame_exp = 0
x_user = 20
y_user = 142
x_vil = 360
y_vil = 160
true_scroll = [0, 0]
fase_run = False
player_rect = pygame.Rect(75, 75, 5, 13)
globals.speed = 5
tempo = 800
rects = []
surfaces = []
texts = []
i_correto = 5
explodiu = False
desafio1 = False
desafio2 = False
desafio3 = False
continuar = True
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

btn1 = pygame.draw.rect(screen, (255, 255, 255), [50, 60, 60, 20])
btn2 = pygame.draw.rect(screen, (255, 255, 255), [150, 60, 60, 20])
btn3 = pygame.draw.rect(screen, (255, 255, 255), [250, 60, 60, 20])


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
    pygame.mixer.music.set_volume(25)
    pygame.mixer.music.load(globals.get_path() + "\\Sound\\explosion.mp3")
    pygame.mixer.music.play(1, 0.15)
    i = pygame.transform.scale(sprites_exp[frame_exp], (225, 225))
    pygame.time.wait(300)
    display.blit(i, (140, 100))
    pygame.mixer.music.load(globals.get_path() + "\\Sound\\gameplay.mpeg")
    pygame.mixer.music.play(5, 10)
    return True


def gerar_desafio(correto):
    formas = ["Quadrado", "Círculo", "Triângulo",
              "Hexágono", "Pentágono", "Retângulo",
              "Trapézio", "Paralelograma", "Losango", "Heptágono"]

    font = pygame.font.Font(pygame.font.match_font("Arial"), 20)
    x = 50
    if len(surfaces) != 3:
        for i in range(0, 3):
            text = formas[random.randint(0, len(formas) - 1)]
            while texts.__contains__(text) or text == correto:
                text = formas[random.randint(0, len(formas) - 1)]
            texts.append(text)
            if text != correto:
                newSurface = font.render(text, True, (0, 0, 0))
                surfaces.append(newSurface)
    if not texts.__contains__(correto):
        globals.index = random.randint(0, 2)
        texts[globals.index] = correto
        surfaces[globals.index] = font.render(correto, True, (0, 0, 0))

    display.blit(surfaces[0], (x, 50))
    display.blit(surfaces[1], (x + 100, 50))
    display.blit(surfaces[2], (x + 200, 50))

    return True


while True:
    clock.tick(12)
    screen.blit(pygame.transform.scale(display, SCREEN_SIZE), (0, 0))
    display.fill((146, 244, 255))
    display.blit(mapa.img_sol, (300, 10))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
            if len(rects) > 0:
                if rects[0].collidepoint(pos) and pressed1:
                        print("testando")
                        desafio1 = True
                        aux = False
                elif rects[1].collidepoint(pos) and pressed1:
                        print("testando")
                        desafio1 = True
                elif rects[2].collidepoint(pos) and pressed1:
                        print("testando")
                        desafio1 = True
                elif event.type == QUIT:
                        pygame.quit()
                        exit()
    desenhar_mapa(mapa)
    if frame_vil != 9:
        pygame.time.wait(tempo)
        frame_vil += 1
    if frame_vil == 9:
        frame_vil = 6
        x_vil += globals.speed
    if frame_vil == 6 and not explodiu:
        mapa.att_mapa('Data\mapa_2')
        tempo = 0
        for i in sprites_exp:
            explodir()
        explodiu = True
        fase_run = False
    if x_vil == 400:
        fase_run = True
    if fase_run:
        respostas = gerar_desafio("Paralelograma")
        rects = [pygame.draw.rect(screen, (255, 255, 255), [150, 110, 80, 40]),
                 pygame.draw.rect(screen, (255, 255, 255), [450, 110, 80, 40]),
                 pygame.draw.rect(screen, (255, 255, 255), [650, 110, 200, 40])]
        if desafio1:
            x_user += globals.speed
            if frame_user == 3:
                frame_user = 2
            else:
                frame_user += 1
            if x_user >= 400:
                x_user = 0
        else:
            display.blit(pygame.image.load(globals.get_path() + "\\View\\fase1\\btnError.png").convert_alpha(),(300, 300))
    img = sprites_user[frame_user]
    display.blit(img, (x_user, y_user))
    img_vil = sprites_vil[frame_vil]
    display.blit(img_vil, (x_vil, y_vil))
    pygame.display.update()
