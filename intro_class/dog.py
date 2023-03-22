import random

class Animal():
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    
    def faim(self):
        seuil_faim = 50  # seuil de faim
        is_hungry = random.randint(0, 100)  # génère un nombre aléatoire entre 0 et 100

        if is_hungry < seuil_faim:
            print(f"{self.nom} a faim.")
        else:
            print(f"{self.nom} n'a pas faim.")

class company(Animal):
    def __init__(self, nom, age, poils, robe, race):
        super().__init__(nom, age)
        self.poils = poils
        self.robe = robe
        self.race = race
    
    def information(self):
        print(f"ce {self.__class__.__name__.lower()} s'appelle {self.nom}, il a {self.age} ans, des poils de type {self.poils} et une robe {self.robe}, de race {self.race}")

class Chien(company):
    dogtype = "mammifère"

    def __init__(self, nom, age, poils, robe, race):
        super().__init__(nom,age, poils, robe, race)
    
    def talking(self):
        speaking_list = ["woaf woaf", "grrr grrr", "wif wif", "pouf pouf"]
        son = random.choice(speaking_list)
        print(f"{self.nom} : {son}")

class chat(company):
    def __init__(self, nom, age, poils, robe, race):
        super().__init__(nom, age, poils, robe, race)
    
    def talking(self):
        speaking_list = ["grrr grrr", "miaow miaow", "chip chip"]
        son = random.choice(speaking_list)
        print(f"{self.nom} : {son}")

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
    chiens = [chien1, chien2, chien3]
    oldest = oldest_dog(chiens)
    print("le plus vieux chien est", oldest.nom, "il a",oldest.age )
    younger = younger_dog(chiens)
    print("le plus jeune chien est", younger.nom, "il a", younger.age)
    chien1.talking()
    chien2.talking()
    chien3.talking()
    chien1.information()
    chien1.faim()
    chat1 = chat('alphonse', 10, 'lisse', 'roux', 'siamois')
    print(chat1.nom)
    chat1.talking()
    chat1.information()
    chat1.faim()

if __name__ == '__main__':
    main()