import pickle
class usuario(object):
    def __init__(self, nome):
        self.nome   = nome
        self.score  = 0
        self.level  = 0
    
    def __str__(self):
        return "nome: %s; score: %s; level: %i" % (self.nome,self.score,self.level)

    def save(self):
        data = {}
        try:
            with open('data.json', 'rb') as f:
                data = pickle.load(f)
            with open('data.json', 'wb') as f:
                pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
        except Exception:
            print("Falha ao manipular o arquivo de users")
        return data

Testando = usuario("Douglas")
Testando.save()