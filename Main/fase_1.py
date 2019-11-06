import pygame
from pygame.locals import *
from pygame import *
import globals
import pygame as pg
from pygame.mixer import Sound
import time


pg.init()
# definindo cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ROXO = (127,0,127)
LARANJA = (255, 127, 0)
AMARELO = (255,255,0)
COR1 = (153, 0, 153)
PELE = (251, 230, 226)
CorSelecionada = (0, 255, 0)
global cor1
cor1 = (0, 0, 0)

cont = 1

fase = 0

pygame.init()

pygame.mixer.init()

fundo = pygame.mixer.music.load(globals.get_path() + '\\Sound\\gameplay.mpeg')
pygame.mixer.music.play()

screen = pygame.display.set_mode((800, 700))
# carregando fonte
font = pygame.font.SysFont(None, 55)

pygame.display.set_caption('COLORANDO')

# preenchendo o fundo com preto
screen.fill(PELE)

def regras():
      flag = True
      while True:
         if(flag== False):
            break
         else:
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                pressed1,pressed2,pressed3 = pygame.mouse.get_pressed()
                btn0 = botoesMenu(BLACK,300,500,372/2,149/2)
                txtFase3 = pygame.image.load(globals.get_path()+'\\View\\fase1\\txtFase1.png').convert_alpha()
                screen.fill(PELE)
                novo_txtFase3 = pygame.transform.scale(txtFase3,(int(1363/2),int(541/2)))
                screen.blit(novo_txtFase3,(60,150))
                screen.blit(botao_continuar('btnContinuar'),(300,500))
                pygame.display.update()
                if event.type == QUIT:
                  pygame.quit()
                  exit()
                elif btn0.collidepoint(pos) and pressed1:
                    flag = False
                    break

def botao_continuar(botao):
       btn = pygame.image.load(globals.get_path()+'\\View\\corrida\\'+botao+'.png').convert_alpha()
       novo_botao = pygame.transform.scale(btn,(int(372/2),int(149/2)))
       return novo_botao

def dimensao_botao(botao):
        btn = pygame.image.load(globals.get_path()+'\\View\\fase1\\'+botao+'.png').convert_alpha()
        novo_botao = pygame.transform.scale(btn,(int(400),int(1500/2)))
        return novo_botao

def titulo():
        titulo = pygame.image.load(globals.get_path()+'\\View\\fase1\\titulo.png').convert_alpha()
        novo_titulo = pygame.transform.scale(titulo,(int(726/2), int(217/2)))
        screen.blit(novo_titulo,(210,50))

def torneira():
        titulo = pygame.image.load(globals.get_path()+'\\View\\fase1\\torneira.png').convert_alpha()
        novo_titulo = pygame.transform.scale(titulo,(int(650), int(500)))
        screen.blit(novo_titulo,(-200,0))

def balde():
        titulo = pygame.image.load(globals.get_path()+'\\View\\fase1\\balde.png').convert_alpha()
        novo_titulo = pygame.transform.scale(titulo,(int(500), int(700)))
        screen.blit(novo_titulo,(2,0))

def botoesMenu(color,x,y,width,height):
        return pygame.draw.rect(screen, color, [x, y, width, height])

def instrucao():
        titulo = pygame.image.load(globals.get_path()+'\\View\\fase1\\txtCorFormada.png').convert_alpha()
        screen.blit(titulo,(50,40))

def btnConfirmar():
        titulo = pygame.image.load(globals.get_path()+'\\View\\fase1\\btnConfirmar.png').convert_alpha()
        novo_titulo = pygame.transform.scale(titulo,(int(115), int(215)))
        screen.blit(novo_titulo,(500,495))

