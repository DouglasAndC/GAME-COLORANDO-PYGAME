import pickle
import globals
import json
class usuario(object):

    def __init__(self, nome):
        self.nome   = nome
        self.score  = 0
        self.level  = 0

    def __str__(self):
        return "nome: %s; score: %s; level: %i" % (self.nome,self.score,self.level)
    
    def ler_usuario(self):
        data = {}
        try:
            with open(globals.get_path()+'\Data\data.pickle', 'rb') as f:
                data = pickle.load(f)
            return data
        except Exception as e:
            print(e)
        return data
    
    def salvar_usuario(self):
        user=[{"nome":self.nome,"score":self.score,"level":self.level}]
        try:
            with open(globals.get_path()+'\Data\data.pickle', 'wb') as f:
                pickle.dump(user, f, pickle.HIGHEST_PROTOCOL)
            return True
        except Exception as e:
            print(e)
        return False
    
    def calcular_posicao(self):
        data = self.ler_usuario()
        for i in sorted (data.keys().__getitem__('score')) :  
            print(i, end = " ")

user1 = usuario('Douglas')
user1.salvar_usuario()
user1.calcular_posicao()