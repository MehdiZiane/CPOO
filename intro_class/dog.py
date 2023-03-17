import random

class company:
    def __init__(self):
        pass

class Chien(company):
    dogtype = "mammifère"

    def __init__(self, nom, age, poils, robe, race, hungry):
        self.nom = nom
        self.age = age
        self.poils = poils
        self.robe = robe
        self.race = race
        self.hungry = hungry
    def talking(self):
        speaking_list = ["woaf woaf", "grrr grrr", "wif wif", "pouf pouf"]
        son = random.choice(speaking_list)
        print(f"{self.nom} : {son}")
    def information(self):
        print(f"ce chien s'appelle {self.nom}, il a {self.age} ans, des poils de type {self.poils} et une robe {self.robe}, de race {self.race}")
    def hungry(self):
        if is_hungry < 50:
            print(f"{self.nom} a faim")

def oldest_dog(chiens):
    max_age = -1
    oldest_dog = None
    for chien in chiens:
        if chien.age > max_age:
            max_age = chien.age
            oldest_dog = chien
    return oldest_dog

def younger_dog(chiens):
    min_age=float('inf')
    younger_dog=None
    for chien in chiens:
        if chien.age<min_age:
            min_age = chien.age
            younger_dog = chien
    return younger_dog



def main():
    chien1 = Chien('Charlotte', 18, 'lisse', 'blanche', 'chien de berger')
    chien2 = Chien('Patrick', 23,  'boucle', 'noir','terrier')
    chien3 = Chien('Bof', 11, 'curly', 'brune','tekkel')
    print(chien3.nom)
    chiens = [chien1, chien2, chien3]
    oldest = oldest_dog(chiens)
    print("le plus vieux chien est", oldest.nom, "il a",oldest.age )
    younger = younger_dog(chiens)
    print("le plus jeune chien est", younger.nom, "il a", younger.age)
    chien1.talking()
    chien2.talking()
    chien3.talking()
    chien1.information()


if __name__ == '__main__':
    main()