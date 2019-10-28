import globals
class usuario(object):

    def __init__(self, nome):
        self.nome   = nome
        self.score  = 0
        self.level  = 0

    def __str__(self):
        return "nome: %s; score: %s; level: %i" % (self.nome,self.score,self.level)
        
