# Ce programme permet de créer un stagiaire avec son nom et ses notes,
# de calculer sa moyenne et de l'afficher.
class Stagiaire:
    def __init__(self, nom):
        # Méthode d'initialisation (constructeur) qui initialise le nom et demande les notes à l'utilisateur
        self.nom = nom                    
        self.note1 = float(input("Entrez la première note : "))  
        self.note2 = float(input("Entrez la deuxième note : "))

    def calc_moy(self):
        return (self.note1 + self.note2) / 2

    def afficher(self):
        moyenne = self.calc_moy()
        print(f"Nom: {self.nom}, Moyenne: {moyenne:.2f}")

# Demande à l'utilisateur d'entrer le nom du stagiaire
nom = input("Entrez le nom du stagiaire : ")
stagiaire = Stagiaire(nom)  

stagiaire.afficher()