def menu():
        btn1 = botoesMenu(BLACK,630,240,40,70)#azul
        btn2 = botoesMenu(BLACK,630,340,40,70)#amarelo
        btn3 = botoesMenu(BLACK,630,440,40,70)#vermelho
        btn4 = botoesMenu(BLACK,730,240,40,70)#verde
        btn5 = botoesMenu(BLACK,730,340,40,70)#laranja
        btn6 = botoesMenu(BLACK,730,440,40,70)#roxo
        btn7 = botoesMenu(BLACK,620,580,60,100)#juntar
        btn8 = botoesMenu(BLACK,720,560,60,130)#lixo
        btn9 = botoesMenu(BLACK,515,560,60,120)#confirma
        screen.fill(PELE)

        #titulo()
        instrucao()
        torneira()
        balde()
        #Quadrados que indicarão a cor a ser desenhada
        #screen.blit(dimensao_botao('quad_verde'),(460,-300))
        #screen.blit(dimensao_botao('quad_laranja'),(460,-300))
        #screen.blit(dimensao_botao('quad_roxo'),(460,-300))
        if(fase ==0):
             screen.blit(dimensao_botao('quad_verde'),(460,-300))
        elif(fase == 1):
             screen.blit(dimensao_botao('quad_laranja'),(460,-300))
        else:
             screen.blit(dimensao_botao('quad_roxo'),(460,-300))
        screen.blit(dimensao_botao('btnAzul'),(450,-100))
        screen.blit(dimensao_botao('btnAmarelo'),(450,0))
        screen.blit(dimensao_botao('btnVermelho'),(450,100))
        if(fase >=1):
            screen.blit(dimensao_botao('btnVerde'),(550,-100))
        if(fase >= 2):
            screen.blit(dimensao_botao('btnLaranja'),(550,0))
        if(fase >= 3):
           screen.blit(dimensao_botao('btnRoxo'),(550,100))

        pygame.display.update()

        return btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9

def derramando1(cor,x, y, widht,height):
    aux = 1
    while(aux < 365):
        botoesMenu(cor,188,313,60,aux)
        pygame.display.flip()
        aux= aux + 1
    botoesMenu(cor,x, y, widht,height)
    pygame.display.flip()
def derramando2(cor,x, y, widht,height):
    aux = 1
    while(aux!= 195):
        botoesMenu(cor,188,313,60,aux)
        pygame.display.flip()
        aux= aux + 1
    botoesMenu(cor,x, y, widht,height)
    pygame.display.flip()

def primeiro():
    while True:
            for event in pygame.event.get():
                    pygame.display.update()
                    pos = pygame.mouse.get_pos()
                    pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
                    if menu_botoes[0].collidepoint(pos) and pressed1:
                        derramando1(BLUE,19, 508, 468, 170)
                        botoesMenu(PELE,188,313,60,195)
                        pygame.display.flip()
                        return  BLUE
                    elif menu_botoes[1].collidepoint(pos) and pressed1:
                        derramando1(AMARELO,19, 508, 468, 170)
                        botoesMenu(PELE,188,313,60,195)
                        pygame.display.flip()
                        return AMARELO
                    elif menu_botoes[2].collidepoint(pos) and pressed1:
                        derramando1(RED,19, 508, 468, 170)
                        botoesMenu(PELE,188,313,60,195)
                        pygame.display.flip()
                        return RED
                    elif menu_botoes[3].collidepoint(pos) and pressed1:
                       if(fase>= 1):
                           derramando1(GREEN,19, 508, 468, 170)
                           botoesMenu(PELE,188,313,60,195)
                           pygame.display.flip()
                           return GREEN
                    elif menu_botoes[4].collidepoint(pos) and pressed1:
                        if(fase>= 2):
                           derramando1(LARANJA,19, 508, 468, 170)
                           botoesMenu(PELE,188,313,60,195)
                           pygame.display.flip()
                           return LARANJA
                    elif menu_botoes[5].collidepoint(pos) and pressed1:
                         if(fase>= 3):
                           derramando1(ROXO,19, 508, 468, 170)
                           botoesMenu(PELE,188,313,60,195)
                           pygame.display.flip()
                           return ROXO
                    if event.type == QUIT:
                        pygame.quit()
                        exit()

