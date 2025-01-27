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
        self.race = race

    def race(self):
        match self.race:
            case "Humain":
                self.magie = random.randint(50,250)

    
Magicien = Magicien(random.randint(0,100), "Gogolum", random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100),"Humain")

print(Magicien.magie)