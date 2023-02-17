import os 

def main():
    current = os.getcwd()
    print(current)
    with open(f'{current}/les_fichier/truc.txt', 'r') as f:
        print(f.read())
        f.seek(0)
        copy = f.read()
    with open(f'{current}/les_fichier/cpy.txt', 'w') as f:
        f.write(copy)

if __name__ == "__main__":
    main()