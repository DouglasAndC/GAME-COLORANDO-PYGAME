import globals


class Usuario(object):

    def __init__(self, nome):
        self.nome = nome
        self.score = 0
        self.level = 0
        self.pos_x = 104
        self.pos_y = 142

    @property
    def __str__(self):
        return "nome: %s; score: %s; level: %i" % (self.nome, self.score, self.level)
