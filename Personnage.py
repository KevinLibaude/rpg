import random

sep = "---------------------------------------------"
class Personnage:
    def __init__(self, vie, nom, force, endurance, rapidité, intelligence, charisme):
        self.vie = vie
        self.nom = nom
        self.force = force
        self.endurance = endurance
        self.rapidité = rapidité
        self.intelligence = intelligence
        self.charisme = charisme
        self.mort = False

    def estMort(self):
        if(self.vie > 0):
            return " est vivant"
        else:
            self.mort = True
            return " est mort"
    
    def afficheEtat(self):
        if self.vie > 0:
            return f"Il reste {self.vie} points de vie à {self.nom}"
        else:
            self.mort = True
            return f"{self.nom} est mort"
    
    def afficheCaractéristiques(self):
        print(f"Nom : {self.nom}")
        print(f"Vie : {self.vie}")
        print(f"Force : {self.force}")
        print(f"Endurance : {self.endurance}")
        print(f"Rapidité : {self.rapidité}")
        print(f"Intelligence : {self.intelligence}")
        print(f"Charisme : {self.charisme}")

    def perdVie(self,degats):
        if(self.vie < 0):
            print(f"{self.nom} a subit une attaque mortelle et est mort")
            return self.estMort()
        else:
            self.vie-=degats

    def gagneVie(self,pvGagnés):
        if(self.mort != True):
            self.vie+= pvGagnés
            return f"{self.nom} gagne {pvGagnés} points de vie"
        else:
            return f"{self.nom} est mort et ne peut pas être soigné"

    def attaque(self,ennemi):
        if(ennemi.mort != True and self.mort != True):
            degats = round(0.6*self.force)
            ennemi.perdVie(degats)
            return f"{self.nom} attaque {ennemi.nom} et lui inflige {degats} points de dégats"
        elif(self.mort == True):
            return f"{self.nom} est mort et ne peut pas attaquer"
        else:
            return f"{ennemi.nom} est mort et ne peut pas recevoir d'attaque"
        
    def soigne(self,autrePersonnage,pointSoignés):
        if(autrePersonnage.mort != True and self.mort != True):
            autrePersonnage.gagneVie(pointSoignés)
            return f"{self.nom} soigne {autrePersonnage.nom} et lui donne {pointSoignés} points de vie"
        elif(autrePersonnage.mort == True):
            return f"{autrePersonnage.nom} est mort et ne peut pas recevoir de soin"
        else:
            return f"{self.nom} est mort et ne peut pas donner de soin"

    def esquive(self,autrePersonnage):
        if(autrePersonnage.mort != True and self.mort != True):
            if(round(self.rapidité * 1.2) > autrePersonnage.force):
                return f"{self.nom} esquive l'attaque de {autrePersonnage.nom} car {self.nom} a une rapidité de {self.rapidité} alors que {autrePersonnage.nom} a une rapidité de {autrePersonnage.rapidité}"
        elif(autrePersonnage.mort == True):
            return f"{autrePersonnage.nom} est mort et ne peut pas esquiver"
        else:
            return f"{self.nom} est mort et ne peut pas esquiver"

    def seDeplace(self,pointDeplacement):
        pass
    

    
if __name__ == '__main__':

    guerrier = Personnage(random.randint(0,100), "Bob", random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100))
    
    ennemie = Personnage(random.randint(0,100), "Alice", random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100))
    
    magicien = Personnage(random.randint(0,100), "Gogolum", random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100))



    print(sep)

    print(f"{guerrier.nom}{guerrier.estMort()}")
    guerrier.afficheCaractéristiques()

    print(sep)

    print(ennemie.attaque(guerrier))
    print(guerrier.afficheEtat())
    print(sep)

    print(guerrier.gagneVie(10))
    print(guerrier.afficheEtat())
    print(sep)

    print(guerrier.attaque(ennemie))
    print(ennemie.afficheEtat())
    print(sep)

    print(magicien.soigne(ennemie,12))
    print(ennemie.afficheEtat())
    print(sep)

    print(guerrier.esquive(ennemie))
    print(sep)

    print(guerrier.seDeplace(5))