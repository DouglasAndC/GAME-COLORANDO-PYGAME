import pygame
from pygame.locals import *
from pygame import *
import globals
from datetime import datetime
import usuario


pygame.init()

screen_largura = 800
screen_altura = 700
global cont
cont = 1
textboxGroup = pygame.sprite.OrderedUpdates()
screenRefresh = True
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

tempo_fase = 0
now = datetime.now()
horas = now.hour
minu = now.minute
sec = now.second
horas = horas*3600
minu = minu*60

time_inicio = minu + sec + horas
print(time_inicio)
dislpay = pygame.display.set_mode((screen_largura, screen_altura))
pygame.display.set_caption('COLORANDO')
screen = pygame.display.get_surface()
oldbackground = pygame.image.load(globals.get_path() + "\\View\\menu\\rainbow.gif")
background = pygame.transform.scale(oldbackground, (int(400 * 2), int(400 * 2)))
pygame.font.init()
font = pygame.font.get_default_font()

# Tamanho do texto e fonte
text_botaomenu = pygame.font.SysFont(font, 40)
text_titulo = pygame.font.SysFont(font, 100)

screen.blit(background, (0, 0))

centralizado = screen_largura / 2

pygame.mixer.init()

pygame.mixer.music.load(globals.get_path() + '\\Sound\\menu.mpeg')

pygame.mixer.music.play()

click = pygame.mixer.Sound(globals.get_path() + '\\Sound\\click.wav')

def printar_placar():
    data = globals.ler_usuario()
    font = pygame.font.Font(pygame.font.match_font("Arial"), 24)
    y = 150
    iterator = 0
    for i in data:
        iterator += 1
        if iterator == 11:
            break
        campo_texto = [str(iterator)+'. ']
        y += 25
        for j in globals.convert_char(i.get('nome')):
            campo_texto.append(j)
        campo_texto.append(' ')

        texto_nome = str.format("%s" % (globals.convert(campo_texto)))
        texto_score = str.format(" %s" % i.get('score'))
        new_surface_nome = font.render(globals.convert(texto_nome), True, WHITE)
        new_surface_score = font.render(texto_score, True, WHITE)
        new_surface_sep = font.render('........................................ ', True, WHITE)

        screen.blit(new_surface_nome, (175, y))
        screen.blit(new_surface_score, (570, y))
        screen.blit(new_surface_sep, (360, y))

def dimensao_botao(botao):
    btn = pygame.image.load(globals.get_path() + '\\View\\menu\\' + botao + '.png').convert_alpha()
    novo_botao = pygame.transform.scale(btn, (int(372 / 2), int(149 / 2)))
    return novo_botao


def titulo():
    titulo = pygame.image.load(globals.get_path() + '\\View\\menu\\titulo.png').convert_alpha()
    novo_titulo = pygame.transform.scale(titulo, (int(726 / 2), int(217 / 2)))
    screen.blit(novo_titulo, (210, 50))


def botoes_menu(color, x, y, width, height):
    return pygame.draw.rect(screen, color, [x, y, width, height])


def menu():
    btn1 = botoes_menu(BLACK, 300, 200, 372 / 2, 149 / 2)
    btn2 = botoes_menu(BLACK, 300, 300, 372 / 2, 149 / 2)
    btn3 = botoes_menu(BLACK, 300, 400, 372 / 2, 149 / 2)
    btn4 = botoes_menu(BLACK, 300, 600, 372 / 2, 149 / 2)
    screen.blit(background, (0, 0))
    titulo()
    screen.blit(dimensao_botao('btnJogar'), (300, 200))
    screen.blit(dimensao_botao('btnContato'), (300, 300))
    screen.blit(dimensao_botao('btnPlacar'), (300, 400))
    screen.blit(dimensao_botao('btnSair'), (300, 600))
    return btn1, btn2, btn3, btn4


