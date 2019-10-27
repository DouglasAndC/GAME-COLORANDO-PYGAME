import os
def get_path():
    os.chdir(os.getcwd())
    if(os.getcwd().__contains__('\\Main')):
        os.chdir('../')
    return os.getcwd()

speed = 1.1