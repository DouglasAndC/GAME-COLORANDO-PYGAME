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
        btn1 = botoesMenu(BLACK,630,240,40,70)#azul
        btn2 = botoesMenu(BLACK,630,340,40,70)#laranja
        btn3 = botoesMenu(BLACK,630,440,40,70)#vermelho
        btn4 = botoesMenu(BLACK,730,240,40,70)#verde
        btn5 = botoesMenu(BLACK,730,340,40,70)#amarelo
        btn6 = botoesMenu(BLACK,730,440,40,70)#roxo
        btn7 = botoesMenu(BLACK,620,580,60,100)#juntar
        btn8 = botoesMenu(BLACK,720,560,60,130)#lixo
        screen.fill(PELE)
        titulo()
        torneira()
        balde()
        screen.blit(dimensao_botao('btnAzul'),(450,-100))
        screen.blit(dimensao_botao('btnLaranja'),(450,0))
        screen.blit(dimensao_botao('btnVermelho'),(450,100))
        screen.blit(dimensao_botao('btnVerde'),(550,-100))
        screen.blit(dimensao_botao('btnAmarelo'),(550,0))
        screen.blit(dimensao_botao('btnRoxo'),(550,100))      
        screen.blit(dimensao_botao('btnMistura'),(450,250))           
        screen.blit(dimensao_botao('btnExclui'),(550,250))  
        
        return btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8

def primeiro():
    pygame.display.update()
    pos = pygame.mouse.get_pos()
    pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
    if menu_botoes[0].collidepoint(pos) and pressed1:
        screen.fill(BLACK)
        #Faz algo quando aperta o btn1
    elif menu_botoes[1].collidepoint(pos) and pressed1:
        screen.fill(BLACK)
        #Faz algo quando aperta o btn2
    elif menu_botoes[2].collidepoint(pos) and pressed1:
        screen.fill(BLACK)
        #Faz algo quando aperta o btn3
    elif menu_botoes[3].collidepoint(pos) and pressed1:
        screen.fill(BLACK)
        #Faz algo quando aperta o btn4
    elif menu_botoes[4].collidepoint(pos) and pressed1:
        screen.fill(BLACK)
        #Faz algo quando aperta o btn5
    elif menu_botoes[5].collidepoint(pos) and pressed1:
        screen.fill(BLACK)
        #Faz algo quando aperta o btn6
    elif menu_botoes[6].collidepoint(pos) and pressed1:
        screen.fill(BLACK)
        #Faz algo quando aperta o btn7
    elif menu_botoes[7].collidepoint(pos) and pressed1:
        screen.fill(BLACK)
        #Faz algo quando aperta o btn8

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
menu_botoes = menu()

while True:
       
        primeiro()
        
        pygame.display.flip()
        for event in pygame.event.get():
           if event.type == QUIT:
              pygame.quit()
              exit()