def contatos():
    screen.fill((0, 0, 0))
    btn6 = botoes_menu(BLACK, 300, 500, 372 / 2, 149 / 2)
    screen.blit(background, (0, 0))
    screen.blit(dimensao_botao('btnVoltar'), (300, 500))
    aut = pygame.image.load(globals.get_path() + '\\View\\menu\\contatos.png').convert_alpha()
    novo_aut = pygame.transform.scale(aut, (int(940 / 2), int(620 / 2)))
    screen.blit(novo_aut, (150, 100))
    if btn6.collidepoint(pos) and pressed1:
        click.play()
        screen.fill((0, 0, 0))
        pygame.display.flip()
        menu()
        pygame.display.flip()
        return 1
    else:
        return 0


def botaoVoltar():
    btn6 = botoes_menu(BLACK, 300, 500, 372 / 2, 149 / 2)
    screen.blit(background, (0, 0))
    screen.blit(dimensao_botao('btnVoltar'), (300, 500))
    if btn6.collidepoint(pos) and pressed1:
        screen.fill((0, 0, 0))
        pygame.display.flip()
        menu()
        pygame.display.flip()
        return 1
    else:
        return 0


def primeiro():
    pygame.display.update()
    if menu_botoes[0].collidepoint(pos) and pressed1:
        click.play()
        return 4
    elif menu_botoes[1].collidepoint(pos) and pressed1:
        click.play()
        contatos()
        return 1
    elif menu_botoes[2].collidepoint(pos) and pressed1:
        click.play()
        placar()
        return 3
    elif menu_botoes[3].collidepoint(pos) and pressed1:
        click.play()
        pygame.quit()
        exit()
    else:
        return 0


def jogar():
    texto = []
    screen.fill((0, 0, 0))
    btn1 = botoes_menu(BLACK, 300, 400, 372 / 2, 149 / 2)
    screen.blit(background, (0, 0))
    screen.blit(dimensao_botao('btnJogar'), (300, 400))
    tituloJ = pygame.image.load(globals.get_path() + '\\View\\menu\\txtSeuNome.png').convert_alpha()
    novo_tituoj = pygame.transform.scale(tituloJ, (int(1036 / 2), int(264 / 2)))
    screen.blit(novo_tituoj, (180, 50))
    flag = True
    while True:
        if (flag == False):
            screen.fill((0, 0, 0))
            menu()
            pygame.display.flip()
            return 0
        else:
            pygame.draw.rect(screen, (255, 255, 255), (250, 200, 300, 30))
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
                btn6 = botoes_menu(BLACK, 300, 500, 372 / 2, 149 / 2)
                if len(texto) != 0:
                    btn1 = botoes_menu(BLACK, 300, 400, 372 / 2, 149 / 2)
                screen.blit(background, (0, 0))
                if len(texto) != 0:
                    screen.blit(dimensao_botao('btnJogar'), (300, 400))
                tituloJ = pygame.image.load(globals.get_path() + '\\View\\menu\\txtSeuNome.png').convert_alpha()
                novo_tituoj = pygame.transform.scale(tituloJ, (int(1036 / 2), int(264 / 2)))
                screen.blit(novo_tituoj, (180, 50))
                screen.blit(dimensao_botao('btnVoltar'), (300, 500))
                if event.type == pygame.KEYDOWN:
                    valor = event.key
                    if len(texto) < 27:
                        if 97 <= valor <= 122:
                            texto.append(chr(valor))
                        elif 49 <= valor <= 57:
                            texto.append(chr(valor))
                        elif valor == 32:
                            texto.append(" ")
                    if valor == 8:
                        if len(texto) > 0:
                            texto.pop()
                elif event.type == QUIT:
                    pygame.quit()
                    exit()
                elif len(texto) != 0:
                    if btn1.collidepoint(pos) and pressed1:
                        return usuario.usuario(globals.convert(texto))
                elif btn6.collidepoint(pos) and pressed1:
                    click.play()
                    screen.fill((0, 0, 0))
                    pygame.display.flip()
                    flag = False
                    break

            font = pygame.font.Font(pygame.font.match_font("Arial"), 24)
            pygame.draw.rect(screen, (255, 255, 255), (250, 200, 300, 30))
            text = globals.convert(texto)
            newSurface = font.render(text, True, (0, 0, 0))
            screen.blit(newSurface, (250, 200))
            pygame.display.update()


