import pickle
import globals

class usuario(object):

    def __init__(self, nome):
        self.nome   = nome
        self.score  = 0
        self.level  = 0

    def __str__(self):
        return "nome: %s; score: %s; level: %i" % (self.nome,self.score,self.level)
    
    def ler_usuario(self):
        try:
            with open(globals.get_path()+'\Data\data.json', 'rb') as f:
                self.data = pickle.load(f)
            return True
        except Exception as e:
            print(e)
        f.close()
        return False
    
    def salvar_usuario(self):
        try:
            with open(globals.get_path()+'\Data\data.json', 'wb') as f:
                pickle.dump(self.data, f, pickle.HIGHEST_PROTOCOL)
            return True
        except Exception as e:
            print(e)
        return False
    
    def calcular_posicao(self):
        for i in sorted (self.data.keys()) :  
            print(i, end = " ") 

Testando = usuario("Douglas")
mapa_data = Testando.save()
print('teste')

