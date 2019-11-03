import pygame
from pygame.locals import *
from pygame import *
import globals
import pygame as pg


pg.init()
# definindo cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
COR1 = (153, 0, 153)
PELE = (251, 230, 226)
CorSelecionada = (0, 255, 0)


pygame.init()

screen = pygame.display.set_mode((800, 700))
# carregando fonte
font = pygame.font.SysFont(None, 55)

pygame.display.set_caption('Olá mundo')

# preenchendo o fundo com preto
screen.fill(PELE)
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

def menu():
        titulo()
        torneira()
        balde()
        #Criando Retangulos
        #Reta caindo 1
        #pygame.draw.rect(screen, CorSelecionada, [188, 313, 60, 365])
        #Retangulo Balde Preenchido
        #pygame.draw.rect(screen, CorSelecionada, [19, 373, 468, 305])
        #Retangulo até metade
        #pygame.draw.rect(screen, CorSelecionada, [19, 508, 468, 170])
        #Retangulo acima metade
        #pygame.draw.rect(screen, CorSelecionada, [19, 373, 468, 170])
        #Retangulo Caindo ate metade
        #pygame.draw.rect(screen, BLUE, [188, 313, 60, 195])
        

        
        

        btn1 = botoesMenu(BLACK,0,0,0,0)
        screen.blit(dimensao_botao('btnVerde'),(550,-100))
        btn2 = botoesMenu(BLACK,0,0,0,0)
        screen.blit(dimensao_botao('btnAzul'),(450,-100))
        btn3 = botoesMenu(BLACK,0,0,0,0)
        screen.blit(dimensao_botao('btnAmarelo'),(550,0))
        btn4 = botoesMenu(BLACK,0,0,0,0)
        screen.blit(dimensao_botao('btnLaranja'),(450,0))
        btn5 = botoesMenu(BLACK,0,0,0,0)
        screen.blit(dimensao_botao('btnRoxo'),(550,100))
        btn6 = botoesMenu(BLACK,0,0,0,0)
        screen.blit(dimensao_botao('btnVermelho'),(450,100))
        btn7 = botoesMenu(BLACK,0,0,0,0)
        screen.blit(dimensao_botao('btnMistura'),(450,250))
        btn8 = botoesMenu(BLACK,0,0,0,0)
        screen.blit(dimensao_botao('btnExclui'),(550,250))

        return (btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,)

def btnVerde():
    if btn1.collidepoint(pos) and pressed1:
        pygame.draw.rect(screen, GREEN, [19, 508, 468, 170])
        pygame.display.flip()
        menu()
        pygame.display.flip()
        return 1
    else:
        return 0
    
    #def btnAzul():
    #def btnAmarelo():
    #def btnLaranja():
    #def btnRoxo():
    #def btnVermelho():
    #def btnMistura():
    #def btnExclui():
    #def btn():



        
menu()
# desenhando na superfície 
#pygame.draw.line(screen, WHITE, [10, 100], [630, 100], 5)
#pygame.draw.rect(screen, BLUE, [200, 210, 40, 20])
#pygame.draw.ellipse(screen, RED, [300, 200, 40, 40])
#pygame.draw.polygon(screen, GREEN, [[420, 200], [440, 240], [400, 240]])

# atualizando a tela
pygame.display.flip()

time.sleep(5)

# preenchendo o fundo com preto
screen.fill(BLACK)

# definindo o texto
text = font.render('pygame', True, WHITE)
# copiando o texto para a superfície
screen.blit(text, [250, 200])

# atualizando a tela
pygame.display.flip()

time.sleep(5)
