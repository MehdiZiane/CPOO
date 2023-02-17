import os

def main():
    current = os.getcwd()
    print(current)
    personne = {'name' : '', 'surname':'', 'age':''}
    with open(f'{current}/les_fichiers/enregistrement.txt', 'r+') as f:
        personne["name"] = input("enter a name: ")
        personne["surname"] = input("enter a surname: ")
        personne["age"] = int(input("enter an age: "))
        print(f.read())

if __name__=="__main__":
    main()