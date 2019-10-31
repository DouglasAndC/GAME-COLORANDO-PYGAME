import os
import pickle
import json
import usuario

def get_path():
    os.chdir(os.getcwd())
    if(os.getcwd().__contains__('\\Main')):
        os.chdir('../')
    return os.getcwd()

speed = 1.1

def convert(s): 
    new = "" 
    for x in s: 
        new += x  
    return new

def ler_usuario():
    data = []
    try:
        with open(get_path()+'\Data\data.pickle', 'rb') as f:
            data = pickle.load(f)
            f.close()
        return data
    except Exception as e:
        print(e)
    return data

def salvar_usuario(user_name):
    data=ler_usuario()
    data.append(usuario(user_name))
    if(len(data)>1):
        data.sort(key=lambda x: x.score, reverse=True)
    try:
        with open(get_path()+'\Data\data.pickle', 'wb') as f:
            pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
            f.close()
        return True
    except Exception as e:
        print(e)
    return False