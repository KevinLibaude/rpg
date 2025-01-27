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
        self.degats = round(0.6*self.force)

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
        
    def getVie(self):
        return self.vie
    
    def getNom(self):
        return self.nom
    
    def getForce(self):
        return self.force
    
    def getEndurance(self):
        return self.endurance
    
    def getRapidité(self):
        return self.rapidité
    
    def getIntelligence(self):
        return self.intelligence
    
    def getCharisme(self):
        return self.charisme
    
    def getMort(self):
        return self.mort
    
    def getDegats(self):
        return self.degats
    
    def afficheCaractéristiques(self):
        print(f"Nom : {self.getNom()}")
        print(f"Vie : {self.getVie()}")
        print(f"Force : {self.getForce()}")
        print(f"Endurance : {self.getEndurance()}")
        print(f"Rapidité : {self.getRapidité()}")
        print(f"Intelligence : {self.getIntelligence()}")
        print(f"Charisme : {self.getCharisme()}")

    def perdVie(self,degats):
        if(self.getVie() < 0):
            print(f"{self.getNom()} a subit une attaque mortelle et est mort")
            return self.getMort()
        else:
            self.vie-=degats

    def gagneVie(self,pvGagnés):
        if(self.getMort() != True):
            self.vie+= pvGagnés
            return f"{self.getNom()} gagne {pvGagnés} points de vie"
        else:
            return f"{self.getNom()} est mort et ne peut pas être soigné"

    def attaque(self,ennemi):
        if(ennemi.getMort() != True and self.getMort() != True):
            ennemi.perdVie(self.degats)
            return f"{self.getNom()} attaque {ennemi.getNom()} et lui inflige {self.degats} points de dégats"
        elif(self.getMort() == True):
            return f"{self.getNom()} est mort et ne peut pas attaquer"
        else:
            return f"{ennemi.getNom()} est mort et ne peut pas recevoir d'attaque"
        
    def soigne(self,autrePersonnage,pointSoignés):
        if(autrePersonnage.getMort() != True and self.getMort() != True):
            autrePersonnage.gagneVie(pointSoignés)
            return f"{self.getNom()} soigne {autrePersonnage.getNom()} et lui donne {pointSoignés} points de vie"
        elif(autrePersonnage.getMort() == True):
            return f"{autrePersonnage.getNom()} est mort et ne peut pas recevoir de soin"
        else:
            return f"{self.getNom()} est mort et ne peut pas donner de soin"

    def esquive(self,autrePersonnage):
        if(autrePersonnage.getMort() != True and self.getMort() != True):
            if(round(self.getRapidité() * 1.2) > autrePersonnage.getRapidité()):
                return f"{self.getNom()} esquive l'attaque de {autrePersonnage.getNom()} car {self.getNom()} a une rapidité de {self.getRapidité()} points alors que {autrePersonnage.getNom()} a une rapidité de {autrePersonnage.getRapidité()} points"
            else:
                return f"{self.getNom()} n'esquive pas l'attaque de {autrePersonnage.getNom()} car {self.getNom()} a une rapidité de {self.getRapidité()} points alors que {autrePersonnage.nom} a une rapidité de {autrePersonnage.getRapidité()} points"
    
        elif(autrePersonnage.getMort() == True):
            return f"{autrePersonnage.getNom()} est mort et ne peut pas esquiver et {self.getNom()} ne peut donc pas lancer d'attaque"
        else:
            return f"{self.getNom()} est mort et ne peut donc pas esquiver"

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