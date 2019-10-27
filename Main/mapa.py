import pygame
import os
from pygame.locals import *
import globals 


class mapa(object):
    def __init__(self, caminho):
        self.value            = self.ler_mapa(caminho)
        self.img_sub          = self.criar_imgs('sub')
        self.img_sup          = self.criar_imgs('sup')
        self.img_trapezio_p1  = self.criar_imgs('trapezio_p1')
        self.img_trapezio_p2  = self.criar_imgs('trapezio_p2')
        self.img_trapezio_p3  = self.criar_imgs('trapezio_p3')
        self.img_triangulo_p1 = self.criar_imgs('triangulo_p1')
        self.img_triangulo_p2 = self.criar_imgs('triangulo_p2')
        self.img_sol          = self.criar_imgs('sol')
    def ler_mapa(self, caminho):
        path = globals.get_path()
        arquivo_mapa = open(path + "\\" + caminho + '.txt', 'r')
        linha = arquivo_mapa.read()
        arquivo_mapa.close()
        linha = linha.split('\n')
        mapa_lido = []
        for row in linha:
            mapa_lido.append(list(row))
        return mapa_lido

    def criar_imgs(self, nome):
        return pygame.image.load(globals.get_path() + '\\View\\' + nome + '.png').convert_alpha()
