import subprocess
import sys
import os

def log(msg: str):
    print(msg)

def help():
    pass



if __name__ == "__main__":

    if sys.argv > 2:
        print("Too many args")
        break
    
    path: str = os.path.abspath(os.getcwd())

    if not (os.path.isdir(path + "/target")):
        logger("Target not found... making dir")
        os.mkdir(path + "/target")

    file: str = sys.argv[-1]

    subprocess.run(["pdflatex", file])
    subprocess.run()
    

    
        


        
            
    
    