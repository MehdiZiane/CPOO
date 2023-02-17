from pathlib import Path
import pdb
import os 

def main():    
    current = os.getcwd()
    chemin_fichier= Path("truc.txt").resolve()
    print(chemin_fichier)
    print(current)
    
    #pdb.set_trace # stop le programme 
    with open(f'{current}/les_fichier/truc.txt', 'r') as f:
        print(f.read())
    
    with open(f'{current}/les_fichier/truc.txt', 'a') as f:
        f.write("or maybe not")

    with open(f'{current}/les_fichier/truc.txt', 'r') as f:
        print(f.read())

if __name__ == "__main__":
    main()
