from Personnage import Personnage
import random

class Magicien(Personnage):
    def __init__(self, vie, nom, force, endurance, rapidité, intelligence, charisme, race):
        self.nom = nom
        self.vie = vie
        self.force = force
        self.endurance = endurance
        self.rapidité = rapidité
        self.intelligence = intelligence
        self.charisme = charisme
        self.magie = random.randint(0,100)
        self.mort = False
        self.race = race
        self.degats = round(0.8*self.magie)

    def race(self):
        match self.race:
            case "Humain":
                self.magie = random.randint(50,250)
            case "Orc":
                self.magie = random.randint(100,300)

    def superAttaque(self, ennemi):
        return super().attaque(ennemi)

    
Magicien = Magicien(random.randint(0,100), "Gandalf", random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100),"Humain")

Ennemi = Personnage(random.randint(0,100), "Gimli", random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100))

print(Magicien.magie)
print(Magicien.superAttaque(Ennemi))