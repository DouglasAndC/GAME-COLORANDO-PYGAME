import os
def get_path():
    os.chdir("../")
    print(os.getcwd())
    return os.getcwd()