import pygame
from pygame.locals import *
import globals
pygame.init()
 
screen_largura = 800
screen_altura = 700

BLACK = (0,0,0)
BLUE = (0, 0, 255)
WHITE = (255,255,255)
 
dislpay = pygame.display.set_mode((screen_largura,screen_altura))
pygame.display.set_caption('COLORANDO')
screen = pygame.display.get_surface()
background = pygame.Surface(screen.get_size())
pygame.font.init()
font = pygame.font.get_default_font()

#Tamanho do texto e fonte
text_botaomenu = pygame.font.SysFont(font,40)
text_titulo = pygame.font.SysFont(font,100)

background.fill((0,0, 0))

centralizado = screen_largura/2

def dimensao_botao(botao):
    btn = pygame.image.load(globals.get_path()+'\\View\\menu\\'+botao+'.png').convert_alpha()  
    novo_botao = pygame.transform.scale(btn,(int(372/2),int(149/2)))
    return novo_botao
    
def titulo():
    titulo = pygame.image.load(globals.get_path()+'\\View\\menu\\titulo.png').convert_alpha()
    novo_titulo = pygame.transform.scale(titulo,(int(726/2), int(217/2)))
    screen.blit(novo_titulo,(210,50))

def botoesMenu(color,x,y,width,height):
    return pygame.draw.rect(screen, color, [x, y, width, height])
    

def menu():
    titulo()
    btn1 = botoesMenu(BLACK,300,200,372/2,149/2)
    screen.blit(dimensao_botao('btnJogar'),(300,200))
    btn2 = botoesMenu(BLACK,300,300,372/2,149/2)    
    screen.blit(dimensao_botao('btnRegras'),(300,300))
    btn3 = botoesMenu(BLACK,300,400,372/2,149/2)
    screen.blit(dimensao_botao('btnContato'),(300,400))
    btn4 = botoesMenu(BLACK,300,500,372/2,149/2)
    screen.blit(dimensao_botao('btnPlacar'),(300,500))
    btn5 = botoesMenu(BLACK,300,600,372/2,149/2)
    screen.blit(dimensao_botao('btnSair'),(300,600))
    return (btn1,btn2,btn3,btn4,btn5)

def jogar():
    screen.fill((0, 0, 0))

menu()

pygame.display.flip()

while True:
    pos = pygame.mouse.get_pos()
    pressed1,pressed2,pressed3 = pygame.mouse.get_pressed()
    menu_botoes = menu()
    if menu_botoes[0].collidepoint(pos) and pressed1:
        jogar()
        pygame.display.flip()
    if menu_botoes[1].collidepoint(pos) and pressed1:
        jogar()
        pygame.display.flip()
    if menu_botoes[2].collidepoint(pos) and pressed1:
        jogar()
        pygame.display.flip()
    if menu_botoes[3].collidepoint(pos) and pressed1:
        jogar()
        pygame.display.flip()
    if menu_botoes[4].collidepoint(pos) and pressed1:
        pygame.quit()
        exit()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