def placar():
    placar = pygame.image.load(globals.get_path() + '\\View\\menu\\txtPlacar.png').convert_alpha()
    novo_placar = pygame.transform.scale(placar, (int(406 / 2), int(264 / 2)))
    screen.fill((0, 0, 0))
    btn6 = botoes_menu(BLACK, 300, 500, 372 / 2, 149 / 2)
    screen.blit(background, (0, 0))
    screen.blit(novo_placar, (290, 50))
    screen.blit(dimensao_botao('btnVoltar'), (300, 500))
    pygame.draw.rect(screen, BLACK, (100, 155, 600, 325))
    printar_placar()
    if btn6.collidepoint(pos) and pressed1:
        click.play()
        screen.fill((0, 0, 0))
        pygame.display.flip()
        menu()
        pygame.display.flip()
        return 3
    else:
        return 0


def final():
      flag = True
      win = pygame.mixer.Sound(globals.get_path() + '\\Sound\\fase_concluida.wav')
      win.play()
      while True:
         if(flag== False):
            break
         else:
            for event in pygame.event.get():
                font = pygame.font.Font(pygame.font.match_font("Arial"), 100)
                pos = pygame.mouse.get_pos()            
                pressed1,pressed2,pressed3 = pygame.mouse.get_pressed()
                btn10 = botoes_menu(BLACK, 300, 600, 372 / 2, 149 / 2)
                txtFase3 = pygame.image.load(globals.get_path() + '\\View\\menu\\txtParabens.png').convert_alpha()
                txtFase4 = pygame.image.load(globals.get_path() + '\\View\\menu\\txtPontuacao.png').convert_alpha()
                btn11 = botoes_menu(BLACK, 300, 500, 372 / 2, 149 / 2)
                Pontos = font.render(textponto, True, (255, 255, 255))
                screen.blit(background, (0, 0))
                novo_txtFase3 = pygame.transform.scale(txtFase3,(int(655/1.5),int(354/1.5)))
                screen.blit(novo_txtFase3,(200,20))
                screen.blit(txtFase4,(130,200))
                screen.blit(Pontos, (300, 300))
                screen.blit(dimensao_botao('btnSair'), (300, 600))
                screen.blit(dimensao_botao('btnMenu'), (300, 500))
                pygame.display.update()
                if event.type == QUIT:
                  pygame.quit()
                  exit()
                elif btn11.collidepoint(pos) and pressed1:
                    flag = False
                    break
                elif btn10.collidepoint(pos) and pressed1:
                    pygame.quit()
                    exit()



menu()

pygame.display.flip()
screen.blit(background, (0, 0))
menu_botoes = menu()

tela = True

while True:
    pos = pygame.mouse.get_pos()
    pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
    if cont == 1:
        cont = cont + primeiro()
    elif cont == 2:
        cont = cont - contatos()
    elif cont == 3:
        cont = cont + 2
    elif cont == 4:
        cont = cont - placar()
    elif cont == 5:
        globals.aux = jogar()
        if globals.aux == 0:        
            cont = cont - 4
        else:
            import fase_1
            fim = datetime.now()
            horas2 = fim.hour
            minu2 = fim.minute
            sec2 = fim.second
            horas2 = horas2*3600
            minu2 = minu2*60
            time_fim = minu2+ sec2 + horas2

            print(time_inicio)
            print(time_fim)
            
            tempo_fase = time_fim - time_inicio

            score = 1000 - tempo_fase

            novo_score = int(score)
            globals.aux.score = novo_score
            globals.salvar_usuario(globals.aux)
            textponto = str(novo_score)
            display = pygame.display.set_mode((screen_largura, screen_altura))
            final()
            menu()
            cont = 1
    pygame.display.flip()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
