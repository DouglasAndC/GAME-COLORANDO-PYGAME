import pygame
 
pygame.init()
 
screen_largura = 800
screen_altura = 600

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

background.fill((0, 0, 0))

centralizado = screen_largura/2

def titulo():
    textoTitulo = text_titulo.render('COLORANDO', 1,WHITE)        
    screen.blit(textoTitulo,(175,100))

def botoesMenu(color,x,y,width,height,titulo,posicaoTexto):
    pygame.draw.rect(screen, color, [x, y, width, height])
    textoBotao = text_botaomenu.render(titulo, 1,WHITE)        
    screen.blit(textoBotao,(posicaoTexto,y))
    

class menu:
    titulo()
    btnJogar = botoesMenu(BLUE,300,250,200,30,'Jogar',360)
    btnRegras = botoesMenu(BLUE,300,300,200,30,'Regras',355)
    btnContato = botoesMenu(BLUE,300,350,200,30,'Contato',350)
    btnPlacar = botoesMenu(BLUE,300,400,200,30,'Placar',355)
    btnSair = botoesMenu(BLUE,300,500,200,30,'Sair',370)


menu()

pygame.display.flip()
