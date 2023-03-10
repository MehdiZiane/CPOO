class Forme:
    def perimeter(self):
        print("perimeter is not defind")

class Carre(Forme):
    def __init__(self, cote):
        self.cote = cote 
    
    def perimeter(self):
        super().perimeter()
        return self.cote*4

class rectangle(Forme):
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
    
    def perimeter(self):
        super().perimeter()
        return (self.longueur + self.largeur) *2

class pentagone(Forme):
    def __init__(self,cote):
        self.cote = cote
    
    def perimeter(self):
        super().perimeter()
        return self.cote*5

class triangle(Forme):
    def __init__(self, coteA, coteB, coteC):
        self.coteA = coteA
        self.coteB = coteB
        self.coteC = coteC
    
    def perimeter(self):
        super().perimeter()
        return (self.coteA + self.coteB + self.coteC)
