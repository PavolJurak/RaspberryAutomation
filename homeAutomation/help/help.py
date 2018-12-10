import os
import glob

def clear_graph_files():
    filelist = glob.glob(os.getcwd()+'\static\graph\*.png')
    for file in filelist:
        print(file)
        os.remove(file)