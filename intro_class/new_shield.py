class employe():
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

class newbie(employe):
    def __init__(self, nom, prenom, age):
        super().__init__(nom, prenom, age)
    
    def salaire(self):
        salaire = 2000
    def first_choice(self):
        choice = input("enter 1 for the car, 2 for a subscribe to the public transit, 3 for the internet and phone subscription")
        if choice == 1:
            print("u choose the car")
        elif choice == 2:
            print("u choose a subscription to public transit")
        elif choice == 3:
            print("u choose the internet and phone subsciption for 60")
        else:
            print("choose a number between 1 or 3")
    def second_choice(self):
        choice = input("enter 1 if u want a laptop or 2 if u want a computer and a screen under 3000")
        if choice == 1:
            print("u choose the laptop")
        elif choice == 2:
            print("ur choose is the computer and the screen")
        else:
            print("enter 1 or 2 for choose")
    def there_is_child(self):
        child_number = input("enter 0 if u have no child else enter the number of ur child")
        if child_number == 0:
            pass
        elif isinstance(child_number, int) and child_number!= 0:
            print(f'u get {child_number} subscribe to disney per years')
        
class old_one(employe):
    def __init__(self, nom, prenom, age, salaire, ancienneté):
        super().__init__(nom, prenom, age)
        self.salaire = salaire
        self.ancienneté = ancienneté
    def bonus(self):
        bonus =  ((5* old_one.ancienneté)/100)* old_one.salaire
        print(f"ur new pay is {bonus}")
    
class commercial(old_one):
    def __init__(self, nom, prenom, age, salaire, ancienneté, new_customer):
        super().__init__(nom, prenom, age, salaire, ancienneté)
        self.new_customer = new_customer
    def bonus_customer(self):
        if commercial.new_customer >= 10:
            commercial.salaire += 400
            print(f"congratulation u found at least 10 new customer ur pay is now {commercial.salaire}")


        

def main():
    newbie.first_choice()
if __name__=='__name__':
    main()