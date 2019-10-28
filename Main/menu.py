import pygame
from pygame.locals import *
from pygame import *
import globals
pygame.init()
 
screen_largura = 800
screen_altura = 700
global cont
cont = 1
textboxGroup = pygame.sprite.OrderedUpdates()
screenRefresh = True
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
    screen.blit(dimensao_botao('btnContato'),(300,300))
    btn3 = botoesMenu(BLACK,300,400,372/2,149/2)
    screen.blit(dimensao_botao('btnPlacar'),(300,400))
    btn4 = botoesMenu(BLACK,300,600,372/2,149/2)
    screen.blit(dimensao_botao('btnSair'),(300,600))
    return (btn1,btn2,btn3,btn4)


def contatos():
    aut = pygame.image.load(globals.get_path()+'\\View\\menu\\contatos.png').convert_alpha()
    novo_aut = pygame.transform.scale(aut,(int(940/2), int(620/2)))
    screen.fill((0, 0, 0))
    screen.blit(novo_aut,(250,100))

def botaoVoltar():
    btn6 = botoesMenu(BLACK,300,500,372/2,149/2)
    screen.blit(dimensao_botao('btnVoltar'),(300,500))
    if btn6.collidepoint(pos) and pressed1:
        screen.fill((0, 0, 0))
        pygame.display.flip()
        menu()
        pygame.display.flip()
        return 1
    else:
        return 0
    
    
def primeiro():
    if menu_botoes[0].collidepoint(pos) and pressed1:
        jogar()
        return 1
    elif menu_botoes[1].collidepoint(pos) and pressed1:
        contatos()
        return 1
    elif menu_botoes[2].collidepoint(pos) and pressed1:
        placar()
        return 1
    elif menu_botoes[3].collidepoint(pos) and pressed1:
        pygame.quit()
        exit()
    else:
        return 0        

            

def jogar():
    texto = []
    screen.fill((0, 0, 0))
    btn1 = botoesMenu(BLACK,300,400,372/2,149/2)
    pygame.draw.rect(screen, (255,255,255),(250, 200, 300, 30))
    screen.blit(dimensao_botao('btnJogar'),(300,400))
    tituloJ = pygame.image.load(globals.get_path()+'\\View\\menu\\txtSeuNome.png').convert_alpha()
    novo_tituoj = pygame.transform.scale(tituloJ,(int(1036/2), int(264/2)))
    screen.blit(novo_tituoj,(180,50))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                valor = event.key
                print(valor)
                if valor >= 97 and valor <= 122:
                    texto.append(chr(valor))
                elif valor>=49 and valor <= 57:
                    texto.append(chr(valor))
                elif valor == 32:
                    texto.append(" ")
                elif valor == 8:
                    if(len(texto)>0):
                        texto.pop()
        font = pygame.font.Font(pygame.font.match_font("Arial"), 24)
        pygame.draw.rect(screen, (255,255,255),(250, 200, 300, 30))
        newSurface = font.render(globals.convert(texto), True, (0,0,0))
        screen.blit(newSurface,(250, 200))
        pygame.display.update()
   
def placar():
    placar = pygame.image.load(globals.get_path()+'\\View\\menu\\txtPlacar.png').convert_alpha()
    novo_placar = pygame.transform.scale(placar,(int(406/2), int(264/2)))
    screen.fill((0, 0, 0))
    screen.blit(novo_placar,(290,50))

    
menu()

pygame.display.flip()

menu_botoes = menu()

tela = True

while True:
    pos = pygame.mouse.get_pos()
    pressed1,pressed2,pressed3 = pygame.mouse.get_pressed()
    if cont == 1:
        cont = cont + primeiro()
    elif cont == 2:
        cont = cont - botaoVoltar()
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
