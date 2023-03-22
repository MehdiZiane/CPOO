import random

class Animal():
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    
    def faim(self):
        seuil_faim = 50  
        is_hungry = random.randint(0, 100) 

        if is_hungry < seuil_faim:
            print(f"{self.nom} a faim.")
        else:
            print(f"{self.nom} n'a pas faim.")

class Mammifere(Animal):
    typ = 'mammifere'
    def __init__(self, nom, age, poils, robe, race):
        super().__init__(nom, age)
        self.poils = poils
        self.robe = robe
        self.race = race
    
    def information(self):
        print(f"ce {self.__class__.__name__.lower()} s'appelle {self.nom}, il a {self.age} ans, des poils de type {self.poils} et une robe {self.robe}, de race {self.race}, de type {self.typ}")


class Company():
    
    companylst = []
    
    @classmethod
    def promener(cls):
        for animal in cls.companylst:
            if animal.__class__.__name__ == 'Chien':
                print("les chiens se promene, ils sont heureux")
            else:
                print("les chats se promene seule")
    
    @classmethod
    def jouer(cls):
        attrape = random.choice(cls.companylst)

class Chien(Mammifere):

    def __init__(self, nom, age, poils, robe, race):
        super().__init__(nom,age, poils, robe, race)
        Company.companylst.append(self)
    
    def talking(self):
        speaking_list = ["woaf woaf", "grrr grrr", "wif wif", "pouf pouf"]
        son = random.choice(speaking_list)
        print(f"{self.nom} : {son}")

class chat(Mammifere):
    def __init__(self, nom, age, poils, robe, race):
        super().__init__(nom, age, poils, robe, race)
        Company.companylst.append(self)
    
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
    charlotte= Chien('Charlotte', 18, 'lisse', 'blanche', 'chien de berger')
    patrick= Chien('Patrick', 23,  'boucle', 'noir','terrier')
    bof= Chien('Bof', 11, 'curly', 'brune','tekkel')
    marie = chat('Marie', 1, 'lisse', 'roux', 'siamois')
    toulouse = chat('Toulouse', 1, 'curly','blanc', 'paschat')
    berlioz = chat('Berlioz', 1,'boucle','rouge','pischat' )
    
    Company.promener()

if __name__ == '__main__':
    main()