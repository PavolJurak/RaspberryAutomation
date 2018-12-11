from os import remove, path, getcwd
import glob

def clear_graph_files():
    filelist = glob.glob(path.join(getcwd(),'static','graph','*.png'))
    for file in filelist:
        remove(file)