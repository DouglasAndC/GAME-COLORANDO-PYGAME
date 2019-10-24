import pygame
from pygame.locals import *

pygame.init()
 
screen_largura = 800
screen_altura = 700

BLUE = (0, 0, 255)
WHITE = (255,255,255)
 
dislpay = pygame.display.set_mode((screen_largura,screen_altura))
pygame.display.set_caption('COLORANDO')
screen = pygame.display.get_surface()
background = pygame.Surface(screen.get_size())
pygame.font.init()
font = pygame.font.get_default_font()


btnJogar = pygame.image.load('menu\\btnJogar.png').convert_alpha()
btnRegras = pygame.image.load('menu\\btnRegras.png').convert_alpha()
btnContato = pygame.image.load('menu\\btnContato.png').convert_alpha()
btnPlacar = pygame.image.load('menu\\btnPlacar.png').convert_alpha()
btnSair = pygame.image.load('menu\\btnSair.png').convert_alpha()

#Tamanho do texto e fonte
text_botaomenu = pygame.font.SysFont(font,40)
text_titulo = pygame.font.SysFont(font,100)

background.fill((0, 0, 0))

centralizado = screen_largura/2

def dimensao_botao(botao):
    novo_botao = pygame.transform.scale(botao,(int(372/2),int(149/2)))
    return novo_botao
    
def titulo():
    titulo = pygame.image.load('menu\\titulo.png').convert_alpha()
    novo_titulo = pygame.transform.scale(titulo,(int(726/2), int(217/2)))
    screen.blit(novo_titulo,(210,50))

def botoesMenu(color,x,y,width,height,titulo,posicaoTexto):
    pygame.draw.rect(screen, color, [x, y, width, height])
    textoBotao = text_botaomenu.render(titulo, 1,WHITE)        
    screen.blit(textoBotao,(posicaoTexto,y))
    

class menu:
    titulo()
    screen.blit(dimensao_botao(btnJogar),(300,200))
    screen.blit(dimensao_botao(btnRegras),(300,300))
    screen.blit(dimensao_botao(btnContato),(300,400))
    screen.blit(dimensao_botao(btnPlacar),(300,500))
    screen.blit(dimensao_botao(btnSair),(300,600))


menu()

pygame.display.flip()

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
