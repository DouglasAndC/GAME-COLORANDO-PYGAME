import os
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