def segundo():
    while True:
            for event in pygame.event.get():
                    pygame.display.update()
                    pos = pygame.mouse.get_pos()
                    pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
                    if menu_botoes[0].collidepoint(pos) and pressed1:
                        derramando2(BLUE,19, 373, 468, 170)
                        botoesMenu(PELE,188,313,60,60)
                        pygame.display.flip()
                        return  BLUE
                    elif menu_botoes[1].collidepoint(pos) and pressed1:
                        derramando2(AMARELO,19, 373, 468, 170)
                        botoesMenu(PELE,188,313,60,60)
                        pygame.display.flip()
                        return AMARELO

                    elif menu_botoes[2].collidepoint(pos) and pressed1:
                        derramando2(RED,19, 373, 468, 170)
                        botoesMenu(PELE,188,313,60,60)
                        pygame.display.flip()
                        return RED
                    elif menu_botoes[3].collidepoint(pos) and pressed1:
                       if(fase>= 1):
                           derramando2(GREEN,19, 373, 468, 170)
                           botoesMenu(PELE,188,313,60,60)
                           pygame.display.flip()
                           return GREEN
                    elif menu_botoes[4].collidepoint(pos) and pressed1:
                        if(fase>= 2):
                           derramando2(LARANJA,19, 373, 468, 170)
                           botoesMenu(PELE,188,313,60,60)
                           pygame.display.flip()
                           return LARANJA
                    elif menu_botoes[5].collidepoint(pos) and pressed1:
                        if(fase>= 3):
                           derramando2(ROXO,19, 373, 468, 170)
                           botoesMenu(PELE,188,313,60,60)
                           pygame.display.flip()
                           return ROXO
                    if event.type == QUIT:
                        pygame.quit()
                        exit()
def misturar(cor1,cor2):
        screen.blit(dimensao_botao('btnMistura'),(450,250))
        while True:
            for event in pygame.event.get():
                    pygame.display.update()
                    pos = pygame.mouse.get_pos()
                    pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
                    if menu_botoes[6].collidepoint(pos) and pressed1:
                        resultado = globals.misturar_cores(cor1,cor2)
                        botoesMenu(resultado,19, 373, 468, 305)
                        botoesMenu(PELE,620,560,70,120)
                        pygame.display.update()
                        return resultado
                    if event.type == QUIT:
                        pygame.quit()
                        exit()
def clicarConfirmarOuExcluir():
        botoesMenu(PELE,620,560,70,120)
        pygame.display.update()
        btnConfirmar()
        screen.blit(dimensao_botao('btnExclui'),(550,250))
        while True:
            for event in pygame.event.get():
                    pygame.display.update()
                    pos = pygame.mouse.get_pos()
                    pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
                    if menu_botoes[7].collidepoint(pos) and pressed1:
                        screen.fill(PELE)
                        menu()
                        return 0
                    elif menu_botoes[8].collidepoint(pos) and pressed1:
                         screen.fill(PELE)
                         menu()
                         return 1
                    elif event.type == QUIT:
                        pygame.quit()
                        exit()

regras()

menu()
menu_botoes = menu()

while True:
        if(cont == 1):
                menu()
                cor1 = primeiro()
                cont= cont + 1
        elif(cont == 2):
                cor2 = segundo()
                cont= cont + 1
                pygame.display.flip()
        elif(cont == 3):
            resultado = misturar(cor1,cor2)
            decisao = clicarConfirmarOuExcluir()
            if(decisao==1):
                  if (fase == 0):
                        if(resultado == GREEN):
                              
                              fase = fase + 1
                              cont = 1
                        else:
                              cont = 1
                  elif(fase == 1):
                        if(resultado == LARANJA):
                              fase = 2
                              cont = 1
                        else:
                              cont = 1
                  elif(fase == 2):
                        if(resultado == ROXO):
                              fase = 3
                              cont = 4
                  else:
                        cont = 1
            else:
                cont = 1
        elif(cont == 4):
              pygame.quit()
              exit()
        for event in pygame.event.get():
           if event.type == QUIT:
              pygame.quit()
              exit()
